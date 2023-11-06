///#0. What function would you use to print the type of an object?///
x = [1, 2, 3]
print(type(x))

///#1. How do you get the variable identifier (which is the memory address in the CPython implementation)?
x = 'hello'
print(id(x))///

///#2. In the following code, do a and b point to the same object?
>>> a = 89
>>> b = 100///
#a and b are assigned to different integers

///#3. In the following code, do a and b point to the same object?
>>> a = 89
>>> b = 89///
#a and b do point to the same object

///#4. In the following code, do a and b point to the same object?
>>> a = 89
>>> b = a///
#a and b do point to the same object

///#5. In the following code, do a and b point to the same object?
>>> a = 89
>>> b = a + 1///
#a and b do not point to the same object

///#6. What does this print?
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)///
#This code will print True because s1 and s2 are two names pointing to the same string object "Best School".

///#7. What does this print?
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)///
#s1 is s2 will return True because they are indeed the same object.

///#8. What does this print?
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)///
#'True' because the values on either side are the same

///#9. What does this print?
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)///
#'True' because they are actually referring to the same string object

///#10. What does this  print?
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 == l2)///
#'True' because the objects referred to by the variables have the same contents

///#11. What does this print?
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 is l2)///
#'False' because l1 and l2 are lists with the same contents, they are two separate objects

///#12. What does this print?
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)///
#'True' because The '==' operator in Python checks for equality of the values

///#13. What does this print?
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)///
#'True' The 'is' operator in Python checks for identity, not equality

///#14. What does this print?
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)///
#'[1, 2, 3, 4]' because when l1.append(4) is called, the number 4 is appended to the list that l1 references

///#15. What does this print?
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)///
#'[1, 2, 3]' because 'l2' still references the original list, which has not been changed

///#16. What does this print?
def increment(n):
    n += 1
a = 1
increment(a)
print(a)///
#'1' because the function 'increment' is defined to take a parameter 'n' and then attempts to increment it by 1 using the '+=' operator

///#17. What does this print?
def increment(n):
    n.append(4)
l = [1, 2, 3]
increment(l)
print(l)///
#[1, 2, 3, 4] because the function 'increment' is defined to take a parameter 'n' and then appends the integer '4' to it and 'l' is set to [1, 2, 3]

///#18. What does this print?
def assign_value(n, v):
    n = v
l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)///
#[1, 2, 3] because the function 'assign_value' is defined to take two parameters, 'n' and 'v', and then assigns the value of 'v' to 'n' and passing the lists l1 and l2 into the function

///#19. What would these lines print?
>>> dict_ = {"WebDriver": "Camp"}
>>> dict_copy = dict_
print(dict_ == dict_copy)
print(dict_ is dict_copy)
>>> dict_copy = dict_.copy()
print(dict_ == dict_copy)
print(dict_ is dict_copy)///
#True
#True
#True
#False
#because the 'dict_' dictionary is created with a single key-value pair. 'dict_copy' is assigned to dict_, meaning both 'dict_' and 'dict_copy' now refer to the same dictionary object in memory.

///#20. Tuple or not?
a = ()///
#Yes, 'a = ()' is a tuple. In Python, parentheses '()' are used to denote a tuple, and having them empty means that 'a' is an empty tuple

///#21. Tuple or not?
a = (1, 2)///
#Yes, `a = (1, 2)` is a tuple in Python. A tuple is created by placing all the items (elements) inside parentheses `()`, separated by commas.

///#22. Tuple or not?
a = (1)///
#No, 'a = (1)' is not a tuple in Python. The parentheses around a single value do not create a tuple.

///#23. Tuple or not?
a = (1, )
b = 1,///
#Yes, both 'a = (1, )' and 'b = 1', are tuples in Python. Including a trailing comma in a set of parentheses indicates to Python that you have a tuple containing a single item.

///#24. What does this script print?
a = (1)
b = (1)
a is b///
#'True' because when you assign 'a = (1)' and 'b = (1)', what you're actually doing is assigning 'a' and 'b' as integers, not tuples, because there's no comma inside the parentheses.

///#25. What does this script print?
a = (1, 2)
b = (1, 2)///
#'True' if you have a line 'print(a == b)', because the two tuples a and b contain the same elements in the same order, making them equal

///#26. What does this print?
a = ()
b = ()
a is b///
#'True" because in Python, empty tuples are immutable and, as an optimization, Python doesn't create a new object every time an empty tuple is declared

///#27. What does this print?
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)///
#This will print a different id than 139926795932424. The reason for this is that lists in Python are mutable, which means they can be changed after they are created

///#28. What does this print?
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)///
#This will print 139926795932424.The reason for this is that the '+=' operator when used with lists, modifies the list in place