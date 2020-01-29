from astropy.table import Table
import numpy as np

def get_gal_info(galaxies, Mr_min, Mr_max, bin_size, Mstar_min, Mstar_max, vflag):

    # Directory + Filename
    fileName = "/Users/leilani/Documents/SHELS_Research/KDouglass/SHELSgalaxies_{0}{1}_Mstar_{2}_{3}-{4}_{5}.txt".format(Mr_min, Mr_max, bin_size, Mstar_min, Mstar_max, vflag)

    # Read Table with galaxy IDs for one bin
    IDS = Table.read(fileName, format = "ascii.no_header")

    ID_list = IDS["col1"]

    redshift_list = [0 for i in range(len(ID_list))]
    mass_list = [0 for i in range(len(ID_list))]

    # i = index postion
    # index = value in i (the value is the ID)
    for i, index in enumerate(ID_list):

        for j in range(len(galaxies)):

            if index == galaxies["ID"][j] :
                redshift = galaxies["redshift"][j]
                mass = galaxies["Mstar"][j]

                redshift_list[i] = redshift
                mass_list[i] = mass

            else:
                pass

    z_ave = np.mean(redshift_list)
    M_ave = np.mean(mass_list)

    return z_ave, M_ave

    
