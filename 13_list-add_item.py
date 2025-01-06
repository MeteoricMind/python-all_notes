##Append

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#--------------------------------------------

# insert

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#-----------------------------------------------

##  The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)