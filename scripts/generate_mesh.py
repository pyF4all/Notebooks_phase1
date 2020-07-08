'''
This script copies molecule data from MJ Schnieders Dropbox
'''
import os
import numpy
from argparse import ArgumentParser

parser = ArgumentParser(description='Read in Tinker and output xyzr')
parser.add_argument('--solute', action='store_true',
                    help="Set if vdw radii will be read from the SOLUTE keyword")
parser.add_argument('-f', '--folder', dest='problem_folder', type=str, default='/home/chris/Dropbox/Implicit\ Solvent/testCasesV3/alkane/',
                    help='Folder cotaining files for molecules in molecule_names.txt.')
parser.add_argument('-n', '--names', dest='names_file', type=str, default='molecule_names.txt',
                    help='File containing the molecule names')
parser.add_argument('-prm', '--parameter_file', dest='parameter_file', type=str, default='no_prm_file',
                    help='prm file')


for line in file(parser.parse_args().names_file):

    mol = line[:-1]

    # Generate folder for molecule
    if not(os.path.isdir(mol)):
        cmd = 'mkdir ' +  mol 
        os.system(cmd)

    # Copy xyz and prm files
    cmd = 'cp ' + parser.parse_args().problem_folder + mol + '/' + mol + '.xyz ' + mol + '/'
    os.system(cmd)
    if parser.parse_args().parameter_file == 'no_prm_file':
        cmd = 'cp ' + parser.parse_args().problem_folder + mol + '/' + mol + '.prm ' + mol + '/'
        os.system(cmd)

    # Create key file calling prm
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_key = open(mol + '/' + mol + '.key','w')
    if parser.parse_args().parameter_file == 'no_prm_file':
        file_key.write('parameters\t' + dir_path + '/' + mol + '/' + mol + '.prm')
    else:
        file_key.write('parameters\t' + parser.parse_args().parameter_file)
    file_key.close()

    # Create xyzr file (uses tinker_to_xyzr.py from pygbe repo)
    if parser.parse_args().solute:
        cmd = 'python /home/chris/git_repo/pygbe_cdcooper/scripts/tinker_to_xyzr.py -f ' + mol + '/' + mol + ' --solute'
    else:
        cmd = 'python /home/chris/git_repo/pygbe_cdcooper/scripts/tinker_to_xyzr.py -f ' + mol + '/' + mol
    os.system(cmd)

    if parser.parse_args().solute:
        filename_xyzr = mol + '/' + mol + '_solute.xyzr'
    else:
        filename_xyzr = mol + '/' + mol + '.xyzr'

    # Generate mesh of dielectric interface
    cmd = 'msms -if '+filename_xyzr+' -of ' + mol + '/surf_d16_p0.1 -d 16 -p 0.1 -no_header'

    os.system(cmd)
