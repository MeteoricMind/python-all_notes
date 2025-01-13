# ##   ZIP()  ##
# #Way 2: Using zip(): zip() is used to combine 2 similar containers(list-list or dict-dict) printing the values sequentially. The loop exists only till the smaller container ends.

questions = ['name', 'colour', 'shape']
answers = ['apple', 'red', 'a circle']

for q,a in zip(questions,answers):
    print("Whats your {0}?\n I am {1}.".format(q,a))