## How a python program runs ?
- Program.py (source code) -> Compiler -> Program.pyc (ByteCode) -> Interpreter -> Converts to Machine Code -> Python Virtual Machine
- Having the source code converted into ByteCode(error free code) reduces the burden on Interpreter.
- Python Platform Independent/Portable
- Same file .pyc can be run on various operating system if PVM is availaible.

## Features of Python
- Simple/Expressive
- Easy to learn
- Scripting Language
- Open Source
- Platform Independent
- Procedural & Object Oriented
- Huge library
- Embeddable
- Scalable

## Variables
- Declaration and initialization is done together.
- Variables do not have specific data type , it's type depends on the value assigned to it.
- type(x) -> <class 'str'>

### Rules for Declaring a variable name
- Name can contains alpha-numeric characters & underscore.
- Name should start with a letter or underscore character.
- Variables are case-sensitive.

## Python Data Types
<img src="./img/python-data-types.png" alt="python-data-types">

- Numeric DataTypes
    - There is no size limit or there is no range for integer, like how we have for other languages like c++.
    - There is no fixed size memory taken by any data type in Python.
    - eg: 12.5 can be represented as 125E-1
- Bool
    - In case of true t should be capital in case of false f should be capital.
    - true represents numeric value 1 whereas false represent numeric value 0.
- Complex
    - eg 4 + 5j can be represented as complex(4, 5)

## Base - conversion
- bin()
- oct()
- hex()
```
eg: a = 10
bin(a) => '0b1010'
```

## Type Conversion
- converting data type from one to another.
 - int()
 - float()
 - complex()
 - bool()
 - str()
 <img src="./img/type-conversion.png" alt="type-conversion">

## is or is not operator
- They will check whether both the variabes are holding onto the same memory.
```
eg: 
a = 10
b = 10
res = a is b //True
```

## range
- range(start, end, step)
- range goes from start to end-1 and steps according to step

## Match Case
- works like if else
```
day = int(input("Enter day number"))
match day:
    case 1:
        print("Sunday")
    case 2: 
        print("monday")
    case _:
        print("holiday")
```

## String and Its Methods
- s1 = [ h  e  l  l  o]
- s1 = [h (0) , e (1), l(2), l(3), 0(4)]
- s1 = [h (-5) , e (-4), l(-3), l(-2), 0(-1)]
- s1 typeof(s1) => ```<class 'str'>```
- len : gives len of a string
- s1 = "john's"

### Operators on String
- 1. concatentation
    ```
        s1 = "hello"
        s2 = " world"
        s3 = s1 + s2 //"hello world"
    ```
- 2. Repetition
    ```
        s1 = "hello"
        s1 = s1 * 2 //"hello hello"
    ```
- 3. Indexing
    - In string index can be done from behind as well -1, -2, ... so on
    ```
    s1 = "hello world"
    for i in range(0, len(s1)):
        print(s1[i])
    ```
- 4. Slicing Operator: ```s1[start:end:step]```

    ```
    s2[::-1] //elloh
    ```
- 5. in (checks whether string is member in string of s1)
```eg : 'h' in s1```

- 6. not in
```eg: 'he' not in s1```

### String Methods: find() and index()
- For any class in python to know its definition you can call eg: ```dir(str) or dir(list)```
- It returns or shows all methods availaible in the class
```
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', 
'__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', 
'__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', 
'__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 
'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 
'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 
'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 
'swapcase', 'title', 'translate', 'upper', 'zfill']
```
- help(s.capitalize) -> returns the documenatation of the method of class
- string object is stored like an array of characters.
- ```s.find(sub[, start[, end]])``` (things in square brackets are optionals)
    - if string not found it returns -1
- s.find returns -1 if string not found , whereas s.index throws exception
```
>>> s.find('k')
-1
>>> s.index('k')
Traceback (most recent call last):
  File "<python-input-12>", line 1, in <module>
    s.index('k')
    ~~~~~~~^^^^^
ValueError: substring not found
```
- ```s.rfind(sub[, start, end]])```
- ```s.index(sub[, start, end]])```
- ```s.rindex(sub[, start, end]])```
- ```s.count(sub[, start, end]])```


