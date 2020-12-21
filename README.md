# Ponies-DataScience
This a python based data analysis project on My Little Pony
## The data:
We’ll be using the dataset available here: [https://www.kaggle.com/liury123/my-little-pony-transcript](https://www.kaggle.com/liury123/my-little-pony-transcript)
For the purpose of this study, we’ll use only clean_dialog.csv and assume that the dataset is perfect. This should be saved as data/clean_dialog.csv
## The code:
For each pony, we will be computing:
- “verbosity”: the fraction of dialogue, measured in # of speech acts produced by this pony
- “mentions”: fraction of times each pony mentions the other
- “follow_on_comments”: the fraction of times each pony has a line that DIRECTLY follows the
others pony’s line
- “non_dictionary_words”: a list of the 5 non-dictionary words used most often by each Pony
  - the dictionary words will be taken from  words_alpha.txt, located here:
[https://github.com/dwyl/english-words](https://github.com/dwyl/english-words)
  - This should be saved in your project as data/words_alpha.txt
### Analysis.py
  is the main piece of code to be run. It will be run in a UNIX shell in which PYTHONPATH includes a path to the project’s src
directory. It should also accept an optional argument “-o <file_name>”. If given, the JSON output is
written to that file. If it is NOT given, the JSON output should be written to stdout.
### TF-IDF (compile_word_counts.py, compute_pony_lang.py)
Calculates the termfrequency-inversedocumentfrequency for each ponies' words. There is one script for computing word counts for each pony from all episodes of MLP, and saves each term used at least five times into a json file (`python compile_word_counts.py -o <word_counts_json> <clean_dialog.csv file>`). Then there is a second script for actually computing the scores and prints the top n distinct words used by each pony to stdout in json format (`python compute_pony_lang.py <pony_counts.json> <num_words>`). 
## To-dos:
  - non_dictionary_words takes way too long, need a better way
  - finish unit tests
