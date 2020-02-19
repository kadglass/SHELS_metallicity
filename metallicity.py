
from astropy.table import Table
from numpy import log10

bin_size = [0.1, 0.2, 0.3, 0.4, 0.5]
environment = ["void", "wall"]

for i in bin_size:

    for j in environment:

        file = "/Users/leilani/Desktop/SHELS/LGamboa/{0}Bin_{1}.txt".format(i, j, "a+")
        data =Table.read(file, format = "ascii.commented_header")

        N2_list = []
        O3N2_list = []
        N2O2_list = []

        for h in range( len(data) ):

            ### DEFINITIONS ###

                # 0II/0III/NII are observed

            HaF = data["HaF"][h]
            HbF = data["HbF"][h]
            OII = data["OII"][h]  #3727
            NII = data["NII"][h]  #6583
            OIII = data["OIII"][h]  #5007
            SSFR = data["SSFR"][h]
            mass = data["mass"][h]

            ### EQUATIONS ###

                # 02/03/N2 are ratios

            N2 = NII / HaF
            O3N2 = OIII / HbF / N2  #yes, this is the correct equation (see Brown et al)
            N2O2 = NII / OII

                # Average SSFR at Mstar

            mass = log10(mass)
            aveSSFR = 283.728 - ( 116.265 * mass) + ( 17.4403 * (mass ** 2) ) - ( 1.17146 * (mass ** 3) ) + ( 0.0296526 * (mass ** 4) )
           
               # Delta log(SSFR)
           
            d_logSSFR = log10(SSFR) - aveSSFR

                # N2 Method

            N2_metallicity = 9.12  + ( 0.58 * log10(N2) ) - ( 0.19 * d_logSSFR )
            N2_list.append(N2_metallicity)

                # O3N2 Method

            O3N2_metallicity = 8.98 - ( 0.32 * log10(O3N2) ) - ( 0.18 * d_logSSFR )
            O3N2_list.append(O3N2_metallicity)

                # N2O2 Method

            N2O2_metallicity = 9.20 + ( 0.54 * log10(N2O2) ) - ( 0.36 * d_logSSFR )
            N2O2_list.append(N2O2_metallicity)

        data["N2"] = N2_list
        data["O3N2"] = O3N2_list
        data["N2O2"] = N2O2_list

        data.write(file, format = "ascii.commented_header", overwrite = True)