## String Method: Removing spaces
- since string is immutable so it returns a new string
- ```s.ljust(width, [fill])```
- ```s.rjust(width, [fill])```
- ```s.center(width, [fill])```
- justifies spaces according to width, and fill is optional for filling certain characters
- eg:
```
>>> res = s.rjust(7, '$')
>>> res
'$$$ho1o'
>>> s (string s remains same)
'ho1o'
```

- ```s.strip([chars])```
- ```s.lstrip([chars])```
- ```s.rstrip([chars])```

## String Method: Changing cases
- ``` s.capitalize()```
- ``` s.lower()```
- ``` s.upper()```
- ``` s.title()```
- ``` s.swapcase()```
- ``` s.casefold()```

## String method: Inquiry Methods

## Formatted Printing
- You can avoid moving to the next line by writing end with empty string eg: `print('abc', end='')`
- whenever print method prints something it moves cursor to the next line.
- `print(object, [sep= , end= , file=sys.stdout ,flush=False]`
```
>>> a = 'nitin'
>>> b = 'delhi'
>>> print(a, b, sep='~')
nitin~delhi
```
- By default sep is a space and end is a new-line.

## C Style formatting
- Use % and then (variable names)
```
>>> name = 'nitin'
>>> age = 25
>>> city = 'delhi'
>>> interest = 5.2
>>> print('user %s age %d living in %s has interest of %f' %(name, age, city, interest))
user nitin age 25 living in delhi has interest of 5.200000
```
- %s string
- %d decimal
- %f float
- %n integer

## Formatted Printing
- Flower brackets are placeholder , and the value that I have written inside them is index. eg: `print('Division of {0} and {1}  is {2}'.format(a, b, c))`
```
>>> a = 30
>>> b = 5
>>> c = 6
>>> print('Division of {0} by {1} is {2}'.format(a, b, c))
Division of 30 by 5 is 6
```


## List
-  List is a collection of heterogeneous objects, & is immutable.
### Indexing and Slicing
- `index [], slice[:], +, *,  in , not in`
- slicing : [start: end: step]

### Iterating a list
- for loop
```
for x in list1
    print(x)
```
- for loop in range
```
for i in range(len(list)):
    print(list[i])
```
- while loop
```
while i < len(list1):
    print(list1[i])
```

### List Methods : Adding elements
- `append(), extend(iterable), insert(idx, ele), copy()`
- `l1.append(10)`
- `eg: l1.extend([120, 121, 209])`
- `eg: l1.insert(3, 10)`
- `eg; insert using slice `l1[4:4] = [22]`
```
- it creates a shallow copy
eg: copy => l2 = l1.copy()
>>> l2 = l1.copy()
>>> id(l2)
4375327488
>>> id(l1)
4375327808
```
### List Methods : Removing elements
- `pop(), remove(element), clear()`
```
>>> l1 = [1,2, 4]
>>> l1.pop()
4
>>> l1
[1, 2]
>>>
```
- del
```
>>> l1 = [1, 2, 3, 4]
>>> del l1[0:2]
>>> l1
[3, 4]
>>>
```
## List Methods : index,count, reverse, sort
- `index(x, [start, [, end]])`
- l1 = [5, 6, 7, 5, 8, 9, 6, 10, 6]
- l1.index(8) => 4
- throws error if value not found
```
>>> l1.index(55, 1, 4)
Traceback (most recent call last):
  File "<python-input-15>", line 1, in <module>
    l1.index(55, 1, 4)
    ~~~~~~~~^^^^^^^^^^
