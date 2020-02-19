
### Import Libraries ###

from numpy import log10, pi, mean
from astropy.table import Table
import os, os.path


def starformationrate(bin_size, environment):

    ### Definitions ###

    bin_size = str(bin_size)

    file = "/Users/leilani/Desktop/SHELS/LGamboa/{0}Bin_{1}.txt".format(bin_size, environment, "a+")
    data = Table.read(file, format = "ascii.commented_header")

    formationrate = []
    specificformationrate = []


    ### Constants ###

    c = 3E5  # Speed of Light (km/s)
    H0 = 70  # Hubble's Constant (km/s/Mpc)


    for i in range(len(data)):

        ### Variables ###

        z = data["redshift"][i]
        HaF = data["HaF"][i]
        HbF = data["HbF"][i]
        mass = data["mass"][i]


        ### Nifty Equations ###

        Dl = ( z * c ) / H0  # Distance Luminosity 
        AHa = 5.91 * log10( HaF / HbF ) -2.70  # Dust Attentuation Correction for H Alpha
        fHa = HaF * ( 10 ** ( AHa / 2.5) )  # Corrected H Alpha
        LHa = 4 * pi * ( Dl ** 2 ) * fHa  # H Alpha Luminosity
        SFR = 7.9 * ( 10 ** -41.28 ) * ( LHa )  # Star Formation Rate: H Alpha Method

        if SFR == 0.0 and mass == 0.0:

            SSFR = 0

        else:

            SSFR = SFR / mass  # Specific Star Formation Rate

        formationrate.append(SFR)
        specificformationrate.append(SSFR)

    data["SFR"] = formationrate
    data["SSFR"] = specificformationrate

    data.write(file, format = "ascii.commented_header", overwrite = True)


