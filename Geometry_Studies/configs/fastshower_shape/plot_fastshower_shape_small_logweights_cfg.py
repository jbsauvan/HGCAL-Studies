from copy import copy
from parameters import PlotParameters, HistogramConfig

range_x = [1.3,2.6]
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
parameters.input_file = './output/output_smallcells_logweights.root'
# hexagon distributions
parameters.distribution_plots['variance_small_hexagons_logweights_x'] = []
parameters.distribution_plots['variance_small_hexagons_logweights_x'].append(copy(histo_cfg1))
parameters.distribution_plots['variance_small_hexagons_logweights_x'][-1].name = 'var_x_hexagons_small_center'
parameters.distribution_plots['variance_small_hexagons_logweights_x'][-1].legend = 'Hexagons, center'
parameters.distribution_plots['variance_small_hexagons_logweights_x'].append(copy(histo_cfg2))
parameters.distribution_plots['variance_small_hexagons_logweights_x'][-1].name = 'var_x_hexagons_small_edge'
parameters.distribution_plots['variance_small_hexagons_logweights_x'][-1].legend = 'Hexagons, edge'
parameters.distribution_plots['variance_small_hexagons_logweights_x'].append(copy(histo_cfg3))
parameters.distribution_plots['variance_small_hexagons_logweights_x'][-1].name = 'var_x_hexagons_small_vertex'
parameters.distribution_plots['variance_small_hexagons_logweights_x'][-1].legend = 'Hexagons, vertex'
parameters.distribution_plots['covariance_small_hexagons_logweights_xy'] = []
parameters.distribution_plots['covariance_small_hexagons_logweights_xy'].append(copy(histo_cfg1))
parameters.distribution_plots['covariance_small_hexagons_logweights_xy'][-1].name = 'covar_xy_hexagons_small_center'
parameters.distribution_plots['covariance_small_hexagons_logweights_xy'][-1].legend = 'Hexagons, center'
parameters.distribution_plots['covariance_small_hexagons_logweights_xy'].append(copy(histo_cfg2))
parameters.distribution_plots['covariance_small_hexagons_logweights_xy'][-1].name = 'covar_xy_hexagons_small_edge'
parameters.distribution_plots['covariance_small_hexagons_logweights_xy'][-1].legend = 'Hexagons, edge'
parameters.distribution_plots['covariance_small_hexagons_logweights_xy'].append(copy(histo_cfg3))
parameters.distribution_plots['covariance_small_hexagons_logweights_xy'][-1].name = 'covar_xy_hexagons_small_vertex'
parameters.distribution_plots['covariance_small_hexagons_logweights_xy'][-1].legend = 'Hexagons, vertex'
for par in parameters.distribution_plots['covariance_small_hexagons_logweights_xy']:
  par.range = [-0.35,0.45]
# triangle distributions
parameters.distribution_plots['variance_small_triangles_logweights_x'] = []
parameters.distribution_plots['variance_small_triangles_logweights_x'].append(copy(histo_cfg1))
parameters.distribution_plots['variance_small_triangles_logweights_x'][-1].name = 'var_x_triangles_small_center'
parameters.distribution_plots['variance_small_triangles_logweights_x'][-1].legend = 'Triangles, center'
parameters.distribution_plots['variance_small_triangles_logweights_x'].append(copy(histo_cfg2))
parameters.distribution_plots['variance_small_triangles_logweights_x'][-1].name = 'var_x_triangles_small_edge'
parameters.distribution_plots['variance_small_triangles_logweights_x'][-1].legend = 'Triangles, edge'
parameters.distribution_plots['variance_small_triangles_logweights_x'].append(copy(histo_cfg3))
parameters.distribution_plots['variance_small_triangles_logweights_x'][-1].name = 'var_x_triangles_small_vertex'
parameters.distribution_plots['variance_small_triangles_logweights_x'][-1].legend = 'Triangles, vertex'
# comparison plots
parameters.comparison_plots['mean_small_logweights_variance'] = HistogramConfig()
parameters.comparison_plots['mean_small_logweights_variance'].name = 'mean values'
parameters.comparison_plots['mean_small_logweights_variance'].color = '#34495e'
parameters.comparison_plots['rms_small_logweights_variance'] = HistogramConfig()
parameters.comparison_plots['rms_small_logweights_variance'].name = 'rms values'
parameters.comparison_plots['rms_small_logweights_variance'].color = '#34495e'
parameters.comparison_plots['mean_small_logweights_covariance'] = HistogramConfig()
parameters.comparison_plots['mean_small_logweights_covariance'].name = 'covariance mean values'
parameters.comparison_plots['mean_small_logweights_covariance'].color = '#34495e'
parameters.comparison_plots['rms_small_logweights_covariance'] = HistogramConfig()
parameters.comparison_plots['rms_small_logweights_covariance'].name = 'covariance rms values'
parameters.comparison_plots['rms_small_logweights_covariance'].color = '#34495e'
