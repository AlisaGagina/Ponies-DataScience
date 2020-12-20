'''
non-dictionary words
clean up dataframe
using stopword logic, get rid off all normal words
split() words in strings, use a dictionary to keep count of word occurences
        where df[df['pony']==pony]
use collections to get most occuring words
'''

import collections
import re
from hw3.helpers import rename

def dictionary (df, ponynames):
	#clean up data
	d=df
	d['dialog']=d['dialog'].str.replace('<U\+....>', ' ')
	#for our main ponies only
	d=d.loc[d['pony'].str.lower().isin([p.lower() for p in ponynames])]

	file=open('../data/words_alpha.txt')
	dicwords = file.read().split()

	#remove ictionary words function
	def rm_dicwords (sentence):
		words= re.findall('[a-zA-Z0-9]*', sentence)
		nondicwords= [word for word in words if not word in dicwords and not word=='']
		print(nondicwords)
		return nondicwords


	#UNCOMMENT PART FOR QUICK CHECK
	d['dialog']=d['dialog'].str.lower().apply(rm_dicwords)
	#part=d.head(100)
	#part['dialog']=part['dialog'].str.lower().apply(rm_dicwords)

	#emprty dictionary for storage
	ndict={}
	#cycle and count non-dictionary words
	for pony in ponynames:
		wordcount={}
		p=d[d['pony']==pony]
		#p=part[part['pony']==pony]
		for row in p['dialog']:
			for word in row:
				if word not in wordcount:
					wordcount[word]=1
				else:
					wordcount [word]+=1
		word_counter=collections.Counter(wordcount)
		l=[]
		for word, count in word_counter.most_common(5):
			l.append(word)
		ndict[rename(pony)]=l

	return( ndict)
