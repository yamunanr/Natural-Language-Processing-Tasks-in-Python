import nltk
nltk.download('punkt')
nltk.download('stopwords')
import sys
import sklearn

print('Python: {}' .format(sys.version))

from nltk.tokenize import sent_tokenize, word_tokenize

text = 'Hello students, how are you doing today? The olympics are inspiring, and Python is awesome, You look grat today.'

#sentence tokenization
print('Sentence Tokenization result')
print(sent_tokenize(text))
#word tokenization
print('words Tokenization result')
print(word_tokenize(text))


# removing stop words -useless data
from nltk.corpus import stopwords
print('Removing the stop word result')
print(set(stopwords.words('english')))

example = 'This is some sample text, showing off the stop words filteration.'

stop_words =set(stopwords.words('english'))

word_tokens = word_tokenize(example)

sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

        print(word_tokens)
        print(sentence)
        print(filtered_sentence)

#stemming using NLTK
from nltk.stem import PorterStemmer

ps = PorterStemmer()

example_words = ['ride', 'riding', 'rider', 'rides', 'argumentation', 'specification', "ponies"]

for w in example_words:
    print(ps.stem(w))

#Stemming entire sentence
new_text = 'When riders are riding their horses, they often think of how cowboys rode horses.'

words = word_tokenize(new_text)
print('Stemming entire sentence')
for w in words:

    print(ps.stem(w))

    


