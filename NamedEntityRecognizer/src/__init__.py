from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize


def splitIntoSentences(text):
    print ("splitIntoSentences, text \n", text)
    trimmedText = text.strip(' \n')
    sentences = sent_tokenize(trimmedText)
    print ("len", len(sentences))
    print (sentences)
    return sentences


def main():
    sentences = splitIntoSentences("""
    this is a simple sentence. this is a simple sentence1. 
    this is a simple sentence3
    """)

    for sent in sentences:
        words = word_tokenize(sent)
        print (words)

    # method1("""
    #     this's a sent tokenize test.
    #     """)


main()

