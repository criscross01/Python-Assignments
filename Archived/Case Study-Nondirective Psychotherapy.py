from random import randint

def getReply(statement):
    #Makes the statement lower case
    statement = statement.lower()
    #Changes first person to second person
    statement = statement.split()
    firstToSecond = {"i":"you","me":"you" ,"my":"your","mine":"yours"}
    for word in statement:
        if word in firstToSecond:
            index = statement.index(word)
            statement.remove(word)
            statement.insert(index,firstToSecond[word])
            
    statement = " ".join(statement)
    
    replyModifier = ["Why do you say that ", "Why do you think that ", "Why do you care that "]
    
    return replyModifier[randint(0,len(replyModifier))-1] + statement + "?"

def reply(statement):
    if randint(0,1) == 1:
        return getReply(statement)
    else:
        return "Please tell me more"

def main():
    print("Hello and welcome to Nondirective Phschotherapy!")
    while True:
        print()
        statement = input("What is bothering you?: ")
        print()
        if statement == "Quit":
            print("Goodbye")
            break
        print(reply(statement))
        
main()