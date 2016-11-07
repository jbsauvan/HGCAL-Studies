import numpy as np
import math as m
from rootpy.io import root_open
from rootpy.plotting import Hist
from root_numpy import fill_hist


def moments(event):
  cells = np.array([[energy for energy in event.cell_energy],
                    [x for x in event.cell_x],
                    [y for y in event.cell_y],
                    [x/2.+y*m.sqrt(3.)/2. for x,y in zip(event.cell_x, event.cell_y)], # u rotated by 60deg / x
                    [y/2.-x*m.sqrt(3.)/2. for x,y in zip(event.cell_x, event.cell_y)], # v rotated by 60deg / x
                   ], dtype=np.float32).transpose()

  xys = cells[:,1:]
  weights = cells[:,[0]].ravel() # log energy weights
  # variances followed by covariances
  # xx, yy, uu, vv, xy, xu, xv, yu, yv, uv
  covar_xy = np.cov(xys, rowvar=False, aweights=weights).ravel()[[0,5,10,15,1,2,3,6,7,11]]
  return covar_xy

def shape_distribution(tree):
  moliere = 2.3
  moment_2nd_x = Hist(100, 0., moliere*2., name='var_x')
  moment_2nd_y = Hist(100, 0., moliere*2., name='var_y')
  moment_2nd_xy = Hist(200, -1., 1., name='covar_xy')
  moment_2nd_u = Hist(100, 0., moliere*2., name='var_u')
  moment_2nd_v = Hist(100, 0., moliere*2., name='var_v')
  moment_2nd_uv = Hist(200, -1., 1., name='covar_uv')
  moment_2nd_x.SetXTitle('Var(x) [cm^{2}]')
  moment_2nd_y.SetXTitle('Var(y) [cm^{2}]')
  moment_2nd_u.SetXTitle('Var(u) [cm^{2}]')
  moment_2nd_v.SetXTitle('Var(v) [cm^{2}]')
  moment_2nd_xy.SetXTitle('Covar(x,y) [cm^{2}]')
  moment_2nd_uv.SetXTitle('Covar(u,v) [cm^{2}]')
  covars = np.array([moments(event) for event in tree], np.float32) 
  var_x = covars[:,[0]].ravel()
  var_y = covars[:,[1]].ravel()
  covar_xy = covars[:,[4]].ravel()
  var_u = covars[:,[2]].ravel()
  var_v = covars[:,[3]].ravel()
  covar_uv = covars[:,[9]].ravel()
  fill_hist(moment_2nd_x, var_x)
  fill_hist(moment_2nd_y, var_y)
  fill_hist(moment_2nd_xy, covar_xy)
  fill_hist(moment_2nd_u, var_u)
  fill_hist(moment_2nd_v, var_v)
  fill_hist(moment_2nd_uv, covar_uv)
  return moment_2nd_x, moment_2nd_y, moment_2nd_xy,moment_2nd_u, moment_2nd_v,moment_2nd_uv



