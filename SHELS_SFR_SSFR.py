from astropy.table import Table
from numpy import log10, pi, mean
from get_gal_info import *

fileName = "SHELSgalaxies_Martini_flux.txt"

Martini = Table.read(fileName, format = "ascii.commented_header")
galaxies = Table.read("SHELSgalaxies_simpleHeader_vflag_rabsmag.txt", format = "ascii.commented_header")

# speed of light (km/s)
c = 3E5

# Hubble's constant (km/s/Mpc)
Ho = 75

# Average redshift for each bin
redshift = []
# Average mass for each bin
Mstar = []
SFR = []
SSFR = []


for i in range(len(Martini)):

    Mr_min = Martini["Mr_min"][i]
    Mr_max = Martini["Mr_max"][i]

    bin_size = Martini["bin_size"][i]

    Mstar_min = Martini["Mstar_min"][i]
    Mstar_max = Martini["Mstar_max"][i]

    vflag = Martini["vflag"][i]
    if vflag == 0:
        vflag = "wall"
    else:
        vflag = "void"

    z_ave, M_ave = get_gal_info(galaxies, Mr_min, Mr_max, bin_size, Mstar_min, Mstar_max, vflag)

    redshift.append( z_ave )
    Mstar.append( M_ave )

    distance = ( c * z_ave ) / Ho

    H_Alpha = Martini["H_ALPHA_FLUX"][i] * 10 ** -17
    H_Beta = Martini["H_BETA_FLUX"][i] * 10 ** -17
    
    # Aperture Correction
    A_H_Alpha = 5.91 * log10( H_Alpha / H_Beta ) - 2.70

    # Dust-Corrected H_Alpha Flux
    fH_Alpha = H_Alpha * 10 ** (A_H_Alpha / 2.5)

    # Distance Conversion
    # Mpc to cm
    distance = ( ( c * z_ave ) / Ho ) * ( 3.0857 * 10 ** 24 )

    # H_Alpha Luminosity
    # flux is 10^-17 
    L_H_Alpha = 4 * pi * ( distance ** 2 ) * fH_Alpha

    #Star Formation Rate
    SFR_galaxy = ( 7.9 * 10 ** -41.28 ) * L_H_Alpha

    SFR.append( SFR_galaxy )

    #Specific Star Formation Rate
    SSFR_galaxy = SFR_galaxy / M_ave

    SSFR.append( SSFR_galaxy )

Martini["redshift"] = redshift
Martini["Mstar"] = Mstar
Martini["SFR"] = SFR
Martini["SSFR"] = SSFR
Martini.write(fileName[:-4] + "_redshift_SFR_SSFR", format = "ascii.commented_header", overwrite = True)
