from functools import reduce

strList = ["word1","word2"]

product = reduce((lambda x,y: x + y),strList)

print(product)