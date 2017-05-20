# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---
### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Tuples are immutable, meaning they can't be edited. Lists can be edited. 

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

["Johanna", "Nick", "Patrick", "Cloud"] is an example of a list.  Lists are ordered.
{"Johanna", "Nick", "Patrick", "Cloud"} is an example of a set. Sets are unordered, just like dictionaries.
Sets kind of look like dictionaries, just without keys. Sets are required to be hashable.

Lists and sets both contain values. 

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is another way of writing a function. 

Here's a function for squaring a number:

def square(num):
  num ** 2
  
print square(3)
9

Here's the same function using lambda instead. 

square = lambda num: num ** 2
print square(3)
9

---

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

Most of the time we create a list, edit the output one by one, and then append it to a new list.
Like this:

items = [1,2,3,4,5]
squared = []
for item in items:
  squared.append(item ** 2)
  
Map allows us to do this in a much simpler way.

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  
from datetime import date

d0 = date(2013, 1, 2)
d1 = date(2015, 7, 28)
delta = d0 - d1
print(delta.days)

-207

So 207 days.

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  

import datetime import date

d0 = date(2013, 12, 31)
d1 = date(2015, 5, 28)
delta = d0 - d1
print(delta.days)

-517

So 517 days. 
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
-7850

So 7850 days. 
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





