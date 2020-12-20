'''mentions code'''
import pandas as pd
from hw3.helpers import rename, getnames 

def mentions(df, ponynames):
	#for pony in ponynames, in all of their dialog, for each other pony str.count(ponyname).sum()

	ponies = df.loc[df['pony'].str.lower().isin([p.lower() for p in ponynames])] #case insensitive

	#then make a nested dictionary for storage
	mentions={'twilight':{},
		'applejack':{},
		'rarity':{},                                                                                                                                                                                                       'pinkie':{},
		'rainbow':{},
		'fluttershy':{}}

	twilight='Twilight Sparkle | Twilight | Sparkle'
	applejack= 'Applejack'
	rarity= 'Rarity'
	pinkie='Pinkie Pie | Pinkie | Pie'
	rainbow='Rainbow Dash | Rainbow | Dash'
	fluttershy= 'Fluttershy'
	allnames=[twilight, applejack, rarity, pinkie, rainbow, fluttershy]


	#most of out work is done here, use str count to count mentions and save in dictionary
	for pony in ponynames:
		l=ponynames.copy()
		l.remove(pony)
		for otherp in l:
			p=rename(pony)
			o=rename(otherp)
			mentions[p][o] = ponies.loc[ponies['pony'] == pony]['dialog'].str.count(getnames(otherp)).sum()
																											   #next we normalize
	for p, o in mentions.items():
		factor=1.0/sum(o.values())
		for key in o:
			o[key]=(o[key]*factor).round(2)

	return mentions
