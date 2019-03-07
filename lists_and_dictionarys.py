"""
introduction/recap
"""
a = 1
b = 1.5
c = "string"
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
"""
soft start lists
"""
some_list = [1,4,12,413,123,18,43]
print(type(some_list))
print(some_list)
another_list = ["VW","BMW","Mercedes"]
print(type(another_list))
print(another_list)
another_another_list = [1,4,"VW",True,"BMW",2.1,"Mercedes"]
print(type(another_another_list))
print(another_another_list)

"""
List and tuples
"""
fruitlist = ["apple","banana","cherry"] #list
print("length of fruitlist is " + str(len(fruitlist)))
print(fruitlist)
print(fruitlist[0])
"""
rape of a for loop
"""
for i in range(len(fruitlist)):
    print("index is "+str(i))
    if fruitlist[i]=="banana":
        print(fruitlist[i])

fruitlist[2] = "orange"
print(fruitlist)

vegetabletuple = ("carrot","avocado","tomato") #tuple
print(vegetabletuple)
print(vegetabletuple[1])
#vegetabletuple[2] = "potato" # notcahngeable

"""
loop through an list
"""
for i in fruitlist:
    print(i)

"""
Check if Item Exists
"""
if "apple" in fruitlist:
    print("Yes apple in fruitlist")

"""
add / insert element in a list
"""
fruitlist.append("maracuja") #add an element
print(fruitlist)
fruitlist.insert(2,"pineapple") #insert element before orange
print(fruitlist)
fruitlist.remove("maracuja") #remove an element
print(fruitlist)
fruitlist.pop(0) #if its unindexed it will remove the last one. here remove the apple
print(fruitlist)
del fruitlist[0] #remove the first element in the list (index is 0)
print(fruitlist)
fruitlist.clear()
print(fruitlist)

print(some_list) #unsorted list
some_list.sort() #sort the list
print(some_list) #sorted list

"""
dictionary
"""

thisdict =	{
  "brand": "Aston Martin", #brand is the key and aston martin is the value
  "model": "DB11",
  "year": 2018
}
print(thisdict)
x = thisdict["model"] #model is the key
print(x)
print(thisdict.get("model")) #"same" as above
thisdict["year"] = 2019
print(thisdict)
print(thisdict.keys())
print(thisdict.values())
if "model" in thisdict:
  print("Yes, 'model' is a key in the dictionary (thisdict)")

#add items
thisdict["color"] = "blue"
print(thisdict)
