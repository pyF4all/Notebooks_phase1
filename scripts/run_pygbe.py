import os
import numpy
import glob
from argparse import ArgumentParser

parser = ArgumentParser(description='Run PyGBe for multiple cases')
parser.add_argument('-o', '--output', dest='output_file', type=str, default='output',
                    help='Filename of output to store values of solvation energy')
parser.add_argument('-n', '--names', dest='names_file', type=str, default='molecule_names.txt',
                    help='File containing the molecule names')


dGsolv = []
mol_array = []
for line in file(parser.parse_args().names_file):

    mol = line[:-1]
    mol_array.append(mol)

    # run pygbe 
    cmd = 'pygbe ' + mol + '/ --polarizable'
    os.system(cmd)

    # find latest log file
    log_files = glob.glob(mol + '/output/*.log')
    latest_log = max(log_files, key=os.path.getctime)

    # read log file
    print ('Reading output from: '+latest_log)
    for line_log in file(latest_log):
        line_log = line_log.split()
        if len(line_log)>4:
            if line_log[0]=='Total' and line_log[1]=='solvation' and line_log[2]=='energy':
                dGsolv.append(line_log[4])

    # Check that dGsolv was found
    if len(mol_array) != len(dGsolv):
        print ('Something went wrong! Not the same number of mol and dG')

write_file = open(parser.parse_args().output_file, 'w')
for i in range(len(mol_array)):
    write_file.write(mol_array[i]+' '+dGsolv[i]+'\n')
write_file.close()
