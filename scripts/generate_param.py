import os 
from argparse import ArgumentParser

parser = ArgumentParser(description='Generate param files for PyGBe')
parser.add_argument('-n', '--names', dest='names_file', type=str, default='molecule_names.txt',
                    help='File containing the molecule names')

param_text = \
'Precision   double\n\
K           4\n\
Nk          9\n\
K_fine      37\n\
thresold    0.5\n\
BSZ         128\n\
restart     100\n\
tolerance   1e-6\n\
max_iter    1000\n\
P           8\n\
eps         1e-12\n\
NCRIT       100\n\
theta       0.5\n\
GPU         1\n\
polar_eps   1e-2'

config_text = \
'FILE    surf_d16_p0.1    dielectric_interface\n\
--------------------------------\n\
PARAM   LorY E?   Dielec  kappa   charges?    coulomb?  charge_file     Nparent parent  Nchild  children\n\
FIELD   1    0      78.3    1e-12   0           0       NA              0       NA      1       0\n\
FIELD   1    1      1       1e-12   1           1       MOLECULE         1       0       0       NA'

for line in file(parser.parse_args().names_file):

    mol = line[:-1]
    file_param = open(mol+'/'+mol+'.param','w')
    file_param.write(param_text)
    file_param.close()

    config_text_mod = config_text.replace('MOLECULE', mol)
    file_config = open(mol+'/'+mol+'.config','w')
    file_config.write(config_text_mod)
    file_config.close()
