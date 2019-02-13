'''Filter through database to determine if all line fluxes are present for 
various metallicity calculation methods.

3 methods from Brown et al. (2016):
	N2: [NII]6584, H_a
	N2O2: [OII]3727, [NII]6584
	O3N2: [OIII]5007, [NII]6584
'''


################################################################################
#
#	DEFINE FUNCTION
#
################################################################################


def count(galaxy):
	'''Based on the provided line fluxes, determines which methods can be used 
	to calculate the galaxy's metallicity.
	Conditions: must be emission line
	'''
	
	############################################################################
	#
	#	INITIALIZE OUTPUTS
	#
	############################################################################
	
	
	# Flag dictionary for signal-to-noise of lines: 1 - fail, 0 - pass
	StoN = {'index':galaxy['index'], 'flux_lt_0':0}
	
	# Flag dictionary for methods: 1 - can use, 0 - cannot use
	C = {'index':galaxy['index'], 'N2':1, 'N2O2':1, 'O3N2':1}
	
	
	############################################################################
	#
	#	EVALUATE FLUX QUALITY
	#
	############################################################################
	
	############################################################################
	#	[OII] 3727
	############################################################################
	
	if galaxy['OII_3727_FLUX'] <= 0.:
		# Cannot use N2O2
		C['N2O2'] = 0
		StoN['OII_3727'] = 1
		StoN['flux_lt_0'] = 1
	else:
		StoN['OII_3727'] = 0
		
	
	############################################################################
	#	[OIII] 5007
	############################################################################
	
	if galaxy['OIII_5007_FLUX'] <= 0.:
		# Cannot use O3N2
		C['O3N2'] = 0
		StoN['OIII_5007'] = 1
		StoN['flux_lt_0'] = 1
	else:
		StoN['OIII_5007'] = 0
	
	############################################################################
	#	H_alpha
	############################################################################
	
	if galaxy['H_ALPHA_FLUX'] <= 0.:
		# Cannot use N2
		C['N2'] = 0
		StoN['H_ALPHA'] = 1
		StoN['flux_lt_0'] = 1
	else:
		StoN['H_ALPHA'] = 0
	
	############################################################################
	#	[NII] 6584
	############################################################################
	
	if galaxy['NII_6584_FLUX'] <= 0.:
		# Cannot use N2, N2O2, O3N2
		C['N2'] = 0
		C['N2O2'] = 0
		C['O3N2'] = 0
		StoN['NII_6584'] = 1
		StoN['flux_lt_0'] = 1
	else:
		StoN['NII_6584'] = 0
		
		
	############################################################################
	#
	#	RETURN OUTPUT
	#
	############################################################################
	
	
	return C, StoN