import PyPDF2
import textblob
import nltk
from collections import Counter
import re



pdfo = open("HerminioVazquez_CV.pdf", "rb")
pdfr = PyPDF2.PdfFileReader(pdfo)

all = "\n".join([re.sub('[^a-zA-Z0-9\n\.]',' ', pdfr.getPage(x).extractText()) for x in range(pdfr.getNumPages())])

blob = textblob.TextBlob(all)

stemmer = nltk.stem.WordNetLemmatizer()

# Sentences (blob): 35
print("Sentences:", len(blob.sentences))

# Words: (blob.words): 1617
print("Words:", len(blob.words))

# Tokens: (blob.tokenize()): 2113
print("Tokens:", len(blob.tokens))

# Verbs
verbs = [k.lower() for k,v in blob.tags if v.startswith("V")]
print("Verbs:", len(verbs))

lemmatized = []
for v in verbs:
    lemmatized.append(stemmer.lemmatize(v, 'v'))


print(Counter(lemmatized))
print(Counter(verbs))
# Subjectivity
print(f'Subjectivity: {round(blob.subjectivity*100,2)}%')
print(f'Objectivity: {100-round(blob.subjectivity*100,2)}%')

# Sentiment
print(blob.sentiment)
