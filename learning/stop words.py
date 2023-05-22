from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = "This is an example showing the Implimentation of stopwords in nltk corpus stuff"

stop_words = set(stopwords.words("english"))

words = word_tokenize(example_sent)

filtered_sent = [w for w in words if w not in stop_words]

print(filtered_sent)