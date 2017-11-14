from random import randint

def randomArticle():
    articles = ['a','the']
    return articles[randint(0,len(articles)-1)]

def randomNoun():
    nouns = ['boy','girl', 'pizza', 'baseball', 'bat']
    return nouns[randint(0,len(nouns)-1)]

def randomVerb():
    verbs = ['ate', 'hit', 'ran']
    return verbs[randint(0,len(verbs)-1)]

def randomPrep():
    prepositions = ['to','with']
    return prepositions[randint(0, len(prepositions)-1)]

def prepPhrase():
    return randomPrep() + ' ' + nounPhrase()
    
def nounPhrase():
    return randomArticle() + ' ' + randomNoun()

def verbPhrase():
    return randomVerb() + ' ' + nounPhrase() + ' ' + prepPhrase()


def sentenceGenerator():
    return nounPhrase() + ' ' + verbPhrase()

def main():
    num = eval(input("Enter the amount of sentences you want to generate: "))
    for i in range(num):
        print(sentenceGenerator())

main()