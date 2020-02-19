
from binseparation import binseparation
from redshiftaverage import redshiftaverage
from starformationrate import starformationrate

bin_size = [0.1, 0.2, 0.3, 0.4, 0.5]
environment = ["void", "wall"]

for i in bin_size:

    binseparation(i)

    for j in environment:

        redshiftaverage(i, j)

        starformationrate(i, j)


