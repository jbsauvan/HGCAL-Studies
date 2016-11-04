import numpy as np
from rootpy.io import root_open
from rootpy.plotting import Hist




def main(input_file_name, tree_name):
  moliere = 2.3
  moment_2nd_x = Hist(100, 0., moliere*2., name='var_x')
  moment_2nd_y = Hist(100, 0., moliere*2., name='var_y')
  moment_2nd_xy = Hist(200, -1., 1., name='covar_xy')
  with root_open(input_file_name) as input_file:
    tree = input_file.Get(tree_name)
    for event in tree:
      cells = np.array([[energy for energy in event.cell_energy],
                        [x for x in event.cell_x],
                        [y for y in event.cell_y]], dtype=np.float32).transpose()

      xs = cells[:,[1]].ravel()
      ys = cells[:,[2]].ravel()
      xys = cells[:,[1,2]]
      weights = cells[:,[0]].ravel() # log energy weights
      covar_xy = np.cov(xys, rowvar=False, aweights=weights)
      moment_2nd_x.Fill(covar_xy[0,0])
      moment_2nd_y.Fill(covar_xy[1,1])
      moment_2nd_xy.Fill(covar_xy[0,1])
  with root_open('test.root', 'recreate') as output_file:
    moment_2nd_x.Write()   
    moment_2nd_y.Write()
    moment_2nd_xy.Write()



if __name__=='__main__':
  import optparse
  usage = 'usage: python %prog [options]'
  parser = optparse.OptionParser(usage)
  parser.add_option('--inputfile', dest='input_file_name', help='Input file', default='tree.root')
  parser.add_option('--tree', dest='tree_name', help='Tree in the input file', default='tree')
  (opt, args) = parser.parse_args()
  main(input_file_name=opt.input_file_name, tree_name=opt.tree_name)
