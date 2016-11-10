from glob import glob
from ROOT import TCanvas, TH2Poly, TMarker
from rootpy.io import root_open
from rootpy.plotting import Canvas
from rootpy.plotting import get_style, set_style
from os.path import splitext, basename

def plot_event(name, canvas):
  primitives = canvas.GetListOfPrimitives()
  histo = None
  point = None
  for primitive in primitives:
    if primitive.InheritsFrom(TH2Poly.Class()):
      histo = primitive
    if primitive.InheritsFrom(TMarker.Class()):
      point = primitive
  histo.SetXTitle('x [cm]')
  histo.SetYTitle('y [cm]')
  canvas_new = Canvas(700, 700)
  histo.SetAxisRange(77,100,'X')
  histo.Draw('colz')
  point.Draw()
  canvas_new.SetLogz()
  canvas_new.Print('./plots/event_{}.png'.format(name))

def main():
  style = get_style('CMSTDR')
  style.SetTitleSize(0.07, "XYZ")
  style.SetPalette(54) # kBlueYellow
  style.SetPadLeftMargin(0.10)
  style.SetPadRightMargin(0.12)
  set_style(style)
  input_dir = '/home/sauvan/Documents/HEP/Projects/CMS/L1CalorimeterTrigger_Phase2HGCal/Misc/FastShower/output/'
  files = glob(input_dir+'*.root')
  for file_name in files:
    with root_open(file_name) as file:
      for object in file.objects(cls=TCanvas):
        if 'Event 1' in object.GetName():
          plot_event(splitext(basename(file_name))[0], object)




if __name__=='__main__':
  main()

