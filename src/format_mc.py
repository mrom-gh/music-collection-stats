'''Search the music collection for badly formatted directories.'''

import os

def find_missing_years(dir, bands):
	'''sucht Alben in dir, die keine Jahreszahl im Ordnernamen haben
	bands gibt dabei vor, welche Ordner als Bandordner erkannt werden'''
	count = 0
	for dirpath, subdirs, _ in os.walk(dir):
		for subdir in subdirs:
			words_in_subdir = subdir.split()
			words_in_path = dirpath.split('/')
			
			if words_in_path[-1] in bands and not words_in_subdir[0][0] in ['1', '2']:
				'''testet fuer jedes subdir, ob der Ordnername mit einer Jahreszahl beginnt
				dabei wird erst gecheckt, ob der Pfad wirklich auf einen Bandordner verweist
				
				sind Lieder direkt im Bandordner, sollten die Alben jetzt korrekt erkannt werden (keine falsch-Negativen mehr);
				Alben mit mehreren CDs werden in Einzelfaellen (z.B. OSTs) noch zu Unrecht erkannt (falsch-Positive)'''
				p = os.path.join(dirpath, subdir)
				count +=1
				print(p)
				#raw_input('next: press <Enter>')
	print(count)

def find_ugly_years(dir,bands):
	'''sucht Alben, bei denen das Jahr nicht im Standardformat "<Jahr> <Titel>" steht'''
	for dirpath, subdirs, _ in os.walk(dir):
		for subdir in subdirs:
			words_in_path = dirpath.split('/')
			if words_in_path[-1] in bands and '-' in subdir[4:6]:
				'''testet fuer jedes subdir, ob zwischen char 4 und 7 ein '-' ist,
				dabei wird erst gecheckt, ob der Pfad wirklich auf einen Bandordner verweist
				
				Alben, die ein anderes Format haben, werden nicht erkannt (falsch-Negative!)
				'''
				p = os.path.join(dirpath, subdir)
				print(p)