ValueError: 55 is not in list
```
- `sort(*, key = None, reverse = False)`
- `l1.sort()` sorts the same list
- `l1.sort(reverse = True)`
- `l1.sort(key=str.lower)` : all should be converted in lower and then sorted

## List Comprehensions
- `L1 = [expression for item in range]`
- eg:
      - l1 = [x for x in range(10)]
      - l2 = [x**2 for x in range(1, 6)]
      - l3 = [x for x in (10,5 ,6, 7, 8) if x%2 == 0]
      - l3 = [x.lower() for x in 'Python']

## Nested List
- accessing a nested list `list[2][0]`
- list = [10, 20, ['a', 'b'], 30, 40]

## Tuples
- Tuple is similar to list and is a collection of values and is `immutable`.
`tuple = ('jack', 45, 48.6, false, 'jill')`
- it can contain duplicate elements
- we cannot append or modify the values.
- unpacking tuple ` a, b, c, d = t1`

### tuple comprehensions and methods
`count(value)` : used to return the no of occurence of value         <br/>
`index()` : returns the index of the value

### tuple operators
```
for i in t1:
         print(i)

for i in range(len(t1)):
        print(t1[i])
```
`index[], slice[:], concatenate +, repeat *, membership (in), not in`

## Sets
- It is unordered collection of different heterogeneous elements, it is mutable.
- `List [], Tuple (),  Set {}`
- It doesn't store duplicate elements.
`s1 = {45, 'nitin', 'hello', 21}`
```
>>> s2 = set((1, 2, 3, 4, 4))
>>> s2
{1, 2, 3, 4}
```
- We can remove or insert more values (i.e mutable)
- `s1.discard(50)`
- `s1.add(10)`
 
### Set Methods: Adding and Deleting
- add()
- copy()
- pop() : removes some random element from set
- discard(ele) : removes required element from set, doesnt throw error even if ele already removed
- remove(ele): removes ele from set , but it would give an error
- clear(): clear all the content of sets

### Set Comprehensions
- simple and easy way of creating sets from other iterables :  `S = { expression for item in iterable}`
- S = set()
- s1 = { x for x in range(10)}
- s2 = {x**2 for x in [-1, 0, 1, 2]}
- s2 = { x for x in (10, 5, 7, 8) if x%2 == 0}
- s2 = { x.upper() for x in 'nitin'}

## Dictionary
`{key:value, key2:value2, .....}`
- dict1 = {'name': 'nitin', 'age':25}
- to get a value for a particular key `dict1['name']`
- for key we can only takes those types which are immutable.(we cannot take list and set as key as they are mutable)
- for data we can take any data type.
- if we given an existing key, then its get updated & if give a new key then the new value is inserted.
- d2 = dict() or d2 = {} -> creates an empty dictionary
```
>>> for x in range(1,6):
...     d2[x] = x**2
...     
>>> d2
{'name': 'nk', 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```
- this is the 2nd Method of creating dictionary : `dict((iterable pairs))`
```
>>> l1 = ([1, 11], [2, 22], [3, 33])
>>> type(l1)
<class 'tuple'>
>>> d2 = dict(l1)
>>> d2
{1: 11, 2: 22, 3: 33}
```
- 3rd method : dict(zip(iterable, iterable))
  - zip will combine these two by taking corresponding element at corresponding positions and bearing them.
  ```
        >>> l1 = ['a', 'b', 'c']
        >>> type(l1)
        <class 'list'>
        >>> l2 = ['apple', 'bnana', 'cherry']
        >>> type(l2)
        <class 'list'>
        >>> dict3 = dict(zip(l1, l2))
        >>> dict3
        {'a': 'apple', 'b': 'bnana', 'c': 'cherry'}
  ```
  - if one iterable has extra values that will be ignored it will only contruct key value pair until it can match as a pair

- 4th : dict(enumerate(iterable))
    - Enumeration gives numbers to items in the list and it is giving a tuple.
    ```
    >>> l1 = ['A', 'B', 'C']
    >>> for item in enumerate(l1):
    ...     print(item)
    ...     
    (0, 'A')
    (1, 'B')
    (2, 'C')

    >>> dict4 = dict(enumerate(l1))
    >>> dict4
    {0: 'A', 1: 'B', 2: 'C'}
    ```

- method 5: dict{exp: exp for item in iterable}
```
    >>> dict1 = {x:x**2 for x in range(1, 5)}
    >>> dict1
    {1: 1, 2: 4, 3: 9, 4: 16}
```
- method 6 : without colon similar to method 5
    - `dict1 = dict((x,x**2) for x in range(1, 5))`

- method 7 : `{x:y for x, y in zip(L1, L2)}`
- method 8: same as method 4
    - we can use `{item for item in enumerate(iterable)}`
    - eg:
       ```
            >>> L2 = [1, 2, 3]
            >>> dict1 = {x:y for x,y in enumerate(L2)}
            >>> dict1
            {0: 1, 1: 2, 2: 3}
        ```

## Looping over Dictionary
1. `get(key, value)`
```
for x in dict1:
    print(x, dict1[x])
```
- using subscript can throw error if key not present `dict1[101]` and using `get` doesnt throw error `dict1.get(101)`

2. `keys()`
    - Gives all the keys in form of a list
        ```
    >>> dict1
    {0: 1, 1: 2, 2: 3}
    >>> e = dict1.keys()
    >>> e
    dict_keys([0, 1, 2])
    >>> type(e)
    <class 'dict_keys'>
    
    for k in dict1.keys():
        print(k, dict1[key])
    ```

4. `values()` : Gives all the values in form of a list
5. `items()`
```
>>> for x, y in dict1.items():
...     print(x,y)
...     
0 1
1 2
2 3
```
## Dictionary Methods
`copy, update(iterable) , setdefault(key, default), fromkeys(sequence, value), pop(), popitem(), clear()`
- update : method can be used to update the existing dictionary to include more key-value pairs
```
>>> dict1
{0: 1, 1: 88, 2: 3}
>>> dict1.update({4:88, 5:99})
>>> dict1
{0: 1, 1: 88, 2: 3, 4: 88, 5: 99}
```
- setdefault
  - It adds the key with value None if not present already in dict.
  - You can also set some required value `dict1.setdefault(110, 'adv')`
```
>>> dict1
{0: 1, 1: 88, 2: 3, 4: 88, 5: 99}
>>> dict1.get(88)
>>> dict1.setdefault(88)
>>> dict1
{0: 1, 1: 88, 2: 3, 4: 88, 5: 99, 88: None}
```
- fromKeys(sequence, value)
    ```
    >>> dict1.fromkeys(l2, 'some-value')
    {55: 'some-value', 66: 'some-value', 77: 'some-value'}
    ```
    - it takes keys from sequence and adds the same value for all the keys

- pop() : removes the key and value, if key not present throws error
    - if you think value might/might not be present then:
        - `dict1.pop(101, 'None')` then the value `None` will be returned(the value you have passed)

- popitem(): pops out the last item, `>>> dict1.popitem() => (11, None)`

 
## Functions
```
def name(<parameter list>) :
    return None
```
- By default function returns None if nothing is returned.

### Positional vs Keyword arguments
- By default it uses positional arguments
- the positional arguments have to be passed in order.
- Keyword arguments:
    - `n = net_sal(deduction=2000, basic=800, allowance=600)`
    - in this method , I should know the exact name of formal parameters
    - if trying mix of both positional and keyword then pass positional first & then keyword

### default arguments
- default should be on the right side
- keywords should be on the right(positional should be first, and then default args)
```python
def add(a, b=0, c=0):
    return a+b+c

print(add(5))
```
- default are created only once
    - here List is created only once, so when additem(33) is called it appends to existing list
```python
def additem(item, L=[]):
    L.append(item)
    return L

additem(22)
additem(33)
```

### Mixed positional Keyword Arguments
- anything before slash is positional arguments rest can be positional / keyword arguments
- anything after * should be keyword arguments
```python
def add(a, b, /, c, d, e, f):
    print(a, b, c, d, e, f)
    return a + b + c + d + e + f

add(2, 5, 3, f = 100, e = 20, d = 1)

# anything after * is keyword argument
def add2(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
    return a + b + c + d + e + f

add2(2, 5, e = 10, f = 100, c = 20, d = 1)
```
### Variable length positional arguments
- args type is tuple    
```python
def fun1(*args):
    print(type(args), args)

fun1()
fun1(10, 20)
fun1(30, 20, 10)

# <class 'tuple'> ()
# <class 'tuple'> (10, 20)
# <class 'tuple'> (30, 20, 10)
```

- Unpacking arguments
```python

def fun1(a, b, c):
    print(a, b, c)

L1 = [10, 5, 6]
fun1(*L1)

```
- Multiple return values
```python
def fun3(a, b, c):
    return a+1, b+1, c+1

x,y,z = fun3(1, 2, 3)
print(x, y, z)
```

### Variable Length Keyword Arguments
- we can pass variable keyword args (which has a type of dict)
- eg: {name:'nitin', age:25, add='Delhi'}
```python
def fun2(**kwargs):
    print(kwargs)
    print(type(kwargs))

fun2(name='nitin', age=25, add='Delhi')
#<class 'dict'>
```
## Iterators and Generators
- Iterators(iter)
- if we try to access the 5th element it would throw runtime error
```python
L = [1, 2, 3, 4]
itr = iter(L)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
```

- Generators
    - `yield` keeps the function on hold and returns the value
```python
def Days():
    L = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    i = 0
    while True:
        x = L[i]
        i = (i+1)%7
        yield x

d = Days()
print(next(d))
print(next(d))
print(next(d))
print(next(d))
```

## global vs local variables
- a function cannot modify global variables
- it can just access and read them
- to modify global variable from a function we define `global` eg: `global g`
- `globals()` gives list of all global variables
- `locals()` gives list of all local variables
eg:
```python
g = 10
def fun1():
    global g
    g = g + 5
    print('global', g)

fun1()
```
## Recursive Functions
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        res = n * factorial(n-1)
        return res

res = factorial(5)
print(res)
```

## Built in Functions
https://docs.python.org/3/library/functions.html#zip
<img src="./img/built-in-functions.png" alt="built-in-functions">

## What are Modules ?
- module is nothing but a python file
```python
import ModuleOne as mo
n1 = 10
n2 = 20
print('Sum', mo.add(n1, n2))
```
- __name__ prints '__main__' if executed in the same file
- if excuted in one file where its imported then it print the fileName

## Nested Functions
- Everything is an object in python, so fns are also treated as an object.
```python
def Outer():
    def Inner():
        print('I am inner function')

    Inner()

Outer()
```

## Returning Functions
- Function as parameter
```python
def display():
    print('hello world')

def fun(d):
    d()

fun(display)
```

- Function returning a function
```python
def Outer():
    def display():
        print('hello world')
    return display

d = Outer()
d()
```
## Closure Function
```python
def hello():
    msg = 'hello world'
    def display():
        print('*' * 10)
        print(msg)
        print('*' * 10)
    return display

d = hello()
d()
```
## Caller Class
- A class whose object can be used as a function name or method name is called as `caller class`.
```python
class Dept:
    def__init__(self):
        self.depts = {
            'hr': 'Human Resource',
            'acc': 'Accounts & Finance',
            'sd' : 'Sales & Distribution',
            'mkt': 'Marketing'
        }
    
    ## call is an override method
    def __call__(self, dept):
        return self.depts[dept]

d = Dept()
result = d('hr')
print(result)
```

## Decorator Function
- Steps
    - Passing fn as parameter
    - Nested fn calling paramter fn
    - return nested fn

- Similar to close fn, but here the fn should be passed as parameter and above steps should be followed.

```python
def decorator(fun):
    def wrapper():
        # do something
        print('something...')
        fun()
        print('did something...')
        # do something
    return wrapper

def display():
    print('hello')

d = decorator(display)
d()
```

## Lambda Functions
- anonymous fn , means fns which don't have any name.
- we should write them as single line of expression and they can take any number of args
```python
def mile2Km(miles):
    kms = 1.6 * miles
    return kms

# to lambda

k = lambda miles: 1.6 * miles
print(k(10))
```

## Exception Handling
- Exceptions are called as runtime errors
- Types of Errors
    - Syntax Errors
    - Logical Errors
    - Runtime Errors

- 






## Classes and Objects
- Declaration & intialisation both should be done inside constructor in python.
```python
class cuboid:
    def __init__(self, l, b, h) : #constructor (init -> intialiser )
        self.length = l
        self.breadth = b
        self.height = h
    
    def lidArea(self):
        return self.length * self.breadth


# creating object
c1 = cuboid
```

### self and reference
- self is reference to the same object
- eg `c2.volume()` here the c2.volume() -> reference the c2 object which is equal to self
- we cannot have multiple constructors as python takes up the recent constructor and overshadows the rest. (i.e the __init__ fn would have onlye 1 declaration)

### Instance variable and methods
- objects are called instances of a class
#### Variables
- instance variable
    ```python
    def sum(self):
        self.a = 10 #here a is an instance variable
    ```

- satic/class variable
    - variable common to the entire class

### Methods
- instance method
    - methods accessing instance variable
- class method
    - If a mathod is using class variable then its a class method

### Accessors and Mutators(get and set)
- get
    ```python
    def getLength(self):
        return self.length
    ```

- set
    ```python
        def setLength(self, l):
            self.length = l
    ```

### Inheritance
- if you are defining your own child class with constructor then the parent class constructor will not be implicitly called
- we would have to call the parent constructor using `super()`
```python
class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b
    
    def area(self):
        return self.length * self.breadth

#example of inheritance
class cuboid(Rectangle):
    def __init__(self, l, b,h):
        self.height = h
        super().__init__(l, b)
    
    def volume(self):
        return self.length * self.breadth * self.height

c1 = cuboid(5, 20, 10)
print(c1.volume())
print(c1.area())
```

### Inner classes
```python
class Customer:
    def __init__(self, name, state, city, country):
        self.name = name
        self.customerAddress = self.Address(state, city, country)
    
    class Address:
        def __init__(self, state, city, country):
            self.state = state
            self.city = city
            self.country = country
        
        def display(self):
            print(self.state)
            print(self.city)
            print(self.country)

c1 = Customer('nitin', 'delhi', 'delhi', 'india')
c1.customerAddress.display()
```

### Polymorphism (many forms)
```python
def petLover(animal):
    animal.talk()
    if hasAttr(animal, 'walk'):
        animal.walk()

class Duck:
    def talk(self):
        print('duck is talking')
    
    def walk(self):
        print('duck is walking')

class Dog:
    def talk(self):
        print('dog is barking')

animalType = Dog()
petLover(animalType)
```
## Method overloading
- when you write two methods with same name then the later one is considered in python.
- the previous one will be shadowed.

```python
class Arith:
    def sum(self, a, b, c = None):
        sum = a + b
        if c == None:
            return sum
        else:
            return sum + sum

a = Arith()
print(a.sum(5, 10))
print(a.sum(5, 10, 20))
```

## Method overriding
- redefining method of parent class in the child class
```python
class iPhone6:
    def home(self):
        print('home button is pressed')

class iPhoneX(iPhone6):
    def home(self):
        print('home is touched')
        super().home()

i6 = iPhone6()
i6.home()

ix = iPhoneX()
ix.home()
```

### Abstract Classes and Interfaces
- for this we would have to import `from abc import ABC, abstractmethod`
- any class inheriting from ABC becomes an abstract class
```python
from abc import ABC, abstractmethod
class Parent(ABC):
    def show(self):
        pass
    
    def display(self):
        print('parent display')

class Child(Parent):
    def show(self):
        print('child class')

c = Child()
c.show()
c.display()

```
- We get Error , if we try to instantiate an abstract class in python
```python

from abc import ABC, abstractmethod
class Parent(ABC):
    @abstractmethod
    def show(self):
        pass
    
    def display(self):
        print('parent display')

class Child(Parent):
    pass

c = Child()


Traceback (most recent call last):
  File "/Users/deshraj/Desktop/nitin/github/Python/code/abstract-class.py", line 13, in <module>
    c = Child()
TypeError: Can't instantiate abstract class Child without an implementation for abstract method 'show'
```

### Method Resolution
- object is the parent class for all the classes in Python.
- method resoultion order (className.mro()) (refer abstract-class.py eg)
    - output: `[<class '__main__.Child2'>, <class '__main__.Child'>, <class '__main__.Parent'>, <class 'abc.ABC'>, <class 'object'>]`
