import nltk
import re
from nltk.corpus import gutenberg, stopwords
nltk.download('stopwords')
nltk.download('gutenberg')

def corpus_analysis(text_name):
    text_tokens = gutenberg.words(text_name)
    text_raw = gutenberg.raw(text_name)
    stop_words = set(stopwords.words('english'))

    print("Tokens", len(text_tokens))
    print("Types", len(set(text_tokens))) 
    print("Types excluding stop words:", len(set([word for word in text_tokens if word not in stop_words])))
    print("10 most common tokens:", nltk.FreqDist(text_tokens).most_common(10)) 
    print("Long words:", set(re.findall(r'[a-zA-Z]{14,}', text_raw)))
    print("Nouns ending in ’ation’:", set(re.findall(r'[a-zA-Z]+ation', text_raw))) 

corpus_analysis('austen-emma.txt')
