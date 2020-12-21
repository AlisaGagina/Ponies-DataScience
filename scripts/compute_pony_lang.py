import argparse
import json
import math




#TFIDF(word, pony) = freq(word | pony) * log( <num of words>/freq(word) ) as old
#TFIDF(word, pony) = freq(word | pony) * log( <num of ponies>/#ponies using word ) as new, when flag p exists
#score for one pony and one word
def tdidf(word, pony, d, totalwords, p):
	freqone=d[pony][word]
	if p: #flag
		freqall=0
		for pony, words in d.items():
			if word in words:
				freqall=freqall+1
		score = freqone* math.log10(6/freqall)
	else: #no flag
		freqall=0
		for pony, words in d.items():
			if word in words:
				freqall=freqall+words[word]
		score = freqone* math.log10(totalwords/freqall)
	return score



#get scores for all ponies
def scores (d, totalwords, p):
	scores= { 'twilight':{},'applejack':{},'rarity':{},'pinkie':{}, 'rainbow':{},  'fluttershy':{}} 
	for pony, words in d.items():
		for word in words:
			#get score
			scores[pony][word]=tdidf(word, pony, d, totalwords, p)
	for pony in scores:
		#sort in descending order
		scores[pony] = dict( sorted(scores[pony].items(), key=lambda item: item[1], reverse=True))
	return scores



#constant			
def counttotalwords(d):
	counter=0
	for pony, words in d.items():
		for word in words:
			counter=counter+words[word]
	print(counter)
	return counter
	

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("input",help="count json")
	parser.add_argument("num_words",help="number of highest words")
	parser.add_argument('-p', '--nostopwords', help= 'invoke if you do not want stop words', action='store_true')

	args = parser.parse_args()
	with open(args.input) as f:
		d=json.load(f)
	p=args.nostopwords #flag
	
	#calculate
	totalwords=counttotalwords(d)
	s=scores(d, totalwords, p)
	print(s)
	#print result
	result={}
	for pony in s:
		l=[]	
		for i in list(s[pony])[0:int(args.num_words)]:	
			l.append(i)
		result[pony]=l	
	print(result)

if __name__ == '__main__':
	main()
