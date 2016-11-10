

class Parameters:
  def __init__(self):
    self.input_files = []
    self.input_tree = 'tree'
    self.log_weights = False
    self.output_file = 'output.root'



class HistogramConfig:
  def __init__(self):
    self.name = ''
    self.legend = ''
    self.color = ''
    self.marker = 20
    self.range = []

class PlotParameters:
  def __init__(self):
    self.input_file = ''
    self.distribution_plots = {}
    self.comparison_plots = {}
