#!/usr/bin/env python3

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, TweetTokenizer, PunktSentenceTokenizer


sample_text = "sample_text.txt"


stop_words = set(stopwords.words('german'))
#stop_words


with open(sample_text):
    sample = sample_text.read()


#custom_sent_tokenizer = PunktSentenceTokenizer(sample_text)
