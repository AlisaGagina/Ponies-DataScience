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
## To-dos:
  - non_dictionary_words takes way too long, need a better way
  - finish unit tests
