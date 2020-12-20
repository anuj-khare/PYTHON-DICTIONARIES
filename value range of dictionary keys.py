test_list = [{"gfg": 4, "is": 7, "best": 10}, 
             {"gfg": 2, "is": 5, "best": 9}, 
             {"gfg": 1, "is": 2, "best": 6}] 
keys = list(test_list[0].keys())
mydict = {key:[min(dictionary[key] for dictionary in test_list),max(dictionary[key] for dictionary in test_list)] for key in keys }
print(mydict)
