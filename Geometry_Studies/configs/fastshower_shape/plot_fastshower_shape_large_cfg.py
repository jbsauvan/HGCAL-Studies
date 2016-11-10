from copy import copy
from parameters import PlotParameters, HistogramConfig

range_x = [0.9,2.0]
histo_cfg1 = HistogramConfig()
histo_cfg1.color = '#e74c3c'
histo_cfg1.range = range_x
histo_cfg2 = HistogramConfig()
histo_cfg2.color = '#34495e'
histo_cfg2.range = range_x
histo_cfg3 = HistogramConfig()
histo_cfg3.color = '#9b59b6'
histo_cfg3.range = range_x


parameters = PlotParameters()
parameters.input_file = './output/output_largecells.root'
# hexagon distributions
parameters.distribution_plots['variance_large_hexagons_x'] = []
parameters.distribution_plots['variance_large_hexagons_x'].append(copy(histo_cfg1))
parameters.distribution_plots['variance_large_hexagons_x'][-1].name = 'var_x_hexagons_large_center'
parameters.distribution_plots['variance_large_hexagons_x'][-1].legend = 'Hexagons, center'
parameters.distribution_plots['variance_large_hexagons_x'].append(copy(histo_cfg2))
parameters.distribution_plots['variance_large_hexagons_x'][-1].name = 'var_x_hexagons_large_edge'
parameters.distribution_plots['variance_large_hexagons_x'][-1].legend = 'Hexagons, edge'
parameters.distribution_plots['variance_large_hexagons_x'].append(copy(histo_cfg3))
parameters.distribution_plots['variance_large_hexagons_x'][-1].name = 'var_x_hexagons_large_vertex'
parameters.distribution_plots['variance_large_hexagons_x'][-1].legend = 'Hexagons, vertex'
parameters.distribution_plots['covariance_large_hexagons_xy'] = []
parameters.distribution_plots['covariance_large_hexagons_xy'].append(copy(histo_cfg1))
parameters.distribution_plots['covariance_large_hexagons_xy'][-1].name = 'covar_xy_hexagons_large_center'
parameters.distribution_plots['covariance_large_hexagons_xy'][-1].legend = 'Hexagons, center'
parameters.distribution_plots['covariance_large_hexagons_xy'].append(copy(histo_cfg2))
parameters.distribution_plots['covariance_large_hexagons_xy'][-1].name = 'covar_xy_hexagons_large_edge'
parameters.distribution_plots['covariance_large_hexagons_xy'][-1].legend = 'Hexagons, edge'
parameters.distribution_plots['covariance_large_hexagons_xy'].append(copy(histo_cfg3))
parameters.distribution_plots['covariance_large_hexagons_xy'][-1].name = 'covar_xy_hexagons_large_vertex'
parameters.distribution_plots['covariance_large_hexagons_xy'][-1].legend = 'Hexagons, vertex'
for par in parameters.distribution_plots['covariance_large_hexagons_xy']:
  par.range = [-0.25,0.35]
# triangle distributions
parameters.distribution_plots['variance_large_triangles_x'] = []
parameters.distribution_plots['variance_large_triangles_x'].append(copy(histo_cfg1))
parameters.distribution_plots['variance_large_triangles_x'][-1].name = 'var_x_triangles_large_center'
parameters.distribution_plots['variance_large_triangles_x'][-1].legend = 'Triangles, center'
parameters.distribution_plots['variance_large_triangles_x'].append(copy(histo_cfg2))
parameters.distribution_plots['variance_large_triangles_x'][-1].name = 'var_x_triangles_large_edge'
parameters.distribution_plots['variance_large_triangles_x'][-1].legend = 'Triangles, edge'
parameters.distribution_plots['variance_large_triangles_x'].append(copy(histo_cfg3))
parameters.distribution_plots['variance_large_triangles_x'][-1].name = 'var_x_triangles_large_vertex'
parameters.distribution_plots['variance_large_triangles_x'][-1].legend = 'Triangles, vertex'
# comparison plots
parameters.comparison_plots['mean_large_variance'] = HistogramConfig()
parameters.comparison_plots['mean_large_variance'].name = 'mean values'
parameters.comparison_plots['mean_large_variance'].color = '#34495e'
parameters.comparison_plots['rms_large_variance'] = HistogramConfig()
parameters.comparison_plots['rms_large_variance'].name = 'rms values'
parameters.comparison_plots['rms_large_variance'].color = '#34495e'
parameters.comparison_plots['mean_large_covariance'] = HistogramConfig()
parameters.comparison_plots['mean_large_covariance'].name = 'covariance mean values'
parameters.comparison_plots['mean_large_covariance'].color = '#34495e'
parameters.comparison_plots['rms_large_covariance'] = HistogramConfig()
parameters.comparison_plots['rms_large_covariance'].name = 'covariance rms values'
parameters.comparison_plots['rms_large_covariance'].color = '#34495e'