def main(parameters):
  input_files = parameters.input_files
  tree_name = parameters.input_tree
  means = Hist(4*len(input_files), 0, 4*len(input_files), name='mean values')
  rmss = Hist(4*len(input_files), 0, 4*len(input_files), name='rms values')
  cov_means = Hist(2*len(input_files), 0, 2*len(input_files), name='covariance mean values')
  cov_rmss = Hist(2*len(input_files), 0, 2*len(input_files), name='covariance rms values')
  means.SetYTitle('Variance mean [cm^{2}]')
  rmss.SetYTitle('Variance RMS [cm^{2}]')
  cov_means.SetYTitle('Covariance mean [cm^{2}]')
  cov_rmss.SetYTitle('Covariance RMS [cm^{2}]')
  with root_open(parameters.output_file, 'recreate') as output_file:
    for i, (name, input_file_name) in enumerate(input_files):
      means.GetXaxis().SetBinLabel(i*4+1, name+' x')
      means.GetXaxis().SetBinLabel(i*4+2, name+' y')
      means.GetXaxis().SetBinLabel(i*4+3, name+' u')
      means.GetXaxis().SetBinLabel(i*4+4, name+' v')
      rmss.GetXaxis().SetBinLabel(i*4+1, name+' x')
      rmss.GetXaxis().SetBinLabel(i*4+2, name+' y')
      rmss.GetXaxis().SetBinLabel(i*4+3, name+' u')
      rmss.GetXaxis().SetBinLabel(i*4+4, name+' v')
      cov_means.GetXaxis().SetBinLabel(i*2+1, name+' x/y')
      cov_rmss.GetXaxis().SetBinLabel(i*2+1, name+' x/y')
      cov_means.GetXaxis().SetBinLabel(i*2+2, name+' u/v')
      cov_rmss.GetXaxis().SetBinLabel(i*2+2, name+' u/v')
      with root_open(input_file_name) as input_file:
        tree = input_file.Get(tree_name)
        moment_2nd_x, moment_2nd_y, moment_2nd_xy, moment_2nd_u, moment_2nd_v, moment_2nd_uv = shape_distribution(tree)
        print name
        print 'x variance Mu =', moment_2nd_x.GetMean(), '+/-', moment_2nd_x.GetMeanError(), 'RMS =', moment_2nd_x.GetRMS(), '+/-', moment_2nd_x.GetRMSError()
        print 'y variance Mu =', moment_2nd_y.GetMean(), '+/-', moment_2nd_y.GetMeanError(), 'RMS =', moment_2nd_y.GetRMS(), '+/-', moment_2nd_y.GetRMSError()
        print 'u variance Mu =', moment_2nd_u.GetMean(), '+/-', moment_2nd_u.GetMeanError(), 'RMS =', moment_2nd_u.GetRMS(), '+/-', moment_2nd_u.GetRMSError()
        print 'v variance Mu =', moment_2nd_v.GetMean(), '+/-', moment_2nd_v.GetMeanError(), 'RMS =', moment_2nd_v.GetRMS(), '+/-', moment_2nd_v.GetRMSError()
        print 'x-y covariance Mu =', moment_2nd_xy.GetMean(), '+/-', moment_2nd_xy.GetMeanError(), 'RMS =', moment_2nd_xy.GetRMS(), '+/-', moment_2nd_xy.GetRMSError()
        print 'u-v covariance Mu =', moment_2nd_uv.GetMean(), '+/-', moment_2nd_uv.GetMeanError(), 'RMS =', moment_2nd_uv.GetRMS(), '+/-', moment_2nd_uv.GetRMSError()
        # fill mean values of variances
        means.SetBinContent(i*4+1, moment_2nd_x.GetMean())
        means.SetBinError(i*4+1, moment_2nd_x.GetMeanError())
        means.SetBinContent(i*4+2, moment_2nd_y.GetMean())
        means.SetBinError(i*4+2, moment_2nd_y.GetMeanError())
        means.SetBinContent(i*4+3, moment_2nd_u.GetMean())
        means.SetBinError(i*4+3, moment_2nd_u.GetMeanError())
        means.SetBinContent(i*4+4, moment_2nd_v.GetMean())
        means.SetBinError(i*4+4, moment_2nd_v.GetMeanError())
        # fill rms values of variances
        rmss.SetBinContent(i*4+1, moment_2nd_x.GetRMS())
        rmss.SetBinError(i*4+1, moment_2nd_x.GetRMSError())
        rmss.SetBinContent(i*4+2, moment_2nd_y.GetRMS())
        rmss.SetBinError(i*4+2, moment_2nd_y.GetRMSError())
        rmss.SetBinContent(i*4+3, moment_2nd_u.GetRMS())
        rmss.SetBinError(i*4+3, moment_2nd_u.GetRMSError())
        rmss.SetBinContent(i*4+4, moment_2nd_v.GetRMS())
        rmss.SetBinError(i*4+4, moment_2nd_v.GetRMSError())
        # fill mean values of covariances
        cov_means.SetBinContent(i*2+1, moment_2nd_xy.GetMean())
        cov_means.SetBinError(i*2+1, moment_2nd_xy.GetMeanError())
        cov_means.SetBinContent(i*2+2, moment_2nd_uv.GetMean())
        cov_means.SetBinError(i*2+2, moment_2nd_uv.GetMeanError())
        # fill rms values of covariances
        cov_rmss.SetBinContent(i*2+1, moment_2nd_xy.GetRMS())
        cov_rmss.SetBinError(i*2+1, moment_2nd_xy.GetRMSError())
        cov_rmss.SetBinContent(i*2+2, moment_2nd_uv.GetRMS())
        cov_rmss.SetBinError(i*2+2, moment_2nd_uv.GetRMSError())
        # write variance distributions
        moment_2nd_x.SetName(moment_2nd_x.GetName()+'_'+name)
        moment_2nd_y.SetName(moment_2nd_y.GetName()+'_'+name)
        moment_2nd_xy.SetName(moment_2nd_xy.GetName()+'_'+name)
        moment_2nd_u.SetName(moment_2nd_u.GetName()+'_'+name)
        moment_2nd_v.SetName(moment_2nd_v.GetName()+'_'+name)
        output_file.cd()
        moment_2nd_x.Write()   
        moment_2nd_y.Write()
        moment_2nd_xy.Write()
        moment_2nd_u.Write()
        moment_2nd_v.Write()
    means.Write()
    rmss.Write()
    cov_means.Write()
    cov_rmss.Write()




if __name__=='__main__':
  import optparse
  import importlib
  import os
  import sys
  usage = 'usage: python %prog [options]'
  parser = optparse.OptionParser(usage)
  parser.add_option('--cfg', dest='parameter_file', help='Python file containing the definition of parameters ', default='pars.py')
  (opt, args) = parser.parse_args()
  current_dir = os.getcwd();
  sys.path.append(current_dir)
  # Remove the extension of the python file before module loading
  if opt.parameter_file[-3:]=='.py': opt.parameter_file = opt.parameter_file[:-3]
  parameters = importlib.import_module(opt.parameter_file).parameters
  main(parameters)

