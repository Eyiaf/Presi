import nltk

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

output = "Lemmatization is the process of reducing inflected forms of a word while ensuring that the reduced form belongs to a language."
# Create a string object. By default, the function breaks sentences by periods. 
# Customize text or read files as needed

# Create lemmatizer
lemmatizer = WordNetLemmatizer()

# Tokenize the text
words = word_tokenize(output)
stop_words = set(stopwords.words("english"))
list1 = []
punctuation =[',','.',"'"]
for token in words:
    if token not in stop_words and token not in punctuation:
        list1.append(token)

list2 = nltk.pos_tag(list1,"universal",'eng')
print(list2)
# Print lemmatized words
########to do: list2 second information needs to turn into corresponding tag for the lemmatization to call############
#for word in words:
    #print(lemmatizer.lemmatize(word))