'''Various error calculations for metallicity methods empirically derived by 
Brown et al. (2016).'''


################################################################################
#
#	IMPORT MODULES
#
################################################################################

import numpy as np
import math


################################################################################
################################################################################


################################	 N2 	####################################

def N2_error(galaxy):
	'''Analytic error of the N2 ratio metallicity calculation empirically 
	derived by Brown et al. (2016).'''
	
	# [NII] 6584
	partial_6584 = 0.58*np.log10(math.e)/galaxy['NII_6584_FLUX']
	N2_6584 = partial_6584*galaxy['NII_6584_FLUX_ERR']
	
	# H alpha
	partial_Halpha = -0.58*np.log10(math.e)/galaxy['H_ALPHA_FLUX']
	Halpha = partial_Halpha*galaxy['H_ALPHA_FLUX_ERR']
	
	# sSFR
	#partial_sSFR = -0.19*np.log10(math.e)/galaxy['sSFR']
	#sSFR = partial_sSFR*galaxy['sSFR_err']
	sSFR = 0.
	
	# sSFR avg
	#partial_sSFRavg = 0.19
	#sSFR_avg = partial_sSFRavg*galaxy['sSFR_avg_err']
	sSFR_avg = 0.
	
	
	# Error
	N2_err = np.sqrt(N2_6584**2 + Halpha**2 + sSFR**2 + sSFR_avg**2)
	
	return N2_err
	

################################	N2O2	####################################

def N2O2_error(galaxy):
	'''Analytic error of the N2O2 ratio metallicity calculation empirically 
	derived by Brown et al. (2016).'''

	# [NII] 6584
	partial_6584 = 0.54*np.log10(math.e)/galaxy['NII_6584_FLUX']
	N2_6584 = partial_6584*galaxy['NII_6584_FLUX_ERR']
	
	# [OII] 3727
	partial_3727 = -0.54*np.log10(math.e)/galaxy['OII_3727_FLUX']
	O2_3727 = partial_3727*galaxy['OII_3727_FLUX_ERR']
	
	# sSFR
	#partial_sSFR = -0.36*np.log10(math.e)/galaxy['sSFR']
	#sSFR = partial_sSFR*galaxy['sSFR_err']
	sSFR = 0.
	
	# sSFR avg
	#partial_sSFRavg = 0.36
	#sSFR_avg = partial_sSFRavg*galaxy['sSFR_avg_err']
	sSFR_avg = 0.
	
	
	# Error
	N2O2_err = np.sqrt(N2_6584**2 + O2_3727**2 + sSFR**2 + sSFR_avg**2)
	
	return N2O2_err


################################	O3N2	####################################

def O3N2_error(galaxy):
	'''Analytic error of the O3N2 ratio metallicity calculation empirically 
	derived by Brown et al. (2016).'''
	
	# [OIII] 5007
	partial_5007 = -0.32*np.log10(math.e)/galaxy['OIII_5007_FLUX']
	O3_5007 = partial_5007*galaxy['OIII_5007_FLUX_ERR']
	
	# [NII] 6584
	partial_6584 = 0.32*np.log10(math.e)/galaxy['NII_6584_FLUX']
	N2_6584 = partial_6584*galaxy['NII_6584_FLUX_ERR']
	
	# sSFR
	#partial_sSFR = -0.18*np.log10(math.e)/galaxy['sSFR']
	#sSFR = partial_sSFR*galaxy['sSFR_err']
	sSFR = 0.
	
	# sSFR avg
	#partial_sSFRavg = 0.18
	#sSFR_avg = partial_sSFRavg*galaxy['sSFR_avg_err']
	sSFR_avg = 0.
	
	
	# Error
	O3N2_err = np.sqrt(O3_5007**2 + N2_6584**2 + sSFR**2 + sSFR_avg**2)
	
	return O3N2_err