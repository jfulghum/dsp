"""
Given a list of strings, return the count of the number of strings
where the string length is 2 or more and the first and last chars
of the string are the same.
"""

def match_ends(words):
    

print(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']) == 3)
print(match_ends(['', 'x', 'xy', 'xyx', 'xx']) == 2)
print(match_ends(['aaa', 'be', 'abc', 'hello']) == 1)

"""
Given a list of strings, return a list with the strings in sorted
order, except group all the strings that begin with 'x' first.
e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].
"""

print(def front_x(words):

print(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']) == ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
print(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']) == ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']) == ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])



"""
Given a list of strings, return a list with the strings in sorted
order, except group all the strings that begin with 'x' first.
e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].
"""

def sort_last(tuples):
    
    

print(sort_last([(1, 3), (3, 2), (2, 1)]) ==  [(2, 1), (3, 2), (1, 3)])
print(sort_last([(2, 3), (1, 2), (3, 1)]) == [(3, 1), (1, 2), (2, 3)])
print(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)] == [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


"""
Given a list of numbers, return a list where all adjacent equal
elements have been reduced to a single element, so [1, 2, 2, 3]
returns [1, 2, 3]. You may create a new list or modify the passed
in list.
"""
    
def remove_adjacent(nums):
    
print(remove_adjacent([1, 2, 2, 3]) == [1, 2, 3])
print(remove_adjacent([2, 2, 3, 3, 3]) == [2, 3])
print(remove_adjacent([3, 2, 3, 3, 3]) == [3, 2, 3])
print(remove_adjacent([]))

"""
Given two lists sorted in increasing order, create and return a
merged list of all the elements in sorted order. You may modify
the passed in lists. Ideally, the solution should work in "linear"
time, making a single pass of both lists.
"""

def linear_merge(list1, list2):
    
print(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']) == ['aa', 'bb', 'cc', 'xx', 'zz'])
print(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']) == ['aa', 'bb', 'cc', 'xx', 'zz'])
print(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']) == ['aa', 'aa', 'aa', 'bb', 'bb'])

