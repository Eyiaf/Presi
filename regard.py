import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

output = ("Lemmatization is the process of reducing inflected forms of a word while ensuring that the reduced form belongs to a language.")
with open("AliceInWonderland.txt") as file:
    output = [line.rstrip() for line in file]
output = " ".join(output[23:28])

lemmatizer = WordNetLemmatizer()

pos = {
    **dict.fromkeys(["NN","NNP","NNS","PRP","PRP$","WP"],"n"),
    **dict.fromkeys(["VB","VBD","VBG","VBN","VBP","VBZ","WRB"],"v"),
    **dict.fromkeys(["JJ","JJR","JJS"],"a"),
    **dict.fromkeys(["RB","RBR","RBS","WRB"],"r"),
}

pos_list = []
words = word_tokenize(output)

POS = nltk.pos_tag(words)

for x in range(len(POS)):
    try:
        pos_list.append([POS[x][0],pos[POS[x][1]]])
    except:
        pos_list.append([POS[x][0],"n"])

lemmatized = []
for x in range(len(pos_list)):
    lemmatized.append(lemmatizer.lemmatize(pos_list[x][0],pos_list[x][1]))
print(POS)


