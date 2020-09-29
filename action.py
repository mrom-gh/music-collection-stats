#!/usr/bin/env python3
'''Traverse a music collection and create a histogram of albums per
year. If no path is given, use the cwd.

The module stats_mc contains the functions ``find_missing_years(dir,
bands)`` and ``find_ugly_years(dir, bands)`` which can be used for
interactive searches for badly formatted directories in the music
collection.
'''

import sys, os
import matplotlib.pyplot as plt
from music_collection import MusicCollection

# to do:
# - moeglichkeit, band liste und dict zu speichern -> db
# - return histo
# - zeitraum suche
# - mehrere musikordner
# - zahl in histo vergleichen mit gesamtzahl der alben

if len(sys.argv) > 1:
    music_collection_path = sys.argv[1]
else:
    music_collection_path = os.getcwd()
print("music_collection_path = %s \n" % music_collection_path)

mc = MusicCollection(music_collection_path)
mc.fill()
mc.plot_histo()