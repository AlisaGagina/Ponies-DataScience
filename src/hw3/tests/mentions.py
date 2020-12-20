mport unittest
import pandas as pd
from hw3.mentions import mentions

class VerbTestCase(unittest.TestCase):
        ponynames =['Twilight Sparkle', 'Applejack', 'Rarity', 'Pinkie Pie', 'Rainbow Dash', 'Fluttershy']
        def test_empty(self):
                data = {'title':  ['a', 'b'],
                        'writer': ['Laura', 'Sue'],
                        'pony': ['Fluttershy', 'Rarity'],
                        'dialog': ['wee wqe qweq', 'ha aha a']
                 }
                df= pd.DataFrame (data, columns=['title', 'writer', 'pony', 'dialog'])

                values = verbosity(df, ['Twilight Sparkle', 'Applejack', 'Rarity', 'Pinkie Pie', 'Rainbow Dash', 'Fluttershy'] )
                self.assetEqual(values, {'twilight':{'applejack':0, 'rarity':0, 'pinkie':0, 'rainbow':0, 'fluttershy':0},
					'applejack':{'twilight':0, 'rarity':0, 'pinkie':0, 'rainbow':0, 'fluttershy':0},
					'rarity':{'twilight':0, 'applejack':0, 'pinkie':0, 'rainbow':0, 'fluttershy':0},
					'pinkie':{'twilight':0, 'applejack':0, 'rarity':0, 'rainbow':0, 'fluttershy':0},
					'rainbow':{'twilight':0,'applejack':0, 'rarity':0, 'pinkie':0,  'fluttershy':0},
					'fluttershy':{'twilight':0, 'applejack':0, 'rarity':0, 'pinkie':0, 'rainbow':0}  )
        def test_onemention(self):
                data = {'title':  ['a', 'b'],
                        'writer': ['Laura', 'Sue'],
                        'pony': ['Fluttershy', 'Rarity'],
                        'dialog': ['Rarity is awesome', 'ha aha a']}

                df= pd.DataFrame (data, columns=['title', 'writer', 'pony', 'dialog'])
                values = verbosity(df, ['Twilight Sparkle', 'Applejack', 'Rarity', 'Pinkie Pie', 'Rainbow Dash', 'Fluttershy'] )
                self.assetEqual(values, {'twilight':{'applejack':0, 'rarity':0, 'pinkie':0, 'rainbow':0, 'fluttershy':0},
                                        'applejack':{'twilight':0, 'rarity':0, 'pinkie':0, 'rainbow':0, 'fluttershy':0},
                                        'rarity':{'twilight':0, 'applejack':0, 'pinkie':0, 'rainbow':0, 'fluttershy':0},
                                        'pinkie':{'twilight':0, 'applejack':0, 'rarity':0, 'rainbow':0, 'fluttershy':0},
                                        'rainbow':{'twilight':0,'applejack':0, 'rarity':0, 'pinkie':0,  'fluttershy':0},
                                        'fluttershy':{'twilight':0, 'applejack':0, 'rarity':1, 'pinkie':0, 'rainbow':0}  )                                                                                    

        def test_doublemention(self):
		 data = {'title':  ['a', 'b'],
                        'writer': ['Laura', 'Sue'],
                        'pony': ['Fluttershy', 'Rarity'],
                        'dialog': ['Rarity is awesome', 'Sparkle']}

                df= pd.DataFrame (data, columns=['title', 'writer', 'pony', 'dialog'])
                values = verbosity(df, ['Twilight Sparkle', 'Applejack', 'Rarity', 'Pinkie Pie', 'Rainbow Dash', 'Fluttershy'] )
                self.assetEqual(values, {'twilight':{'applejack':0, 'rarity':0, 'pinkie':0, 'rainbow':0, 'fluttershy':0},
                                        'applejack':{'twilight':0, 'rarity':0, 'pinkie':0, 'rainbow':0, 'fluttershy':0},
                                        'rarity':{'twilight':1, 'applejack':0, 'pinkie':0, 'rainbow':0, 'fluttershy':0},                                                                                                                                   'pinkie':{'twilight':0, 'applejack':0, 'rarity':0, 'rainbow':0, 'fluttershy':0},
                                        'rainbow':{'twilight':0,'applejack':0, 'rarity':0, 'pinkie':0,  'fluttershy':0},
                                        'fluttershy':{'twilight':0, 'applejack':0, 'rarity':1, 'pinkie':0, 'rainbow':0}  )
        def test_trickymention(self):
                 data= {'title':  ['a', 'b'],
                        'writer': ['Laura', 'Sue'],
                        'pony': ['Fluttershy', 'Rarity'],
                        'dialog': ['Rarity is awesome', 'Twilight Twilight Sparkle']}

                df= pd.DataFrame (data, columns=['title', 'writer', 'pony', 'dialog'])
                values = verbosity(df, ['Twilight Sparkle', 'Applejack', 'Rarity', 'Pinkie Pie', 'Rainbow Dash', 'Fluttershy'] )
                self.assetEqual(values, {'twilight':{'applejack':0, 'rarity':0, 'pinkie':0, 'rainbow':0, 'fluttershy':0},
                                        'applejack':{'twilight':0, 'rarity':0, 'pinkie':0, 'rainbow':0, 'fluttershy':0},
                                        'rarity':{'twilight':1, 'applejack':0, 'pinkie':0, 'rainbow':0, 'fluttershy':0},                                                                                                                                   'pinkie':{'twilight':0, 'applejack':0, 'rarity':0, 'rainbow':0, 'fluttershy':0},
                                        'rainbow':{'twilight':0,'applejack':0, 'rarity':0, 'pinkie':0,  'fluttershy':0},
                                        'fluttershy':{'twilight':0, 'applejack':0, 'rarity':1, 'pinkie':0, 'rainbow':0}  )
