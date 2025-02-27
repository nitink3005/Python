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