my_list = []
#Appendind values
my_list.append (10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#inserting at the 2nd position
my_list.insert(1, 15)

#extendin the List
my_list.extend([50, 60, 70])

#Removing the last element
my_list.pop()

#sorting in ascending order.
my_list.sort()

#printing the index of the value 30

index_of_30 = my_list.index(30)
print(index_of_30)
print(my_list)