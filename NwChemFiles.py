import glob
import os
import shutil

path = 'C:/Users/Gavin/Desktop/NWchem/Plain/'
path1 = 'C:/Users/Gavin/Desktop/NWchem/Stuttgart/'

func = ['b3lyp', 'm06', 'm06-2x', 'pbe96', 'pbe0', 'vwn_1', 'tpss03', 'xctpssh']

fil = ['La', 'Ce', 'Pr', 'Nd', 'Eu', 'Gd', 'Dy', 'Ho', 'Er', 'Lu']

lanth = {'La':'mult 1', 'Ce':'mult 2', 'Pr':'mult 3', 'Nd':'mult 4', 'Pm':'mult 5', 'Sm':'mult 6', 'Eu':'mult 7', 'Gd':'mult 8',
         'Tb':'mult 7', 'Dy':'mult 6', 'Ho':'mult 5', 'Er':'mult 4', 'Tm':'mult 3', 'Yb':'mult 2', 'Lu':'mult 1'}



for item in fil:
    geo = str(path) + str(item) + '.xyz'
    basis = str(path1) + str(item) + '.txt'

    for items in func:
        path2 = str(path) + str(item) + '/' + str(items) + '/'

        if not os.path.exists(path2):
            os.makedirs(path2)
        
        nw = open(str(path2) + str(item) + '_' + str(items) + '.nw', "w")

        nw.write("start " + str(item) + '_' + str(items) +
                 "\nmemory 2048 mb\n" +
                 "charge 3\n" +
                 "geometry units angstrom\n")

        with open(geo) as f:
            count = 0
            count1 = 0
            for line in f:
                for k,v in lanth.items():
                    if str(k) in line:
                        mult = v
                count += 1
                if count > 2:
                    nw.write(line)

        nw.write("End\n")

        with open(basis) as f:
            count = 0
            for line in f:
                count += 1
                if count == 1:
                    nw.write(line)
                    nw.write("o library aug-cc-pVDZ\nh library aug-cc-pVDZ\n")
                else:
                    nw.write(line)
        

        nw.write("dft\n xc ")
        if str(items) == 'pbe96' or str(items) == 'tpss03':
            nw.write('x' + str(items) + ' c' + str(items) + '\n')
            nw.write(" convergence energy 1e-7\n grid xfine\n iterations 600\n maxiter 40\n " + str(mult) + '\n' + 
                 " RODFT\nend\ntask dft optimize")
        else:
            nw.write(str(items) + "\n convergence energy 1e-7\n grid xfine\n iterations 600\n maxiter 40\n " + str(mult) + '\n' + 
                 " RODFT\nend\ntask dft optimize")
        nw.close()

        pbs = open(str(path2) + '/submit.pbs', "w")

        pbs.write("#PBS -A ACF-UTK0022\n" + 
                  "#PBS -l nodes=1:ppn=16\n" + 
                  "#PBS -l mem=10000mb\n" + 
                  "#PBS -l walltime=20:00:00\n" + 
                  #"#PBS -l partition=rho\n"  + 
                  "#PBS -N " + str(item) + "_" + str(items) + "\n" + 
                  "#PBS -M gmccarve@vols.utk.edu\n" +
                  "#PBS -m bae\n\n" +
                  "cd $PBS_O_WORKDIR\n\n" +
                  "module load nwchem\n" +
                  "mpirun -np 16 nwchem " + str(item) + "_" + str(items) + ".nw > "+ str(item) + "_" + str(items)+ ".out")

        pbs.close()



for item in fil:
    count2 = 0
    submit = str(path) + str(item) + '/' + 'submit'
    with open(submit, 'w') as f:
        for item in func:
            if count2 == 0 :
                f.write('cd ' + str(item) + '_' + str(items) + '/\n' + 'qsub submit.pbs\n')
                count2 += 1
            else:
                f.write('cd ../' + str(item) + '_' + str(items) + '/\n' + 'qsub submit.pbs\n')
                count2 += 1
        """submit = open(str(path) + str(item) + '/' + 'submit', 'w')

        submit.write('cd ' + str(item) + '_' + str(items) + '/\n' + 'qsub submit.pbs\n')

        if count2 == 0:
            submit.write('cd ' + str(item) + '_' + str(items) + '/\n' + 'qsub submit.pbs\n')
            count2 += 1
        else:
            submit.write('cd ../' + str(item) + '_' + str(items) + '/\n' + 'qsub submit.pbs\n')     

    
    submit.close()"""







        
