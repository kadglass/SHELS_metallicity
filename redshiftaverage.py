

### Import Libraries ###

from numpy import mean
from astropy.table import Table
import os, os.path


def redshiftaverage(bin_size, environment):

    ### Definitions ###

    bin_size = str(bin_size)

    file = "/Users/leilani/Desktop/SHELS/LGamboa/{0}Bin_{1}.txt".format(bin_size, environment, "a+")
    data = Table.read(file, format = "ascii.commented_header")
    redshift = [ ]
    mass = [ ]

    simple = Table.read("/Users/leilani/Desktop/SHELS/SHELSgalaxies_simpleHeader_vflag_rabsmag.txt", format = "ascii.commented_header")

    for i in range(len(data)):

        MinAM = str(data["MinAM"][i])
        MaxAM = str(data["MaxAM"][i])
        MinSM = str(data["MinSM"][i])
        MaxSM = str(data["MaxSM"][i])

        if os.path.exists("/Users/leilani/Desktop/SHELS/KDouglass/SHELSgalaxies_{0}{1}_Mstar_{2}_{3}-{4}_{5}.txt".format(MinAM, MaxAM, bin_size, MinSM, MaxSM, environment)) == True:

            Douglass = "/Users/leilani/Desktop/SHELS/KDouglass/SHELSgalaxies_{0}{1}_Mstar_{2}_{3}-{4}_{5}.txt".format(MinAM, MaxAM, bin_size, MinSM, MaxSM, environment)
            Douglass = Table.read(Douglass, format = "ascii.no_header")
            ID = Douglass["col1"]

            AveR = []
            AveM = []

            for index, value in enumerate(ID):

                for j in range(len(simple)):

                    if value == simple["ID"][j]:

                        z = simple["redshift"][j]
                        r = simple["Mstar"][j]
                        AveR.append(z)
                        AveM.append(r)

                    else:

                        continue

            AveR = mean(AveR)
            AveM = mean(AveM)
            redshift.append(AveR)
            mass.append(AveM)


        else:

            redshift.append(0)
            mass.append(0)
            continue

    data["redshift"] = redshift
    data["mass"] = mass
    data.write(file, format = "ascii.commented_header", overwrite = True)


