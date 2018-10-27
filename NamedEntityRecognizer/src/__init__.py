from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize


def splitIntoSentences(text):
    # print ("splitIntoSentences, text \n", text)
    trimmedText = text.strip(' \n\t')
    sentences = sent_tokenize(trimmedText)
    print ("len", len(sentences))
    # print (sentences)
    return sentences


def main():
    # sentences = splitIntoSentences("""
    # this is a simple sentence. this is a simple sentence1.
    # this is a simple sentence3
    # """)

    sentences = splitIntoSentences("""
    people with bad audio quality have defective phones . 
    i have read a lot of the reviews and my phone does not have a hiss or anything that people are talking about . 
    sound quality[+3][u]##it is crystal clear . 
    this is one of the nicest phones nokia has made . 
    i do recommend getting the data kit for those geeks . 
    there are a lot of cool websites with games and midi ringtones to download for free .
     
    t-mobile ruins an otherwise good phone. nokia makes a great phone, that's clear. with all its complicated features, the menus are easily accessible and the quality of the features is great. the one huge disappointment is that the phones manufactured for t-mobile lack many of the menus and functions that a nokia straight from the manufacturer should have. 
    one of the things t-mobile brags about is the fact that it's a " worldphone " and can be used in europe, etc. 
    yet they've gotten rid of most of the languages that should be in the phone, including italian, german, and dutch. the internet functions of the phone - wap and gprs - will only work through t-mobile's services, because they have deleted the menu options that would enable you to configure the phone to be used on a different network. therefore, if you wanted to travel abroad and pop in a local sim card, even if you unlock the phone, there is no way you can use the local wap browser or internet. 
    after spending hours being transferred from one tech help person to another, i got fed up and have decided to return the phone. 
    bottom line, if you're attracted to this phone because of its tri-band feature so you can take it abroad, forget it. find another phone, or buy this one in its manufacturer-unlocked form. 
    """)

    for sent in sentences:
        words = word_tokenize(sent)
        print (words)



    # method1("""
    #     this's a sent tokenize test.
    #     """)


main()

