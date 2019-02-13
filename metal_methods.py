'''Various metallicity methods empirically derived by Brown et al. (2016)
All methods require sSFR'''


################################################################################
#
#	IMPORT MODULES
#
################################################################################

import numpy as np


################################################################################
################################################################################


################################	 N2		####################################

def N2(galaxy):
	'''Calculate the metallicity of a galaxy based on the N2 ratio as outlined 
	in Brown et al. (2016).'''
	
	N2_ratio = galaxy['NII_6584_FLUX']/galaxy['H_ALPHA_FLUX']
	
	logOH12 = 9.12 + 0.58*np.log10(N2_ratio) - 0.19*galaxy['D_sSFR']
	
	return logOH12


################################	N2O2	####################################

def N2O2(galaxy):
	'''Calculate the metallicity of a galaxy based on the N2O2 ratio as outlined 
	in Brown et al. (2016).'''
	
	N2O2_ratio = galaxy['NII_6584_FLUX']/galaxy['OII_3727_FLUX']
	
	logOH12 = 9.20 + 0.54*np.log10(N2O2_ratio) - 0.36*galaxy['D_sSFR']
	
	return logOH12
	
	
################################	O3N2	####################################

def O3N2(galaxy):
	'''Calculate the metallicity of a galaxy based on the O3N2 ratio as outlined 
	in Brown et al. (2016).'''
	
	O3N2_ratio = galaxy['OIII_5007_FLUX']/galaxy['H_BETA_FLUX']/galaxy['NII_6584_FLUX']/galaxy['H_ALPHA_FLUX']
	
	logOH12 = 8.98 - 0.32*np.log10(O3N2_ratio) - 0.18*galaxy['D_sSFR']
	
	return logOH12