'''Main script to calculate metallicity of galaxies.'''


################################################################################
#
#	IMPORT LIBRARIES
#
################################################################################


from totalCount_Martini import totalCount_Martini
from Delta_sSFR import DsSFR
from metMartini import metMartini
from time import time


################################################################################
#
#	INPUTS FROM USER
#
################################################################################


# Metallicity method to use
method = str(input('Which metallicity method? (N2, N2O2, O3N2): '))


start_time = time()
# File name of data
#fileName = input('File name of data (with extension): ')
fileName = '../../Data/kias1033_5_Martini_MPAJHU_flux_oii.txt'


# List of columns of additional data (does not include index)
extra_cols = ['Mstar', 'sSFR', 'rabsmag', 'BPTclass', 'vflag', 'MPA_index']


################################################################################
#
#	CREATE OUTPUT FILE NAME
#
################################################################################


# Filter fileName for outFile
if fileName[0] == '.':
	for i in range(len(fileName)-1,0,-1):
		if fileName[i] == '/':
			break
	
	outFileName = fileName[i+1:]


# Build output file name
outFile = 'comp_Z_Martini_' + method + '_' + outFileName


################################################################################
#
#	FILTER GALAXIES
#
################################################################################
print 'Filtering galaxies'

'''
# Filter out galaxies that have negative fluxes
totalCount_Martini(fileName, extra_cols)
'''

t = time()
print 'Filtering time:', t - start_time
################################################################################
#
#	CALCULATE METALLICITIES
#
################################################################################
print 'Calculating metallicities'


# Calculate D_sSFR
DsSFR(method)

# Calculate metallicities of remaining galaxies
metMartini(method, outFile, extra_cols)


print 'Calculation time:', time() - t
print 'Total runtime:', time() - start_time