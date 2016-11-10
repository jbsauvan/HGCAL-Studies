from rootpy.io import root_open
from rootpy.plotting import Canvas, Legend
from rootpy.plotting.style import get_style, set_style
from rootpy.plotting.utils import get_limits

def plot_distributions(input_file, distribution_plots):
  with root_open(input_file) as file:
    for name,histo_configs in distribution_plots.items():
      canvas = Canvas(700,700)
      legend = Legend(len(histo_configs), leftmargin=0.4, margin=0.3)
      histograms = []
      for histo_config in histo_configs:
        histogram = file.Get(histo_config.name)
        if len(histo_config.range)==2:
          histogram.SetAxisRange(histo_config.range[0], histo_config.range[1], 'X')
        histogram.color = histo_config.color
        histogram.markerstyle = histo_config.marker
        legend.AddEntry(histogram, label=histo_config.legend, style='ep')
        histograms.append(histogram)
      xmin, xmax, ymin, ymax = get_limits(histograms, logy=False)
      option = ''
      for histogram in histograms:
        histogram.SetAxisRange(ymin,ymax,'Y')
        histogram.Draw(option)
        option += ' same'
      legend.Draw()
      canvas.Print('plots/{}.png'.format(name))

def plot_comparisons(input_file, comparison_plots):
  with root_open(input_file) as file:
    for name,histo_config in comparison_plots.items():
      canvas = Canvas(1200,700)
      canvas.SetLeftMargin(0.08)
      canvas.SetRightMargin(0.12)
      histogram = file.Get(histo_config.name)
      if len(histo_config.range)==2:
        histogram.SetAxisRange(histo_config.range[0], histo_config.range[1], 'X')
      histogram.color = histo_config.color
      histogram.markerstyle = histo_config.marker
      histogram.Draw()
      canvas.Print('./plots/{}.png'.format(name))



def main(parameters):
  style = get_style('CMSTDR')
  style.SetTitleSize(0.07, "XYZ")
  style.SetLegendBorderSize(0)
  style.SetLegendFillColor(0)
  style.SetLegendFont(43)
  style.SetTextSize(25)
  set_style(style)
  input_file = parameters.input_file
  plot_distributions(input_file, parameters.distribution_plots)
  plot_comparisons(input_file, parameters.comparison_plots)


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
  # Add config directory to the python path and load configuration
  config_dir = os.path.dirname(opt.parameter_file)
  config_module = os.path.splitext(os.path.basename(opt.parameter_file))[0]
  sys.path.append(current_dir+'/'+config_dir)
  parameters = importlib.import_module(config_module).parameters
  main(parameters)

