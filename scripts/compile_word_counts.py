import argparse
import pandas as pd
import json

def rename (str):
        if str=='Twilight Sparkle' : return 'twilight'
        if str=='Applejack': return 'applejack'
        if str== 'Rarity':return 'rarity'
        if str=='Pinkie Pie': return 'pinkie'
        if str=='Rainbow Dash':return 'rainbow'
        if str=='Fluttershy': return 'fluttershy'

def clean(df):
	#drop unneeded columns
	df=df.drop('title', axis=1)
	df=df.drop('writer', axis=1)
	ponies= ['Twilight Sparkle', 'Rainbow Dash', 'Pinkie Pie', 'Applejack', 'Rarity', 'Fluttershy']
	#drop unneeded ponies
	df=df[df['pony'].isin(ponies)]
	
	#regex, lowercase
	df['dialog']=df['dialog'].str.replace('<U\+....>', ' ')
	df['dialog']=df['dialog'].str.replace(r'[^\w\s\']+', ' ')
	df['dialog']=df['dialog'].str.replace(r'\d+', ' ')
	df['dialog']=df['dialog'].str.lower()
	return df

def getwordcounts(df):	
	count={'Twilight Sparkle':{}, 'Rainbow Dash':{}, 'Pinkie Pie':{}, 'Applejack':{}, 'Rarity':{}, 'Fluttershy':{}}
	#get counts
	for index,row in df.iterrows():
		pony=row['pony']
		d=row['dialog']
		words = d.split()
		for word in words:
			#print(word)
			if (word not in count[pony]):
				count[pony][word] = 1
			else:
				count[pony][word] += 1
	abovefive={ 'twilight':{},'applejack':{},'rarity':{},'pinkie':{}, 'rainbow':{},  'fluttershy':{}}
	#get counts above four
	for pony, words in count.items():
		for word in words:
			if words[word]>=5:
				abovefive[rename(pony)][word]=words[word]
	return abovefive


def main():
	
	parser = argparse.ArgumentParser()
	parser.add_argument("input", help="cleandialog.csv file")
	parser.add_argument('-o', '--output', help='output file')

	args = parser.parse_args()
	df = pd.read_csv(args.input)	
	df=clean(df)
	count=getwordcounts(df)
	
	print (count)	
	
	with open(args.output, 'w') as f:
		json.dump(count, f)
	
if __name__ == '__main__':
	main()

