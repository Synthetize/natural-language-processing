import nltk
from nltk.corpus.reader.tagged import TaggedCorpusReader
reader = TaggedCorpusReader('.', 'MIM-GOLD.sent', sep='/')
print("Number of sequences", len(reader.tagged_sents()))

#99 since array counts from 0
sentence = [word for word, tag in reader.tagged_sents()[99]]
print("Sentence no.100: ", sentence)

print("Number of tokens: ", len(reader.words()))
print("Number of types: ", len(set(reader.words())))


print("The 10 most frequent tokens:\n",nltk.FreqDist(reader.words()).most_common(10))

tags = [tags for word, tags in reader.tagged_words()]
print("The most 20 frequent PoS tags:\n", nltk.FreqDist(tags).most_common(20))

#range(len(tags)-1) bacause we are looking at pairs, so we stop one before the end otherwise it give an error
pairs = [(tags[i], tags[i+1]) for i in range(len(tags)-1) if tags[i] == 'AF']
pairs_dist = nltk.FreqDist(pairs).most_common(10)
pairs_formatted = [f"{pair[0][1]} => {pair[1]}" for pair in pairs_dist]
print("The 10 most frequent PoS tags following the tag ’af’:\n", pairs_formatted)





