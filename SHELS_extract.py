'''Extract spectroscopic data (line fluxes, errors) from SHELS data (stacked 
spectra from Jabran Zahid).'''


################################################################################
#
#								IMPORT LIBRARIES
#
################################################################################


import numpy as np
from astropy.table import Table
from time import time
from SHELS_gal_flux import *


start_time = time()
################################################################################
#
#									USER IMPUT
#
################################################################################


# Bin widths
bin_width = [0.1, 0.2, 0.3, 0.4, 0.5]

# M_r limits
rabsmag_limits = [0, -17, -18, -19, -20]

# Data value binned
bin_value = 'Mstar'

# Bin min, max
bin_limits = [6.1, 11.0]


method = input('Metallicity method to be used (Nagao, KE, Martini): ')


################################################################################
#
#									COLUMNS
#
################################################################################
'''For each line, there is the line continuum, the line flux, and the error in 
the flux.'''


fields = ['FLUX', 'FLUX_ERR']

if method == 'Nagao':
	# Strong-line methods
	# [OII]3727, H_beta, [OIII]4959, [OIII]5007, H_alpha, [NII]6584, [SII]6717
	lines = ['OII_3727', 'H_BETA', 'OIII_4959', 'OIII_5007', 'H_ALPHA', 'NII_6584', 'SII_6717']
elif method == 'KE':
	# Direct Te method
	# [OII]3726, [OII]3729, [OIII]4363, H_beta, [OIII]4959, [OIII]5007, [NII]6548, H_alpha, [NII]6584, [SII]6717, [SII]6731
	lines = ['OII_3727', 'OIII_4363', 'H_BETA', 'OIII_4959', 'OIII_5007', 'NII_6548', 'H_ALPHA', 'NII_6584', 'SII_6717', 'SII_6731']
elif method == 'Martini':
	# Martini methods (Brown16)
	# [OII]3727, H_beta, [OIII]5007, H_alpha, [NII]6584
	lines = ['OII_3727', 'H_BETA', 'OIII_5007', 'H_ALPHA', 'NII_6584']
else:
	# empirical method not requiring [OII] 3727 or [OIII] 4363
	# H_beta, [OIII]4959, [OIII]5007, [NII]6548, H_alpha, [NII]6584, [SII]6717, [SII]6731
	lines = ['H_BETA', 'OIII_4959', 'OIII_5007', 'NII_6548', 'H_ALPHA', 'NII_6584', 'SII_6717', 'SII_6731']


################################################################################
#
#								LOCATE FLUX DATA
#
################################################################################
'''We are just saving the flux data, along with the galaxies' ID numbers, 
magnitudes, and void status.  We will add the metallicity estimates to the main 
data file after they are computed.'''
t = time()


# Column names in data table
col_names = ['index', 'Mr_min', 'Mr_max', 'vflag', 'bin_size', bin_value+'_min', bin_value+'_max']
col_type = [np.int16, np.int8, np.int8, np.int8, np.float32, np.float32, np.float32]
for line in lines:
	for field in fields:
		col_names.append('_'.join([line,field]))
		col_type.append(np.float32)

# Initialize final data table
data = Table(names=col_names, dtype=col_type)
j = 0 	# row index

for width in bin_width:
	for i_Mr in range(len(rabsmag_limits)-1):
		for bin in np.arange(bin_limits[0], bin_limits[1], width):
			for vflag in ['void', 'wall']:

				# Retrieve flux data
				flux_table = get_gal_flux([rabsmag_limits[i_Mr], rabsmag_limits[i_Mr + 1]], bin_value, width, [bin, bin + width], vflag)
	
				# Check to see if data exists for galaxy
				if flux_table is None:
					continue
		
				################################################################
				# Only continue if data for galaxy was found
	
				data.add_row(np.empty(shape=len(col_type)))

				# Add flux data to final data table
				data['index'][j] = j
				data['Mr_min'][j] = rabsmag_limits[i_Mr]
				data['Mr_max'][j] = rabsmag_limits[i_Mr + 1]
				data['bin_size'][j] = width
				data[bin_value+'_min'][j] = bin
				data[bin_value+'_max'][j] = bin + width
				
				if vflag == 'void':
					data['vflag'][j] = 1
				else:
					data['vflag'][j] = 0
	
				for line in lines:
	
					# Locate row index of line
					row_line = np.where(flux_table['LINENAME'] == line)[0][0]
		
					for field in fields:
						data['_'.join([line,field])][j] = flux_table[field][row_line]
			
				# Increment data table row index
				j = j + 1
		
		
print 'Assigned fluxes to table', time()-t
################################################################################
#
#								SAVE DATA TO FILE
#
################################################################################
t = time()


# Set number of decimal places in columns
data['bin_size'].format = '{:.1f}'
data[bin_value+'_min'].format = '{:.1f}'
data[bin_value+'_max'].format = '{:.1f}'

data.write('SHELS/Data/SHELSgalaxies_' + method + '_flux.txt', format='ascii.commented_header')


print 'Saved data to file', time()-t
print 'Total run time', time()-start_time
