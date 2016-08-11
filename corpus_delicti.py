#!/usr/bin/env python3

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, TweetTokenizer, PunktSentenceTokenizer
import pandas as pd


sample_text = "sample.txt"


stop_words = set(stopwords.words('german'))
#stop_words


with open(sample_text) as f:
    sample = f.read()

def tokenize_casual(sample_text):
    word_tokens = TweetTokenizer(preserve_case=True, strip_handles=False, reduce_len=False).tokenize(sample_text)
    #print(word_tokens)

    #word_tokens = map(str.lower, word_tokens) ## to lowercase
    #word_tokens = [ x.replace("[^A-Za-z0-9\u00F0-\u02AF#]+", "") for x in word_tokens ] #remove all which is not a letter or a number or an umlaut or a # , http://stackoverflow.com/questions/22017723/regex-for-umlaut
    #word_tokens = [ x.replace('\n', "") for x in word_tokens ] ##remove newline

    word_tokens = [w for w in word_tokens if not w in stop_words] ##remove stop words
    return(pd.Series(word_tokens))

tokenized = tokenize_casual(sample)
#print(tokenized)


print(tokenized.value_counts().head(50))


hasthag_worhty = ['Blöße', "Einhorn", "Bachblüten"]

## was in der liste hashtagworthy is
#[w for w in word_tokens if not w in stop_words]
