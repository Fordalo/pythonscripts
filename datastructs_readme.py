
import adv_data_structts as DT

#list operations
#+++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++


# from re import X


# a = []

# for i in range(5):
#     a.append(i)
    
# a.pop()
    
# print(a)




#+++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++

#tuples
#written in c, are immutable but objects are mutible
#decleration of tuple

# list1 = ()
# list1 = 1,2,3
# print(list1)
# print(type(list1))

# x = [1,2,3,4,45]
# xtup = tuple(x)
# print(type(xtup), xtup)


#you can have a list within a ttuple that is mutable

#will say tuple does not support deletion
# y = (0,1,2,3)
# del(y[1])

#however if you have a list within a tuple, you can modify it

# y = ([2,3,4,5], 0, 6, 18)
# del(y[0][2])
# print(y)
#outtput: ([2, 3, 5], 0, 6, 18)

# y += (4,)
# print(y)
#outtput: ([2, 3, 5], 0, 6, 18, 4)


#+++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++
#sets: for non duplicate items
#sets: very fast access vs list
#uses a hash

# from joblib import PrintTime


# x_set = {3,5,3,5}
# print(type(x_set), x_set)
# #outtput: <class 'set'> {3, 5}

# #adding itemns to a set
# x_set.add(90)
# x_set.remove(3)
# print(x_set)
# #outtput: {90, 5}

# print(x_set.pop(), x_set)
# #outtput: 90 {5}

# print(0 in x_set)





#+++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++
#dictionaries



# x = {'pork' : 24.5, 'ass' : 45.6, 'beef' : 22.70}
# x['shrimp'] = 38.2
# print(x)
#output: {'pork': 24.5, 'ass': 45.6, 'beef': 22.7, 'shrimp': 38.2}
#x.keys
#x.values
#x.items

#print('beef' in x)

#iterating through dict

# for key in x:
#     print(key, x[key])
    
#output: pork 24.5
#ass 45.6
#beef 22.7
#shrimp 38.2



#+++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++
#list comprehension


# under10 = [x for x in range(10)]
# print(under10)
#output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# x = [2, 4, 5, 9,10, 17, 24, 456]

# xeven = [1 if i %2 ==0 else 0 for i in x ]
# print(xeven)
# #output: [1, 1, 0, 0, 1, 0, 1, 1]

# #we can pull put numbers into a new list as well
# xeven2 = [x for x in x if x%2 ==0]
# print(xeven2)
# #output: [2, 4, 10, 24, 456]


# y = [23.9, 4, 92, 'Lue', 'Ty', 34]
# y_num = [i for i in y if type(i) == int]
# print(y_num)
#output: [4, 92, 34]




#+++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++
#stacks

#python list are a very versitile data structure, they can be used to create stacks.
#firstt in First out

my_stack = list()
my_stack.append(4)
my_stack.append(4)
my_stack.append(8)
my_stack.append(9)
my_stack.append(10)

# print(my_stack)
# my_stack.pop()
# print(my_stack)

#output: [4, 4, 8, 9, 10]
#output: [4, 4, 8, 9]


#the pop functtion returns and value and removes it, but you can use peek to peek at the top of the stack
# print(my_stack.pop())
# print(my_stack)

#output: 9
#output: [4, 4, 8]






#+++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++
#Max Heap


#every node is greater than or equal to its parent
#binary tree ttructure


#                  20                         #
#                 /  \                        #
#                16   19                      #
#               /  \   /  \                   #
#              3    4  5   6                  #
###############################################

#Max Heap operations

#push (insert)
#--add value to end of array
#-- float it up to its proper position


#peek ( get max)
#-- returns heap[1]


#pop (remove max)
#--Move max to end of array
#--delete it 
#--Bubble down the item at index 1 to its proper position
#--return max 






#+++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++
#linked list
#each item in a linked list is a node
#each node is connected to the next node

#all linked list have a root and and end
#size number of nodes in list


#+++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++
#Double linked list

#has data, prev pointer, and next pointer














