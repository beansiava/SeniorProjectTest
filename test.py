from textblob import TextBlob
opinion = TextBlob("EliteDataScience.com is dope. hate hate hate hate hate love love love lovely love")
#NOTE: the word tag affects the subjectivity, but not necessarily the polarity - lets check this
print(opinion.sentiment)
print(opinion.sentences) #Notice that TextBob will split everything up into sentences for me.
#print(opinion.words), gives the words    #I wonder if it will give me values for the individual sentences (not just the average)
#print(opinion.noun_phrases) gives the nouns in the text

#pulls the word tag from each word and prints it
for word, pos in opinion.tags:
    print(word, pos)
    #NN: noun
    #JJ: adjective
    #IN: preposition
    #VB_: verb (the _ gets replaced with various letters depending on the form of the verb)

#grab a word and pluralize it
from textblob import Word
w = Word("university")
print(w.pluralize())

#lemmatize the word (brings the word down to its most root form - ie. captures the essence of the word)
w = Word("octopus")
print(w.lemmatize())

#all items in the .word and .tags attributes are secretly of type Word
for word, pos in opinion.tags:
    if pos == 'NN':
        print(word.pluralize())
