"""
Zenburn for Matplotlib
-------

This script sets default matplotlib styles so that plots look nice when used
with ipynb-zenburn.css.

"""
#########################
### Color References: ###
#########################

# Gray: #3F3F3F
# Light Gray: #6F6F6F
# White: #FFFFEF
# Red: #CC9393
# Green: #7F9F7F
# Orange: #DFAF8F
# Yellow: #F0DFAF
# Cyan: #93E0E3
# Blue: #8CD0D3
# Dark Red: #A55D5D
# Dark Green: #466F46
# Dark Blue: #4A7274
# Dark Orange: #A352E

##############################
### Commonly used packages ###
##############################

from matplotlib import pyplot as plt
import matplotlib as mpl
from cycler import cycler

##################################
### Change matplotlib defaults ###
##################################

# To restore defaults, run `mpl.rcdefaults()`.
# For nice publisable plots, use `plt.style.use(['classic','ggplot'])`.

mpl.rcParams['text.color'] = 'white'
mpl.rcParams['legend.facecolor'] = '9F9F9F'
mpl.rcParams['legend.fancybox'] = True
mpl.rcParams['axes.grid'] = True
mpl.rcParams['axes.titlesize'] = '18'
mpl.rcParams['figure.figsize'] = [8,6]
mpl.rcParams['lines.color'] = '#3F3F3F'
mpl.rcParams['axes.prop_cycle'] = cycler('color',
                                         ['#A55D5D', '#466F46',
                                          '#4A7274','#3F3F3F',
                                          '#A35E2E',])
mpl.rcParams['patch.facecolor'] = '466F46'
mpl.rcParams['axes.facecolor'] = 'CFCFCF'
mpl.rcParams['axes.labelcolor'] = 'white'
mpl.rcParams['axes.labelsize'] = '14'
mpl.rcParams['xtick.color'] = 'CFCFCF'
mpl.rcParams['ytick.color'] = 'CFCFCF'
mpl.rcParams['legend.loc'] = 'best'
