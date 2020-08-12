from os import *
from pylab import *
from format import *
from statistik import *

# to do:
#moeglichkeit, band liste und dict zu speichern
#return histo
#zeitraum suche
#mehrere musikordner
#zahl in histo vergleichen mit gesamtzahl der alben

# Variablen
dir = getcwd()
print 'cwd =', dir, '\n'
print 'generating band list...\n'
bands = get_band_list(dir)

# Albumformat
# print 'finding missing years...\n'
# find_missing_years(dir,bands)
# print 'finding ugly years...\n'
# find_ugly_years(dir,bands)

# Histogramm nach Jahren
print 'generating dict of years...\n'
d = get_dict_of_years(dir,bands)
print 'generating histo...'
histo(d,bands,'Jahre','Anzahl Alben','Titel')
show()

# Suche
#year = 2005
#print 'gesuchte Alben:', d[year]
