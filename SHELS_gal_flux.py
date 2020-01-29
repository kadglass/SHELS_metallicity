'''Loads galaxy .fits file, coverts flux data to table'''


################################################################################
#
#								LOAD LIBRARIES
#
################################################################################


from os.path import isfile
from astropy.io import fits
from astropy.table import Table
import numpy as np


################################################################################
#
#								DEFINE FUNCTION
#
################################################################################


def get_gal_flux(rabsmag, bin_value, bin_width, bin_range, vorw):
	'''rabsmag is a list of two values, the minimum and maximum M_r for the bin.
	bin_value is a string of the data value binned by.
	bin_width is an integer, the width of the bin.
	bin_range is a list of two values, the minimum and maximum of the bin value.
	vorw is a string of either 'void' or 'wall' '''
	

	############################################################################
	#								IMPORT FILE
	############################################################################


	# Build file name
	fileName = "SHELS/Data/stack_data/SHELSgalaxies_{:d}{:d}_{:s}_{:.1f}_{:.1f}-{:.1f}_{:s}.fits".format(rabsmag[0], rabsmag[1], bin_value, bin_width, bin_range[0], bin_range[1], vorw)
	
	if not isfile(fileName):
		return None
		
	############################################################################
	# Only continue if data for galaxy exists

	# SDSS DR12 pipeline data
	F = fits.open(fileName)
	Fdata = F[1].data
	
	
	############################################################################
	#							CONVERT DATA TO TABLE
	############################################################################
	'''The [OII] 3727,3729 doublet is unresolved, so [OII] 3729 flux, ew are 
	equal to 0.'''


	# Initialize table
	SD = Table()
	
	# Add column of measured emission lines
	SD['LINENAME'] = ['OII_3727', 'OII_3729', 'H_GAMMA', 'OIII_4363', 'H_BETA', 'OIII_4959', 'OIII_5007', 'NII_6548', 'H_ALPHA', 'NII_6584', 'SII_6717', 'SII_6731']
	
	# Add flux to table
	SD['FLUX'] = Fdata['FLUX'][0]
	
	# Add flux errors to table
	SD['FLUX_ERR'] = Fdata['FLUX_ERR'][0]
	
		
	############################################################################
	############################################################################
	
		
	return SD
