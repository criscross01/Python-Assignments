print("Hmmm... You have 5 tickets to that new movie everyone wants to see.\nWhom should you invite to go with you?")

friendList = []

for i in range(1,5):
    print("Enter the name of friend",i, ': ',end='')
    name = input()
    friendList.append(name)
    print("Your invite list now contains: ",friendList)
    
print("Great!  You are ready to go to the movie")