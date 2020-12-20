
t os.path as os 
import argparse
import sys
import pandas as pd
import numpy as np
#import json

from hw3.verbosity import verbosity
from hw3.mentions import mentions
from hw3.helpers import rename, getnames
from hw3.foc import foc 
from hw3.dictionary import dictionary

def main():
	
	import json 
 
	parser=argparse.ArgumentParser()
	
 	#to check file ending
	def file_choices(choices,fname):
    		ext = os.splitext(fname)[1][1:]
    		if ext not in choices:
       			parser.error("file doesn't end with .json")
    		return fname

	parser.add_argument('src_file', help='the transcript file should be a csv' )
	#parser.add_argument('-o', '--output' type=lambda s:file_choices(("json"),s), help='Specify the output file (must be .json). Default is stdout')
	parser.add_argument('-o', '--output', help='Specify the output file (must be .json). Default is stdout') 
	args=parser.parse_args()
	
	#get our data
	src_file=args.src_file
	
	#set stdout 
	if args.output and args.output != '-':
		sys.stdout = open(args.output, 'w')
	#read data into df
	df = pd.read_csv(src_file)
	

	ponynames=['Twilight Sparkle', 'Applejack', 'Rarity', 'Pinkie Pie', 'Rainbow Dash', 'Fluttershy']


	js={}
	js["verbosity"]=verbosity(df, ponynames)
	js["mentions"]=mentions(df, ponynames)
	js["follow_on_comments"]=foc(df, ponynames)
	#js["non_dictionary_words"]=dictionary(df, ponynames)
	
	js = json.dumps(js, indent=4 * ' ')
	print(js)


if __name__ == '__main__':
	main()


'''
my results are:

{
    "verbosity": {
        "twilight": 0.26,
        "applejack": 0.16,
        "rarity": 0.15,
        "pinkie": 0.15,
        "rainbow": 0.17,
        "fluttershy": 0.11
    },
    "mentions": {
        "twilight": {
            "applejack": 0.19,
            "rarity": 0.21,
            "pinkie": 0.18,
            "rainbow": 0.2,
            "fluttershy": 0.22
        },
        "applejack": {
            "twilight": 0.06,
            "rarity": 0.32,
            "pinkie": 0.26,
            "rainbow": 0.2,
            "fluttershy": 0.16
        },
        "rarity": {
            "twilight": 0.07,
            "applejack": 0.34,
            "pinkie": 0.15,
            "rainbow": 0.22,
            "fluttershy": 0.21
        },
        "pinkie": {
            "twilight": 0.12,
            "applejack": 0.19,
            "rarity": 0.18,
            "rainbow": 0.32,
            "fluttershy": 0.19
        },
        "rainbow": {
            "twilight": 0.07,
            "applejack": 0.24,
            "rarity": 0.15,
            "pinkie": 0.23,
            "fluttershy": 0.31
        },
        "fluttershy": {
            "twilight": 0.09,
            "applejack": 0.13,
            "rarity": 0.33,
            "pinkie": 0.14,
            "rainbow": 0.3
        }
    },
    "follow_on_comments": {
        "twilight": {
            "applejack": "0.09",
            "rarity": "0.08",
            "pinkie": "0.11",
            "rainbow": "0.1",
            "fluttershy": "0.08",
            "other": "0.53"
        },
        "applejack": {
            "twilight": "0.15",
            "rarity": "0.14",
            "pinkie": "0.11",
            "rainbow": "0.14",
            "fluttershy": "0.08",
            "other": "0.39"
        },
        "rarity": {
            "twilight": "0.13",
            "applejack": "0.16",
            "pinkie": "0.1",
            "rainbow": "0.11",
            "fluttershy": "0.1",
            "other": "0.4"
        },
        "pinkie": {
            "twilight": "0.18",
            "applejack": "0.12",
            "rarity": "0.1",
            "rainbow": "0.15",
            "fluttershy": "0.07",
            "other": "0.39"
        },
        "rainbow": {
            "twilight": "0.17",
            "applejack": "0.12",
            "rarity": "0.09",
            "pinkie": "0.12",
            "fluttershy": "0.1",
            "other": "0.4"
        },
        "fluttershy": {
            "twilight": "0.18",
            "applejack": "0.11",
            "rarity": "0.14",
            "pinkie": "0.09",
            "rainbow": "0.15",
            "other": "0.34"
        }
    },
    "non_dictionary_words": {
        "twilight": [
            "ve",
            "celestia",
            "fluttershy",
            "everypony",
            "equestria"
        ],
        "applejack": [
            "ve",
            "somethin",
            "everypony",
            "doin",
            "fluttershy"
        ],
        "rarity": [
            "ve",
            "fluttershy",
            "canterlot",
            "equestria",
            "somepony"
        ],
        "pinkie": [
            "ve",
            "everypony",
            "fluttershy",
            "ponyville",
            "somepony"
        ],
        "rainbow": [
            "ve",
            "fluttershy",
            "everypony",
            "wonderbolts",
            "ponyville"
        ],
        "fluttershy": [
            "ve",
            "everypony",
            "fluttershy",
            "equestria",
            "somepony"
        ]
    }
}

'''
