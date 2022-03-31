import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't eat cardboard"""
tokenized_word=word_tokenize(text)
print(tokenized_word)
stop_words=set(stopwords.words("english"))
print(stop_words)
filtered_word=[]
for w in tokenized_word:
    if w not in stop_words:
        filtered_word.append(w)

print("Tokenized Sentence:",tokenized_word)
print("Filterd Sentence:",filtered_word)
ps = PorterStemmer()
stemmed_words=[]
for w in filtered_word:
    stemmed_words.append(ps.stem(w))
print("Filtered Sentence:",filtered_word)
print("Stemmed Sentence:",stemmed_words)
lem = WordNetLemmatizer()
stem = PorterStemmer()
word = "flying"
print("Lemmatized Word:",lem.lemmatize(word,"v"))
print("Stemmed Word:",stem.stem(word))
