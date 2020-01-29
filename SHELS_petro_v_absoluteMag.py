from astropy.io import ascii
from astropy.table import Table
import matplotlib.pyplot as plt

SHELS_rabsmag = Table.read("SHELS_rabsmag.txt", format = "ascii.commented_header")

petroMag_r = SHELS_rabsmag["petroMag_r"]
rabsmag = SHELS_rabsmag["rabsmag"]

plt.scatter(petroMag_r, rabsmag,label = "Petrosian r-magnitude v. Absolute r-band magnitude")
plt.xlabel("Petrosian r-magnitude")
plt.ylabel("Absolute r-band magnitude")
plt.legend()
plt.save(label = "Petrosian r-magnitude v. Absolute r-band magnitude")
#plt.show()
