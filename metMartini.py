'''Import data file, run metallicity calculations on all galaxies included, and 
create text file of metallicity values.'''

################################################################################
#
#	IMPORT LIBRARIES
#
################################################################################


from metal_methods import N2,N2O2,O3N2
from metal_errors import N2_error,N2O2_error,O3N2_error
from astropy.table import Table
import numpy as np


################################################################################
#
#	DEFINE FUNCTION
#
################################################################################


def metMartini(method, outFile, extra_cols):
	'''method is the metallicity method to be used
	outFile is the name of the output file for the calculated metallicity values
	extra_cols is the number of columns of additional data in the original file 
	(before the beginning of the flux data)'''
	
	############################################################################
	#
	#	INITIALIZATIONS
	#
	############################################################################
	
	# Dictionary to relate method to function name
	method_options = {'N2':[N2, N2_error], 'N2O2':[N2O2, N2O2_error], 'O3N2':[O3N2, O3N2_error]}
	
	# Output table
	out_table = Table()
	
	# Output lists
	Z_list = []
	Zerror_list = []
	
	
	############################################################################
	#
	#	INPUTS
	#
	############################################################################
	
	fileName = method + '.txt'
	method_calc = method_options[method][0]
	method_error = method_options[method][1]
	
	
	############################################################################
	#
	#	IMPORT DATA
	#
	############################################################################
	
	galaxy_data = Table.read(fileName, format='ascii.commented_header')
	
	
	############################################################################
	#
	#	ADD INITIAL COLUMNS TO OUTPUT TABLE
	#
	############################################################################
	
	out_table['index'] = galaxy_data['index']
	
	for column in extra_cols:
		out_table[column] = galaxy_data[column]
	
	
	############################################################################
	#
	#	CALCULATE METALLICITY
	#
	############################################################################
	
	# Calculate metallicity for each galaxy
	for i_galaxy in range(len(galaxy_data)):
		
		if i_galaxy%1000 == 0:
			print 'Calculating galaxy #:', i_galaxy
		
		########################################################################
		#	CALCULATE ABUNDANCES
		########################################################################
		
		# Calculate metallicity
		Z = method_calc(galaxy_data[i_galaxy])
		
		# Calculate abundance errors
		Zerror = method_error(galaxy_data[i_galaxy])
		
		########################################################################
		#	SAVE RESULTS TO LISTS
		########################################################################
		
		Z_list.append(Z)
		Zerror_list.append(Zerror)
		
		
	############################################################################
	#
	#	BUILD OUTPUT TABLE
	#
	############################################################################
	
	out_table['Z12logOH'] = Z_list
	out_table['Zerr'] = Zerror_list
	
	
	############################################################################
	#
	#	SAVE OUTPUT TABLE
	#
	############################################################################
	
	out_table.write(outFile, format='ascii.commented_header')