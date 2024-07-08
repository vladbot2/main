# 1#
# list = (1, 2, [3, 4, 5])
# print("Original tuple:", list)

# list[2][0] = 9
# print("Modified tuple", list)


2#
# tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# numbers = tuple(num for num in tuple if num %2 == 0)
# print = tuple("Even numbers tuple")

3#
# five_elements_tuple = (1, 2, 3, 4, 5)
# first1, first2, * middle, last1, last2 = five_elements_tuple
# middle = middle[0]
# print("First two elements", first1, first2)
# print("Last two elements", last1, last2)
# print("Middle element as a list", [middle])


4#
# unsorted_tuple = (5, 3, 8, 1, 9, 2)
# sorted_tuple = tuple(sorted(unsorted_tuple))
# print = sorted("Sorted tuple")

5#
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# set1 = set(list1)
# set2 = set(list2)

# union = set1.union(set2)
# intersection = set1.intersection(set2)
# difference = set1.difference(set2)
# symmetric_difference = set1.symmetric_difference(set2)

# print= union("Union")
# print= intersection("Intersection")
# print = difference("Difference")
# print= symmetric_difference("Symmetric Difference")

6#
# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = (4, 5, 6, 7, 8)

# set1 = set(tuple1)
# set2 = set(tuple2)

# common_elements = set1.intersection(set2)
# common_tuple = tuple(common_elements)

# print = tuple("Common elements tuple")

7#
# numbers_list = [4, 2, 5, 2, 3, 1, 4, 5, 3]
# unique_sorted_tuple = tuple(sorted(set(numbers_list)))
# print = unique_sorted_tuple("Unique sorted tuple")

8#
# list_of_lists = [[1, 2, 3],[3, 4, 5],[5, 6, 7]]

# sets = [set(lst) for lst in list_of_lists]
# union_of_sets = set().union(*sets)

# print = union_of_sets("Union of all sets" )

9#
# import random

# random_tuples = [(random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)) for i in range(10)]
# unique_tuples_set = set(random_tuples)

# print=random_tuples("List of random tuples" )
# print=unique_tuples_set("Set of unique tuples")

10#
# numbers_tuple = (1, 2, 3, 4, 5)

# sum_of_elements = sum(numbers_tuple)
# product_of_elements = 1
# for num in numbers_tuple:
#     product_of_elements *= num
# average = sum_of_elements / len(numbers_tuple)

# print=sum_of_elements("Sum" )
# print=product_of_elements("Product")
# print=average("Average" )

11#
# nested_tuple = ((1, 2), (3, 4), (5, 6))

# first_element = nested_tuple[0][0]
# second_element = nested_tuple[0][1]
# third_element = nested_tuple[1][0]
# fourth_element = nested_tuple[1][1]

# print=first_element("First element")
# print=second_element("Second element")
# print=third_element("Third element")
# print=fourth_element("Fourth element")

12#
# from collections import Counter

# repeated_elements_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# elements_count = Counter(repeated_elements_list)
# most_common_elements = elements_count.most_common(1)

# print=most_common_elements("Most common elements")

13#
# list_of_lists = [[1, 2, 2, 3],[4, 5, 5, 6],[7, 8, 8, 9]]

# tuple_of_sets = tuple(set(lst) for lst in list_of_lists)

# print=tuple_of_sets("Tuple of sets")










