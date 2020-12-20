import unittest
import pandas as pd


from hw3.verbosity import verbosity

class VerbTestCase(unittest.TestCase):
	
	def test_empty(self):
		data = {'title':  ['a', 'b'],
        		'writer': ['Laura', 'Sue'],
			'pony': ['pony1', 'pony2'],	
			'dialog': ['wee wqe qweq', 'ha aha a']
       		 }
		df= pd.DataFrame (data, columns=['title', 'writer', 'pony', 'dialog'])
		
		values = verbosity(df, ['Twilight Sparkle', 'Applejack', 'Rarity', 'Pinkie Pie', 'Rainbow Dash', 'Fluttershy'] )
		self.assetEqual(values, {'twilight':0, 'applejack':0, 'rarity':0, 'pinkie':0, 'rainbow':0, 'fluttershy':0}  )
	def test_onespeaker(self):
		data = {'title':  ['a', 'b'],
			'writer': ['Laura', 'Sue'],
			'pony': ['Twilight Sparkle', 'pony2'],
			'dialog': ['wee wqe qweq', 'ha aha a']} 
		
		df= pd.DataFrame (data, columns=['title', 'writer', 'pony', 'dialog'])
		values = verbosity(df, ['Twilight Sparkle', 'Applejack', 'Rarity', 'Pinkie Pie', 'Rainbow Dash', 'Fluttershy'])
		self.assetEqual(values, "{'twilight':1, 'applejack':0, 'rarity':0, 'pinkie':0, 'rainbow':0, 'fluttershy':0}" )                                                                                                                     


	def test_twospeakers(self):
		data = {'title':  ['a', 'b', 'a'],
			'writer': ['Laura', 'Sue', 'Sue'],
			'pony': ['Fluttershy', 'Applejack', 'Fluttershy'],
			'dialog': ['wee wqe qweq', 'ha aha a', 'yo']}
		df= pd.DataFrame (data, columns=['title', 'writer', 'pony', 'dialog'])
		values = verbosity(df, ['Twilight Sparkle', 'Applejack', 'Rarity', 'Pinkie Pie', 'Rainbow Dash', 'Fluttershy'] )
		self.assetEqual(values, {'twilight':0, 'applejack':0.33, 'rarity':0, 'pinkie':0, 'rainbow':0, 'fluttershy':0.66}  )                                                                

	def test_speechact(self):
		data = {'title':  ['a', 'a', 'a'],
			'writer': ['Sue', 'Sue', 'Sue'],
			'pony': ['Fluttershy', 'Fluttershy', 'Applejack'],
			'dialog': ['wee wqe qweq', 'ha aha a', 'yo']}
		df= pd.DataFrame (data, columns=['title', 'writer', 'pony', 'dialog'])
		values = verbosity(df, ['Twilight Sparkle', 'Applejack', 'Rarity', 'Pinkie Pie', 'Rainbow Dash', 'Fluttershy'])
		self.assetEqual(values, {'twilight':0, 'applejack':0.5, 'rarity':0, 'pinkie':0, 'rainbow':0, 'fluttershy':0.5}  )
