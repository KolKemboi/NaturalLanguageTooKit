import sys
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer 

ps = PorterStemmer()

example = ["python", "pythonly", "pythonista", "pythonic", "pythoned"]
statement = "If you really, really love tell me now, Cause I know i wont be there for all eternity, but for now I will stay with you "

stemmed = [ps.stem(word) for word in example]
stems = [ps.stem(word) for word in statement.split(" ")]

print(*stemmed, sep=' ', end='\n', file=sys.stdout)
print(*stems, sep=' ', end='\n', file=sys.stdout)