################################################################################
#
#	IMPORT LIBRARIES
#
################################################################################


import numpy as np
from astropy.table import Table
from MartiniCount import count


################################################################################
#
#	DEFINE FUNCTION
#
################################################################################


def totalCount_Martini(fileName, extra_cols):
	'''Filter through database to determine if all line fluxes are present for 
	various Martini metallicity calculation methods.
		- fileName is the name of file with flux data
		- extra_cols is the list of additional columns of data (not including the index)
	'''
	
	############################################################################
	#	IMPORT DATA
	############################################################################
	# Set up table with line fluxes 3727,H_beta(4863),4959,5007,H_alpha(6565),6583
	# and line errors 3727,H_beta,4959,5007,H_alpha,6583
	
	
	galaxy_data = Table.read(fileName, format='ascii.commented_header')
	
	# Number of galaxies
	N_gal = len(galaxy_data)
	
	
	############################################################################
	#	OUTPUT TABLES
	############################################################################
	
	
	# Output tables
	N2_table = Table()
	N2O2_table = Table()
	O3N2_table = Table()
	
	# Output index lists
	N2_indices = []
	N2O2_indices = []
	O3N2_indices = []
	
	# Output index list reference dictionary
	index_refs = {'N2':N2_indices, 'N2O2':N2O2_indices, 'O3N2':O3N2_indices}
	
	# Initialize count dictionary
	C = {'N2':0, 'N2O2':0, 'O3N2':0}
	
	# Initialize total table
	tot_names = ['index', 'N2', 'N2O2', 'O3N2']
	tot = Table(names=tot_names, dtype=[np.int32]*len(tot_names))
	
	# Initialize line S/N ratio table
	StoN_rat_names = ['index', 'OII_3727', 'H_BETA', 'OIII_5007', 'H_ALPHA', 'NII_6584', 'flux_lt_0']
	StoN_rat = Table(names=StoN_rat_names, dtype=[np.int32]*len(StoN_rat_names))
	
	# Initialize method matrix
	method = [['', 'N2', 'N2O2', 'O3N2'],
			  ['N2', 0, 0, 0],
			  ['N2O2', 0, 0, 0],
			  ['O3N2', 0, 0, 0]]
			  
	# Initialize H_alpha flag total
	Ha = 0
	
	# Initialize S/N ratio flag total dictionary
	SN = {}
	for name in StoN_rat_names[1:]:
		SN[name] = 0
		
	
	############################################################################
	#	FILTER GALAXIES
	############################################################################
	
	
	for i_galaxy in range(N_gal):
	
		########################################################################
		#	DETERMINE VALID METHOD(S)
		########################################################################
		
		# Determine to which method(s) this galaxy can be applied
		c, StoN = count(galaxy_data[i_galaxy])
		
		########################################################################
		#	RECORD RESULTS
		########################################################################
		
		# Update total number of galaxies excluded due to negative fluxes of emission lines
		for line in SN.keys():
			SN[line] = SN[line] + StoN[line]
			
		
		# Build total matrix
		tot.add_row(c)
		
		# Build line S/N ratio matrix
		StoN_rat.add_row(StoN)
		
		
		# Just save off the index value of the galaxy for whichever method(s) it 
		# can be used for, so that we can build the tables at the end all at once.
		
		for method in c.keys()[1:]:
			if c[method]:
				# method can be used
				index_refs[method].append(i_galaxy)
			
				# Increment count
				C[method] = C[method] + 1
	
	
	############################################################################
	#	BUILD OUTPUT TABLES
	############################################################################
	
	
	# Suffixes needed
	suffixes = ['_FLUX', '_FLUX_ERR']
	
	
	################################	N2		################################
	
	# Lines needed
	N2_lines = ['H_ALPHA', 'NII_6584']
	
	N2_table['index'] = galaxy_data['index'][N2_indices]
	
	for column in extra_cols:
		N2_table[column] = galaxy_data[column][N2_indices]
		
	for line in N2_lines:
		for ending in suffixes:
			N2_table[line + ending] = galaxy_data[line + ending][N2_indices]
			
	
	################################	N2O2	################################
	
	# Lines needed
	N2O2_lines = ['OII_3727', 'NII_6584']
	
	N2O2_table['index'] = galaxy_data['index'][N2O2_indices]
	
	for column in extra_cols:
		N2O2_table[column] = galaxy_data[column][N2O2_indices]
		
	for line in N2O2_lines:
		for ending in suffixes:
			N2O2_table[line + ending] = galaxy_data[line + ending][N2O2_indices]
			
			
	################################	O3N2	################################
	
	# Lines needed
	O3N2_lines = ['OIII_5007', 'H_BETA', 'H_ALPHA', 'NII_6584']
	
	O3N2_table['index'] = galaxy_data['index'][O3N2_indices]
	
	for column in extra_cols:
		O3N2_table[column] = galaxy_data[column][O3N2_indices]
		
	for line in O3N2_lines:
		for ending in suffixes:
			O3N2_table[line + ending] = galaxy_data[line + ending][O3N2_indices]
			
			
	############################################################################
	#
	#	WRITE OUTPUT FILES
	#
	############################################################################
	
	
	N2_table.write('N2.txt', format='ascii.commented_header')
	N2O2_table.write('N2O2.txt', format='ascii.commented_header')
	O3N2_table.write('O3N2.txt', format='ascii.commented_header')
	
	
	############################################################################
	#
	#	PRINT OUTPUTS TO TERMINAL
	#
	############################################################################
	
	
	# Print total count
	print 'N2:', C['N2']
	print 'N2O2:', C['N2O2']
	print 'O3N2:', C['O3N2']
	
	# Print number of galaxies eliminated due to flux of [OII] 3727
	print 'Flux of [OII] 3727 < 0:', SN['OII_3727']
	
	# Print number of galaxies eliminated due to flux of H_beta
	print 'Flux of H_beta < 0:', SN['H_BETA']
	
	# Print number of galaxies eliminated due to flux of [OIII] 4959
	print 'Flux of [OIII] 4959 < 0:', SN['OIII_4959']
	
	# Print number of galaxies eliminated due to flux of [OIII] 5007
	print 'Flux of [OIII] 5007 < 0:', SN['OIII_5007']
	
	# Print number of galaxies eliminated due to flux of H_alpha
	print 'Flux of H_alpha < 0:', SN['H_ALPHA']
	
	# Print number of galaxies eliminated due to flux of [NII] 6584
	print 'Flux of [NII] 6584 < 0:', SN['NII_6584']
	
	
	'''
	# Print total matrix to file
	tot_fileName = 
	tot.write(tot_fileName, format='ascii.commented_header')
	
	# Print line S/N ratio matrix to file
	StoN_rat_fileName = 
	StoN_rat.write(StoN_rat_fileName, format='ascii.commented_header')
	'''