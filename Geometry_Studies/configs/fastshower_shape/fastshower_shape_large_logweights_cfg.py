from glob import glob
from parameters import Parameters
from os.path import splitext, basename

input_dir = '/home/sauvan/Documents/HEP/Projects/CMS/L1CalorimeterTrigger_Phase2HGCal/Misc/FastShower/output/'

parameters = Parameters()
parameters.input_files = sorted([(splitext(basename(f))[0], f) for f in glob(input_dir+'*large*.root')])
parameters.tree = 'tree'
parameters.log_weights = False
parameters.output_file = 'output/output_largecells_logweights.root'
