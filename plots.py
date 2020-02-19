
import matplotlib.pyplot as plt
from astropy.table import Table
from numpy import log10

bin_size = [0.1, 0.2, 0.3, 0.4, 0.5]
method = ["N2", "O3N2", "N2O2"]

for i in bin_size:

    void = "/Users/leilani/Desktop/SHELS/LGamboa/{0}Bin_void.txt".format(i)
    wall = "/Users/leilani/Desktop/SHELS/LGamboa/{0}Bin_wall.txt".format(i)

    vfile = Table.read(void, format = "ascii.commented_header")
    wfile = Table.read(wall, format = "ascii.commented_header")

    for j in method:

        plt.scatter(vfile["mass"], log10(vfile["SSFR"]), c = vfile[j])
        plt.scatter(wfile["mass"], log10(wfile["SSFR"]), c = wfile[j], marker = "^")

        cbar = plt.colorbar()
        cbar.set_label(f"12 + $log(O/H)_{j}$")

        plt.xlabel("$M_*$ [log($M_\odot$)]")
        plt.ylabel("SSFR [SFR/$M_*$]")
        plt.savefig(f"/Users/leilani/Desktop/SHELS/LGamboa/Plots/{i}bin_{j}method.pdf", overwrite = True)
        plt.close()


