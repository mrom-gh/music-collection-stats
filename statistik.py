from os import *
from pylab import *

def get_band_list(dir):
	'''erstellt eine Liste der Bandordner in dir
	Ann.: Ordner der Subgenres fangen mit '#' an'''
	bands = []
	for dirpath, subdirs, files in walk(dir):
		if dirpath == dir:
			'''legt eine Liste aller styles an'''
			styles = subdirs

		words_in_path = dirpath.split('/')
		if words_in_path[-1] in styles:
			for subdir in subdirs:
				if subdir[0] == '#':
					'''haengt substyles an'''
					styles.append(subdir)
				else:
					'''legt eine Liste aller Bandordner an'''
					bands.append(subdir)
	return bands

def get_dict_of_years(dir,bands):
	'''benutzt walk um ein nach Jahren sortiertes dict aller Alben in dir anzulegen'''
	d = {}
	for dirpath, subdirs, files in walk(dir):
		for subdir in subdirs:
			words_in_subdir = subdir.split()
			words_in_path = dirpath.split('/')
			
			if words_in_path[-1] in bands and words_in_subdir[0][0] in ['1', '2']:
				'''checkt, ob der Pfad auf einen Bandordner verweist und ob das subdir mit einer Jahreszahl anfaengt
				und haengt dann das subdir an das entsprechende Jahr bei d an'''
				year = int(words_in_subdir[0])
				if year not in d:
					d[year] = []
				d[year].append(subdir)
	return d

def histo(d,bands,x='x',y='y',titel=''):
	'''macht aus dem dict ein histogramm und plottet es mit pylab'''
	t = []
	check = {}
	
	for year in d:
		for item in range(len(d[year])):
			'''legt fuer jedes Album einen eigenen Listeneintrag mit der Jahreszahl an'''
			t.append(year)
		
		check[year] = len(d[year])
	print '\ncheck histo:'
	for item in check:
		print item,'-',check[item]
	
	zeitraum = max(t) - min(t)
	print len(check), 'Eintraege in einem Zeitraum von', zeitraum, 'Jahren\n'
	print len(bands), 'Bands und', len(t), 'Alben erfasst\n'
	#print t, '\n'

	h = hist(t, zeitraum+1)
	xlabel(x)
	ylabel(y)
	title(titel)
