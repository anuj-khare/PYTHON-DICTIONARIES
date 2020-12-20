words = input().lower().split()
keys = [word[0] for word in words]
mydict = {word[0]:[values for values in words if values[0] == word[0]] for word in words}
print(mydict)
