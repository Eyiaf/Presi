import nltk
from nltk.tokenize import word_tokenize
from nltk.tree import Tree
from IPython.display import display

output = ("Apple's name was inspired by Steve Jobs' visits. His visits was to an apple farm while on a fruitarian diet.")
# Create a string object. By default, the function breaks sentences by periods. 
# Customize text or read files as needed

# Tokenize the text
words = word_tokenize(output)

# POS tag the text
tag = nltk.pos_tag(words)

grammar = "NP: {<DT>*<JJ>*<NN>}"
#grammar = """Chunk: }<JJ>{"""


# Create chunk parser object
chunk_parser = nltk.RegexpParser(grammar)


# Create a tree diagram for the chunking
tree = chunk_parser.parse(tag)
display(tree)