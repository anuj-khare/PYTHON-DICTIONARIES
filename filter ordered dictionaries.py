test_list = [{'gfg': 2, 'is': 8, 'good': 10}, 
             {'gfg': 1, 'for': 10, 'geeks': 9}, 
             {'love': 3, 'gfg': 4}] 
mylist = [elements for elements in test_list if sorted(elements.values()) == list(elements.values())]
print(mylist)
#There is however a better way to be dealing with these type of problems and that is using filter() but we'll see examples of that later on in this repo.
