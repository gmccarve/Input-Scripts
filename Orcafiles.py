import glob
import os
import shutil

path = 'C:/Users/Gavin/Desktop/Structures/Orca/LaF/'
#path = '/nics/d/home/gmccarve/haven/Orca/Prescreen/LaF/'

func = {'LDA':' RI ', 'BP':' RI ', 'PW91':' RI ', 'BLYP':' RI ', 'PBE':' RI ', 'OLYP':' RI ', 'OPBE':' RI ', 'M06L':' RI ', 'TPSS':' RI ', 'B3LYP':' RIJCOSX ', 'O3LYP':' RIJCOSX ',
        'PBE0':' RIJCOSX ', 'M06':' RIJCOSX ', 'M06-2x':' RIJCOSX ', 'TPSSH':' RIJCOSX '}

basis = ['SarcD', 'SarcZ', 'Sarc2D', 'Sarc2Z', 'ANOD', 'ANOZ', 'Def2', 'Sapporo', 'Stuttgart']

for k in basis:
    
    path3 = path + str(k) + '/'  
    if not os.path.exists(path3):
            os.makedirs(path3)
    quick = open(path3 + 'quick', 'w')
    
    for key,value in func.items():

        path2 = path + str(k) + '/' + str(key) + '/'
        if not os.path.exists(path2):
            os.makedirs(path2)

        
        orca = open(path2 + 'orca.inp', 'w')
        submit = open(path2 + 'submit.pbs', 'w')

        if k == 'SarcD':
            orca.write('! ' + str(key) + str(value) + 'SARC-DKH-TZVP OPT DKH AUTOAUX\n')
            orca.write('%basis\n        newgto F "DKH-def2-TZVP"end\nend\n')

        if k == 'SarcZ':
            orca.write('! ' + str(key) + str(value) + 'SARC-ZORA-TZVP OPT ZORA AUTOAUX\n')
            orca.write('%basis\n        newgto F "ZORA-def2-TZVP"end\nend\n')

        if k == 'Sarc2D':
            orca.write('! ' + str(key) + str(value) + 'SARC2-DKH-QZV OPT DKH AUTOAUX\n')
            orca.write('%basis\n        newgto F "DKH-def2-TZVP"end\nend\n')

        if k == 'Sarc2Z':
            orca.write('! ' + str(key) + str(value) + 'SARC2-ZORA-QZV OPT ZORA AUTOAUX\n')
            orca.write('%basis\n        newgto F "ZORA-def2-TZVP"end\nend\n')

        if k == 'ANOD':
            orca.write('! ' + str(key) + str(value) + 'ANO-RCC-TZP OPT DKH AUTOAUX\n')

        if k == 'ANOZ':
            orca.write('! ' + str(key) + str(value) + 'ANO-RCC-TZP ZORA OPT AUTOAUX\n')

        if k == 'Def2':
            orca.write('! ' + str(key) + str(value) + 'Def2-TZVP OPT AUTOAUX\n')

        if k == 'Sapporo':
            orca.write('! ' + str(key) + str(value) + 'Sapporo-DKH3-TZP-2012 DKH OPT AUTOAUX\n')
            orca.write('%basis\n        newgto F "Sapporo-TZP-2012" end\nend\n')

        if k == 'Stuttgart':
            orca.write('! ' + str(key) + str(value) + 'ZORA OPT AUTOAUX\n')
            orca.write('%basis\n        newgto F\n' +
                        'S   3\n' +
                        '  1     51.6427630              0.0085660\n' +
                        '  2      9.4142770             -0.1530090\n' +
                        '  3      1.2141230              0.5898350\n' +
                        'S   1\n'
                        '  1      0.3700810              1.0000000\n' +
                        'P   3\n' +
                        '  1     22.3008300              0.0518510\n' +
                        '  2      4.9545730              0.2372870\n' +
                        '  3      1.3423110              0.5076660\n' +
                        'P   1\n' +
                        '  1      0.3465300              1.0000000\n' +
                        'P   1\n' +
                        '  1      0.0847720              1.0000000\nend\n')
            orca.write('        newgto La\n' +
                        'S   5\n' +
                          '1  60228.6130000              0.0000030\n' +
                          '2   7142.4190000              0.0000350\n' +
                          '3   1034.3051000              0.0003290\n' +
                          '4    563.4427000             -0.0001060\n' +
                          '5    123.5532000              0.0032800\n' +
                        'S   1\n' +
                          '1     34.5544000              1.0000000\n' +
                        'S   1\n' +
                          '1     24.6330000              1.0000000\n' +
                        'S   1\n' +
                          '1     11.2660000              1.0000000\n' +
                        'S   1\n' +
                          '1      2.9062000              1.0000000\n' +
                        'S   1\n' +
                          '1      1.5433000              1.0000000\n' +
                        'S   1\n' +
                          '1      0.5672000              1.0000000\n' +
                        'S   1\n' +
                          '1      0.2539000              1.0000000\n' +
                        'S   1\n' +
                          '1      0.0467000              1.0000000\n' +
                        'S   1\n' +
                          '1      0.0200000              1.0000000\n' +
                        'P   6\n' +
                          '1   3966.3547000              0.0000040\n' +
                          '2   1143.9280000              0.0000330\n' +
                          '3    446.9977000              0.0000340\n' +
                          '4    229.5466000              0.0003620\n' +
                          '5     27.3267000             -0.0071360\n' +
                          '6     19.4864000              0.2066540\n' +
                        'P   1\n' +
                          '1     13.9024000              1.0000000\n' +
                        'P   1\n' +
                          '1      4.2361000              1.0000000\n' +
                        'P   1\n' +
                          '1      2.2936000              1.0000000\n' +
                        'P   1\n' +
                          '1      1.1258000              1.0000000\n' +
                        'P   1\n' +
                          '1      0.5279000              1.0000000\n' +
                        'P   1\n' +
                          '1      0.2292000              1.0000000\n' +
                        'P   1\n' +
                          '1      0.0800000              1.0000000\n' +
                        'D   6\n' +
                         ' 1    367.7157000              0.0000740\n' +
                          '2    113.5768000              0.0006120\n' +
                          '3     33.5588000              0.0076870\n' +
                          '4     14.4198000             -0.0765100\n' +
                          '5      7.3159000              0.1517540\n' +
                          '6      3.9483000              0.4218730\n' +
                        'D   1\n' +
                          '1      2.0150000              1.0000000\n' +
                        'D   1\n' +
                          '1      0.9581000              1.0000000\n' +
                        'D   1\n' +
                          '1      0.3109000              1.0000000\n' +
                        'D   1\n' +
                          '1      0.0954000              1.0000000\n' +
                        'F   5\n' +
                          '1    124.7971000              0.0011500\n' +
                          '2     43.9427000              0.0143330\n' +
                          '3     19.2668000              0.0625940\n' +
                          '4      8.4893000              0.1640000\n' +
                          '5      3.7672000              0.2858630\n' +
                        'F   1\n' +
                          '1      1.5902000              1.0000000\n' +
                        'F   1\n' +
                          '1      0.6098000              1.0000000\n' +
                        'F   1\n' +
                          '1      0.1973000              1.0000000\n' +
                        'G   4\n' +
                          '1     19.2668000             -0.0021180\n' +
                          '2      8.4893000              0.0267090\n' +
                          '3      3.7672000             -0.0296670\n' +
                          '4      1.5902000              0.2827850\n' +
                        'G   1\n' +
                          '1      0.6098000              1.0000000\n' +
                        'G   1\n' +
                          '1      0.1973000              1.0000000\nend\n' +
                        ' end\n' +
                        'delECP F\nend\n')

        orca.write('%scf\n' +
                        'maxiter 600\n' +
                        'CNVDIIS 0\n' +
                        'end\n' +
                        '* xyz 0 1\n' +
                        'La 0 0 0\n' +
                        'F 0 0 2\n' +
                        '*')
        orca.close()
        submit.write('#PBS -A ACF-UTK0022\n' +
                        '#PBS -l nodes=1:ppn=1\n' +
                        '#PBS -l mem=2000mb\n' +
                        '#PBS -l walltime=23:59:59\n' +
                        '#PBS -N LaF-' + str(k) + '-' + str(key) + '\n' +
                        '#PBS -M gmccarve@vols.utk.edu\n' +
                        '#PBS -m bae\n\n' +
                        'cd $PBS_O_WORKDIR\n\n' +
                        'orca orca.inp > orca.out')
        submit.close()


        quick.write('cd\n')
        quick.write('cd haven/Orca/Prescreen/LaF/' + str(k) + '/' + str(key) + '/\n')
        quick.write('qsub submit.pbs\n')
    quick.close()
    
