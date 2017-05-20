# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

"""
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.
    """
def donuts(count):
    if count < 10:
        return "Number of donuts: {}".format(count)
    else:
        return "Number of donuts: many"
        
        
print(donuts(4) == 'Number of donuts: 4')
print(donuts(9) == 'Number of donuts: 9')
print(donuts(10) == 'Number of donuts: many')
print(donuts(99) == 'Number of donuts: many')


"""
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.
"""



def both_ends(s):
    if len(s) < 2:
        return ""
    else:
        return s[:2] + s[-2:]
        
    

print(both_ends('spring') == 'spng')
print(both_ends('Hello') == 'Helo')
print(both_ends('a') == '')
print(both_ends('xyz') == 'xyyz')


"""
Given a string s, return a string where all occurences of its
first char have been changed to '*', except do not change the
first char itself. e.g. 'babble' yields 'ba**le' Assume that the
string is length 1 or more.
"""

def fix_start(s):
    i = 1
    s = list(s)
    while i < len(s):
        if s[i] == s[0]:
            s[i] = "*"
        i += 1
    return "".join(s)

print(fix_start('babble') =='ba**le')
print(fix_start('aardvark') == 'a*rdv*rk')
print(fix_start('google') == 'goo*le')
print(fix_start('donut') == 'donut')



"""
Given strings a and b, return a single string with a and b
separated by a space '<a> <b>', except swap the first 2 chars of
each string. Assume a and b are length 2 or more.
"""

def mix_up(a, b):
    a = list(a)
    b = list(b)
    a[:2] = b[:2]
    b[:2] = a[:2]
    return a + " " + "b"
    

print(mix_up('dog', 'dinner') == 'dig donner')
print(mix_up('gnash', 'sport') == 'spash gnort')
print(mix_up('pezzy', 'firm') == 'fizzy perm')


"""
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.
"""

def verbing(s):
    if len(s) > 3 and s[-3:] != "ing":
        return s + 'ing'
    elif len(s) < 3:
        return s
    else:
        return s + 'ly'
    

print(verbing('hail') == 'hailing')
print(verbing('swiming') == 'swimingly')
print(verbing('do') == 'do')

"""
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'
"""

def not_bad(s):
    notv = s.find("not")
    badv = s.find("bad")
    if (badv > notv): #if bad is after not. if bad index is larger than not index.
        return s[:notv] + "good" + s[(badv+3):]
    else:
        return s
    
    
print(not_bad('This movie is not so bad') == 'This movie is good')
print(not_bad('This dinner is not that bad!') == 'This dinner is good!')
print(not_bad('This tea is not hot') == 'This tea is not hot')
print(not_bad("It's bad yet not") == "It's bad yet not")

# Consider dividing a string into two halves. If the length is even,
# the front and back halves are the same length. If the length is
# odd, we'll say that the extra char goes in the front half. e.g.
# 'abcde', the front half is 'abc', the back half 'de'. Given 2
# strings, a and b, return a string of the form a-front + b-front +
# a-back + b-back
# """

def front_back(a, b):
    aV= len(a)/2 + (len(a) % 2)
    bV= len(b)/2 + (len(b) % 2)
    return a[:aV] + b[:bV] + a[aV:] + b[bV:]
    
print(front_back('abcd', 'xy') == 'abxcdy')
print(front_back('abcde', 'xyz') == 'abcxydez')
print(front_back('Kitten', 'Donut') == 'KitDontenut')

