'''Traverse a music collection and create a histogram of albums per
year. If no path is given, use the cwd.

The module stats_mc contains the functions ``find_missing_years(dir,
bands)`` and ``find_ugly_years(dir, bands)`` which can be used for
interactive searches for badly formatted directories in the music
collection.
'''

import sys, os
import matplotlib.pyplot as plt
from stats_mc import get_band_list, get_dict_of_years, histo

# to do:
# - moeglichkeit, band liste und dict zu speichern
# - return histo
# - zeitraum suche
# - mehrere musikordner
# - zahl in histo vergleichen mit gesamtzahl der alben

if len(sys.argv) > 1:
    dir = sys.argv[1]
else:
    dir = os.getcwd()
print("\ndir = %s \n" % dir)

print('generating band list...\n')
bands = get_band_list(dir)

print('generating dict of years...\n')
d = get_dict_of_years(dir,bands)

print('generating histogram...')
histo(d,bands,'Jahre','Anzahl Alben','Titel')
plt.show()