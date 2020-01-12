from sklearn.feature_extraction.text import CountVectorizer

sentences = ['John likes ice cream', 'John hates choclate.']

vectorizer = CountVectorizer(min_df=0, lowercase=False)
vectorizer.fit(sentences)
print1 = vectorizer.vocabulary_

print(print1)

print2 = vectorizer.transform(sentences).toarray()
print(print2)
