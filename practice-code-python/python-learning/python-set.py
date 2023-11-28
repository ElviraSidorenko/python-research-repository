# - All elements in the set must be unique
# - Order does not matter in the set
# - Sets are not subscriptable (cannot get a specific element by its index)

# len function:
my_set = {1, 2, 3, 4, 5}
len(my_set)  # Out: 5

# Note that function len only counts unique values in the set:
new_set = {1, 1, 2, 2}
len(new_set)  # Out: 2

# Same goes for print:
set_to_print = {1, 1, 2, 2}
print(set_to_print)  # Out: {1, 2}


{1, 2, 3} == {3, 2, 1, 1, 1}  # True

# Adding to set:
mySet = {'a', 'b', 'c'}
mySet.add('d')
print(mySet)  # Out: {'a', 'b', 'c', 'd'}

# Check element in set:
mySet = {'a', 'b', 'c'}

'a' in mySet  # True

'z' in mySet  # False

# When all elements of a set A are present in a set B, we say that a set A is a subset of a set B.
friends = {'Ellie', 'Max', 'Connor', 'Bob'}
chat = {'Ellie', 'Bob'}

# To check whether a set is a subset of another, we use .issubset()
print(chat.issubset(friends))  # True


set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Union of sets (elements in either set1 or set2 or both)
union_set = set1.union(set2)
# Alternatively, you can use the pipe operator (|) for union
# union_set = set1 | set2
print("Union:", union_set)

# Intersection of sets (elements common to both set1 and set2)
intersection_set = set1.intersection(set2)
# Alternatively, you can use the ampersand operator (&) for intersection
# intersection_set = set1 & set2
print("Intersection:", intersection_set)

# Difference of sets (elements in set1 but not in set2)
difference_set1 = set1.difference(set2)
# Alternatively, you can use the minus operator (-) for difference
# difference_set1 = set1 - set2
print("Difference (set1 - set2):", difference_set1)

# Difference of sets (elements in set2 but not in set1)
difference_set2 = set2.difference(set1)
# Alternatively, you can use the minus operator (-) for difference
# difference_set2 = set2 - set1
print("Difference (set2 - set1):", difference_set2)
