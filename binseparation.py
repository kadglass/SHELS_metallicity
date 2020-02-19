### CURRENTLY CREATING NEW FILES ###

### Import Libraries ###

import numpy as np
import os
from astropy.table import Table


def binseparation(bin_size):

    ### Definitions ###

    Martini = Table.read("SHELSgalaxies_Martini_flux.txt", format = "ascii.commented_header")

    ### Void Environment
    VOID_MinAbsoluteMagnitude = []
    VOID_MaxAbsoluteMagnitude = []
    VOID_MinStellarMass = []
    VOID_MaxStellarMass = []
    VOID_HAlphaFlux = []
    VOID_HAlphaFluxError = []
    VOID_HBetaFlux = []
    VOID_HBetaFluxError = []
    VOID_OIIFlux = []
    VOID_OIIIFlux = []
    VOID_NIIFlux = []

    ### Wall Environment
    WALL_MinAbsoluteMagnitude = []
    WALL_MaxAbsoluteMagnitude =[]
    WALL_MinStellarMass = []
    WALL_MaxStellarMass = []
    WALL_HAlphaFlux = []
    WALL_HAlphaFluxError = []
    WALL_HBetaFlux =[]
    WALL_HBetaFluxError =[]
    WALL_OIIFlux = []
    WALL_OIIIFlux = []
    WALL_NIIFlux = []

    # we dont really need the absolute magnitude for our calculations
    # but we need the SHELS galaxy ID to find the redshift, which we DO need to determine the SFR


    ### Separation by Environment ###

    for i in range( len(Martini) ):

        if Martini["bin_size"][i] == bin_size:  # Change file names

            if Martini["vflag"][i] == 1:
                VOID_MinAbsoluteMagnitude.append( Martini["Mr_min"][i] )
                VOID_MaxAbsoluteMagnitude.append( Martini["Mr_max"][i] )
                VOID_MinStellarMass.append( Martini["Mstar_min"][i] )
                VOID_MaxStellarMass.append( Martini["Mstar_max"][i] )
                VOID_HAlphaFlux.append( Martini["H_ALPHA_FLUX"][i] )
                VOID_HAlphaFluxError.append( Martini["H_ALPHA_FLUX_ERR"][i] )
                VOID_HBetaFlux.append( Martini["H_BETA_FLUX"][i] )
                VOID_HBetaFluxError.append( Martini["H_BETA_FLUX_ERR"][i] )
                VOID_OIIFlux.append( Martini["OII_3727_FLUX"][i] )
                VOID_OIIIFlux.append( Martini["OIII_5007_FLUX"][i] )
                VOID_NIIFlux.append( Martini["NII_6584_FLUX"][i] )

            elif Martini["vflag"][i] == 0:
                WALL_MinAbsoluteMagnitude.append( Martini["Mr_min"][i] )
                WALL_MaxAbsoluteMagnitude.append( Martini["Mr_max"][i] )
                WALL_MinStellarMass.append( Martini["Mstar_min"][i] )
                WALL_MaxStellarMass.append( Martini["Mstar_max"][i] )
                WALL_HAlphaFlux.append( Martini["H_ALPHA_FLUX"][i] )
                WALL_HAlphaFluxError.append( Martini["H_ALPHA_FLUX_ERR"][i] )
                WALL_HBetaFlux.append( Martini["H_BETA_FLUX"][i] )
                WALL_HBetaFluxError.append( Martini["H_BETA_FLUX_ERR"][i] )
                WALL_OIIFlux.append( Martini["OII_3727_FLUX"][i] )
                WALL_OIIIFlux.append( Martini["OIII_5007_FLUX"][i] )
                WALL_NIIFlux.append( Martini["NII_6584_FLUX"][i] )

            else:
                print("SCREEEEEECCCCHHHHHH")


        else:
            pass


    ### Create Tables ###

    VOID = Table( [VOID_MinAbsoluteMagnitude, VOID_MaxAbsoluteMagnitude, VOID_MinStellarMass, VOID_MaxStellarMass, VOID_HAlphaFlux, VOID_HAlphaFluxError, VOID_HBetaFlux, VOID_HBetaFluxError, VOID_OIIFlux, VOID_OIIIFlux, VOID_NIIFlux], names = ("MinAM", "MaxAM","MinSM", "MaxSM", "HaF", "HaFe", "HbF", "HbFe", "OII", "OIII", "NII" ) )  # Column names are abbreviated

    WALL = Table( [WALL_MinAbsoluteMagnitude, WALL_MaxAbsoluteMagnitude, WALL_MinStellarMass, WALL_MaxStellarMass, WALL_HAlphaFlux, WALL_HAlphaFluxError, WALL_HBetaFlux, WALL_HBetaFluxError, WALL_OIIFlux, WALL_OIIIFlux, WALL_NIIFlux], names = ("MinAM", "MaxAM", "MinSM", "MaxSM", "HaF", "HaFe", "HbF", "HbFe", "OII", "OIII", "NII") )  # Column names are abbreviated


    ### Write and Save Files ###

    # Change bin size
    VOID.write("/Users/leilani/Desktop/SHELS/LGamboa/" + str(bin_size) + "Bin_void.txt", format = "ascii.commented_header", overwrite = True )
    WALL.write("/Users/leilani/Desktop/SHELS/LGamboa/" +str(bin_size) + "Bin_wall.txt", format = "ascii.commented_header", overwrite = True )
