from astropy.table import Table
from numpy import log10

fileName = "SHELSgalaxies_Martini_flux_redshift_SFR_SSFR.txt"

# Martini data with SSFR 
Martini = Table.read(fileName, format = "ascii.commented_header")

H_ALPHA_FLUX = Martini["H_ALPHA_FLUX"]
H_BETA_FLUX = Martini["H_BETA_FLUX"]
# [NII]_6583 ?
NII_6584_FLUX = Martini["NII_6584_FLUX"]
OII_3727_FLUX = Martini["OII_3727_FLUX"]
OIII_5007_FLUX = Martini["OIII_5007_FLUX"]

N2_cal = []
O3N2_cal = []
N2O2_cal = []

for i in range(len(SSFR)):

    SSFR = Martini["SSFR"][i]
    Mstar = Martini["Mstar"][i]

    #log(SSFR)
    log_SSFR = log10( SSFR )

    #log(SSFR)_Mstar
    # M* is already log
    log_SSFR_Mstar = 283.728 - 116.265 * log10( Mstar ) + 17.4403 * ( log10( Mstar ) ) ** 2 - 1.17146 * ( log10 ( Mstar ) ) ** 3 + 0.0296526 * ( log10 ( Mstar ) ) ** 4

    # Delta_log(SSFR)
    delta_log_SSFR = log_SSFR - log_SSFR_Mstar

    ### Calculate Metalicity
    ## result: 12 + log( O/H )_method

    # N2 Method
    N2 = NII_6584_FLUX[i] / H_ALPHA_FLUX[i]
    O_H_N2 = 9.12 + 0.58 * log( N2 ) - 0.19 * delta_log_SSFR
    N2_cal.append(O/H_N2)

    # O3N2 Method
    O3N2 = OIII_5007_FLUX / H_BETA_FLUX / NII_6584_FLUX / H_ALPHA_FLUX
    O_H_O3N2 = 8.98 + 0.32 * log( O3N2 ) - 0.18 * delta_log_SSFR
    O3N2_cal.append(O/H_03N2)

    #N2O2 Method
    N2O2 = NII_6584_FLUX / OII_3727_FLUX
    O_H_N2O2= 9.20 + 0.54 * log( N2O2 ) - 0.36 * delta_log_SSFR
    N2O2_cal.append(O/H_N2O2)

Martini["N2"] = N2_cal
Martini["O3N2"] = O3N2_cal
Martini["N2O3"] = N2O2_cal
Martini.write(fileName[:-4] + "_Metalicity", format = "ascii.commented_header", overwrite = True)
