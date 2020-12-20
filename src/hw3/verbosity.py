'''Verbosity Code
'''
import pandas as pd


def verbosity (df, ponynames):
	#split by episodes
	titles= df.groupby('title')

	#group by consecutives
	#for t in titles:
        	#v=verbosity.groupby(((df['pony'].shift() != df['pony'])).cumsum())

	v=df.groupby(((df['pony'].shift() != df['pony'])).cumsum())
	#just get first sentence of each speach act
	vp= v.first()
	vp=vp.loc[vp['pony'].isin(ponynames)]
	vp=vp.replace({'Twilight Sparkle':'twilight', 'Applejack':'applejack', 'Rarity':'rarity',
    	'Pinkie Pie':'pinkie', 'Rainbow Dash':'rainbow', 'Fluttershy':'fluttershy'})

	
	res={}
	result=vp['pony'].value_counts(normalize=True).round(2)
	
	if ((result.isin(['twilight'])).all() == False):
		result["twilight"]=0.0	
	if ((result.isin(['applejack'])).all() == False):
                result["applejack"]=0.0
	if ((result.isin(['rarity'])).all() == False):
                result["rarity"]=0.0
	if ((result.isin(['pinkie'])).all() == False):
                result["pinkie"]=0.0
	if ((result.isin(['rainbow'])).all() == False):
                result["rainbow"]=0.0
	if ((result.isin(['fluttershy'])).all() == False):
                result["fluttershy"]=0.0



	
	print("res", result["twilight"])
	res["twilight"]=result['twilight']
	res["applejack"]=result['applejack']
	res["rarity"]=result['rarity']
	res["pinkie"]=result['pinkie']
	res["rainbow"]=result['rainbow']
	res["fluttershy"]=result['fluttershy']
	print(res)
	return res

