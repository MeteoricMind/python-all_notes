## The remove() method removes the specified item.

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#------------------------------------------------

## The pop() method removes the specified index.

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
##         pop() will only remove last item
#----------------------------------------------------

##     The del keyword also removes the specified index:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#------------------------------------------------------


# The clear() method empties the list.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)