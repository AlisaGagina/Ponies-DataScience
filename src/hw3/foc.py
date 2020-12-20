'''
follow on comments
shift() to get rid of speech acts
for each pony
        for every other pony
                df[df.pony.shift()==otherpony].sum()
        other=df[~df.pony.shift().isin(ponynames)].sum()

'''
from hw3.helpers import rename

def foc (df, ponynames):
	c = df[df.pony.shift() != df.pony] #get rid off speech acts
	 #then make a nested dictionary for storage
	follow_on_comments={'twilight':{},
		'applejack':{},
		'rarity':{},                                                                                            'pinkie':{},
		'rainbow':{},
		'fluttershy':{}}

	for pony in ponynames:
		l=ponynames.copy()
		l.remove(pony)
		for otherp in l:
			p=rename(pony)
			o=rename(otherp)
			follow_on_comments[p][o] = df[(df['pony']==pony) & (df['pony'].shift() == otherp)].shape[0]
		follow_on_comments[p]["other"]= df[(df['pony']==pony) & ~(df.pony.shift().isin(ponynames))].shape[0]


	

	#normalize
	for p, o in follow_on_comments.items():
		factor=1.0/sum(o.values())
		for key in o:
			o[key]=str(round(o[key]*factor, 2))

	return follow_on_comments
