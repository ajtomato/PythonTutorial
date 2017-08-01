# Python Tutorial

## 1. Whetting Your Appetite

## 2. Using the Python Interpreter

### 2.1 Invoking the Interpreter

Typing an end-of-file character (Control-D on Unix, Control-Z on Windows) at the primary prompt causes the interpreter to exit with a zero exit status. If that doesn’t work, you can exit the interpreter by typing the following command: quit().

A way of starting the interpreter is python -c command [arg] ..., which executes the statement(s) in command, analogous to the shell’s -c option. Since Python statements often contain spaces or other characters that are special to the shell, it is usually advised to quote command in its entirety with single quotes.

Some Python modules are also useful as scripts. These can be invoked using python -m module [arg] ..., which executes the source file for module as if you had spelled out its full name on the command line.

#### 2.1.1 Argument Passing

When known to the interpreter, the script name and additional arguments thereafter are turned into a list of strings and assigned to the argv variable in the sys module, e.g., sys.argv[0].

#### 2.1.2. Interactive Mode

### 2.2. The Interpreter and Its Environment

#### 2.2.1. Source Code Encoding

To declare an encoding other than the default one, a special comment line should be added as the first line of the file.

One exception to the first line rule is when the source code starts with a UNIX “shebang” line. In this case, the encoding declaration should be added as the second line of the file. For example:

    #!/usr/bin/env python3
    # -*- coding: cp-1252 -*-

## 3. An Informal Introduction to Python

Comments in Python start with the hash character, #, and extend to the end of the physical line.

### 3.1. Using Python as a Calculator

#### 3.1.1. Numbers

Division (/) always returns a float. To do floor division and get an integer result (discarding any fractional result) you can use the (//) operator.

There is full support for floating point; operators with mixed type operands convert the integer operand to floating point.

With Python, it is possible to use the ** operator to calculate powers.

In interactive mode, the last printed expression is assigned to the variable _. This variable should be treated as read-only by the user. Don’t explicitly assign a value to it.

#### 3.1.2. Strings

Strings can be enclosed in single quotes ('...') or double quotes ("...") with the same result. \ can be used to escape quotes

    >>> 'doesn\'t'  # use \' to escape the single quote...

If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote.

String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''. End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line.

    print("""\
    Usage: thingy [OPTIONS]
        -h                        Display this usage message
        -H hostname               Hostname to connect to
    """)

Strings can be concatenated (glued together) with the + operator, and repeated with *.

Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated. This only works with two literals though, not with variables or expressions.

    >>> 'Py' 'thon'

Slicing is also supported. The start is always included, and the end always excluded.

Python strings cannot be changed — they are immutable.

The built-in function len() returns the length of a string:

    >>> len(s)

#### 3.1.3. Lists

All slice operations on lists return a **NEW** list containing the requested elements.

Lists are a mutable type, i.e. it is possible to change their content.

You can also add new items at the end of the list, by using the append() method.

    >>> cubes.append(216)

Assignment to slices is also possible and works on the original list, and this can even change the size of the list or clear it entirely.

### 3.2. First Steps Towards Programming

For print, a space is inserted between items. The keyword argument _end_ can be used to avoid the newline after the output, or end the output with a different string.

## 4. More Control Flow Tools

### 4.1. if Statements

### 4.2. for Statements

Python’s for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence.

If you need to modify the sequence you are iterating over while inside the loop (for example to duplicate selected items), it is recommended that you first make a copy. Iterating over a sequence does not implicitly make a copy. The slice notation makes this especially convenient.

### 4.3. The range() Function

If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy.

    >>> for i in range(5):
    >>> for o in lst:
    >>> for i, o in enumerate(lst):

In many ways the object returned by range() behaves as if it is a list, but in fact it isn’t. It is an object which returns the successive items of the desired sequence when you iterate over it, but it doesn’t really make the list, thus saving space.

    >>> list(range(5))

### 4.4. break and continue Statements, and else Clauses on Loops

Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the list (with for) or when the condition becomes false (with while), but not when the loop is terminated by a break statement.

### 4.5. pass Statements

### 4.6. Defining Functions

The first statement of the function body can optionally be a string literal; this string literal is the function’s documentation string, or docstring.

The _return_ statement returns with a value from a function. _return_ without an expression argument returns _None_. Falling off the end of a function also returns _None_.

### 4.7. More on Defining Functions

#### 4.7.1. Default Argument Values

The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes.

    def f(a, L=[]):
        L.append(a)
        return L
    print(f(1))
    print(f(2))
    print(f(3))

The _in_ keyword tests whether or not a sequence contains a certain value.

    if ok in ('n', 'no', 'nop', 'nope'):
        return False

#### 4.7.2. Keyword Arguments

In a function call, keyword arguments must follow positional arguments.

#### 4.7.3. Arbitrary Argument Lists

These arguments will be wrapped up in a tuple. Before the variable number of arguments, zero or more normal arguments may occur.

When a final formal parameter of the form **name is present, it receives a dictionary containing all keyword arguments except for those corresponding to a formal parameter.

    def cheeseshop(kind, *arguments, **keywords):
        print("-- Do you have any", kind, "?")
        print("-- I'm sorry, we're all out of", kind)
        for arg in arguments:
            print(arg)
        print("-" * 40)
        for kw in keywords:
            print(kw, ":", keywords[kw])

    cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

#### 4.7.4. Unpacking Argument Lists

The reverse situation occurs when the arguments are already in a list or tuple but need to be unpacked for a function call requiring separate positional arguments. If they are not available separately, write the function call with the *-operator to unpack the arguments out of a list or tuple. In the same fashion, dictionaries can deliver keyword arguments with the **-operator.

    >>> args = [3, 6]
    >>> list(range(*args))            # call with arguments unpacked from a list
    >>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
    >>> parrot(**d)

#### 4.7.5. Lambda Expressions

Small anonymous functions can be created with the lambda keyword. This function returns the sum of its two arguments: lambda a, b: a+b.

Like nested function definitions, lambda functions can reference variables from the containing scope:

    >>> def make_incrementor(n):
    ...     return lambda x: x + n
    ...
    >>> f = make_incrementor(42)
    >>> f(0)
    42
    >>> f(1)
    43

#### 4.7.6. Documentation Strings

The first line should always be a short, concise summary of the object’s purpose. This line should begin with a capital letter and end with a period.

If there are more lines in the documentation string, the second line should be blank, visually separating the summary from the rest of the description. The following lines should be one or more paragraphs describing the object’s calling conventions, its side effects, etc.

#### 4.7.7. Function Annotations

 Parameter annotations are defined by a colon after the parameter name, followed by an expression evaluating to the value of the annotation. Return annotations are defined by a literal ->, followed by an expression, between the parameter list and the colon denoting the end of the def statement.

    >>> def f(ham: str, eggs: str = 'eggs') -> str:

### 4.8. Intermezzo: Coding Style

## 5. Data Structures

### 5.1. More on Lists

#### 5.1.1. Using Lists as Stacks

    >>> stack = [3, 4, 5]
    >>> stack.append(6)
    >>> stack.pop()

#### 5.1.2. Using Lists as Queues

Lists are not efficient for this purpose. To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends.

    >>> from collections import deque
    >>> queue = deque(["Eric", "John", "Michael"])
    >>> queue.append("Terry")
    >>> queue.popleft()

#### 5.1.3. List Comprehensions

List comprehensions provide a concise way to create lists.

    >>> squares = list(map(lambda x: x**2, range(10)))
    >>> squares = [x**2 for x in range(10)]

A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it. If the expression is a tuple (e.g. the (x, y) in the previous example), it must be parenthesized.

    >>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

#### 5.1.4. Nested List Comprehensions

### 5.2. The del statement

There is a way to remove an item from a list given its index instead of its value: the del statement.

    >>> a = [-1, 1, 66.25, 333, 333, 1234.5]
    >>> del a[0]
    >>> del a[2:4]
    >>> del a[:]
    >>> del a

### 5.3. Tuples and Sequences

Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking or indexing (or even by attribute in the case of _namedtuples_). Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

Empty tuples are constructed by an empty pair of parentheses; a tuple with one item is constructed by following a value with a comma (it is not sufficient to enclose a single value in parentheses).

The statement t = 12345, 54321, 'hello!' is an example of tuple packing: the values 12345, 54321 and 'hello!' are packed together in a tuple. The reverse operation is also possible:

    >>> x, y, z = t

This is called, appropriately enough, sequence unpacking and works for any sequence on the right-hand side.

### 5.4. Sets

A set is an unordered collection with no duplicate elements.

Curly braces or the set() function can be used to create sets. Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary.

    >>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    >>> 'orange' in basket
    >>> a = set('abracadabra')
    >>> b = set('alacazam')
    >>> a - b
    >>> a | b
    >>> a & b
    >>> a ^ b

Set comprehensions are also supported.

    >>> a = {x for x in 'abracadabra' if x not in 'abc'}

### 5.5. Dictionaries

Dictionaries are indexed by keys, which can be any immutable type. If a tuple contains any mutable object either directly or indirectly, it cannot be used as a key.

    >>> tel = {'jack': 4098, 'sape': 4139}
    >>> tel['guido'] = 4127
    >>> del tel['sape']
    >>> list(tel.keys())
    >>> 'guido' in tel

The dict() constructor builds dictionaries directly from sequences of key-value pairs:

    >>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:

    >>> dict(sape=4139, guido=4127, jack=4098)

In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:

    >>> {x: x**2 for x in (2, 4, 6)}

### 5.6. Looping Techniques

When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.

    >>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    >>> for k, v in knights.items():

When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.

    >>> for i, v in enumerate(['tic', 'tac', 'toe']):

To loop over two or more sequences at the same time, the entries can be paired with the zip() function.

    >>> questions = ['name', 'quest', 'favorite color']
    >>> answers = ['lancelot', 'the holy grail', 'blue']
    >>> for q, a in zip(questions, answers):

To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.

    >>> for i in reversed(range(1, 10, 2)):

To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.

    >>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    >>> for f in sorted(set(basket)):

### 5.7. More on Conditions

The comparison operators _in_ and _not in_ check whether a value occurs (does not occur) in a sequence.

The operators _is_ and _is not_ compare whether two objects are really the same object; this only matters for mutable objects like lists.

### 5.8. Comparing Sequences and Other Types

Sequence objects may be compared to other objects with the same sequence type. The comparison uses lexicographical ordering: first the first two items are compared, and if they differ this determines the outcome of the comparison; if they are equal, the next two items are compared, and so on, until either sequence is exhausted. If two items to be compared are themselves sequences of the same type, the lexicographical comparison is carried out recursively. If all items of two sequences compare equal, the sequences are considered equal. If one sequence is an initial sub-sequence of the other, the shorter sequence is the smaller (lesser) one.

## 6. Modules

A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended.

Within a module, the module’s name (as a string) is available as the value of the global variable _\_\_name___.

The simple _import_ statement does not enter the names of the functions defined in the module directly in the current symbol table; it only enters the module name there. Using the module name you can access the functions:

    >>> import tutorial
    >>> print(tutorial.l)

### 6.1. More on Modules

A module can contain executable statements as well as function definitions. These statements are intended to initialize the module. They are executed only the first time the module name is encountered in an import statement.

Each module has its own private symbol table, which is used as the global symbol table by all functions defined in the module. Thus, the author of a module can use global variables in the module without worrying about accidental clashes with a user’s global variables. On the other hand, if you know what you are doing you can touch a module’s global variables with the same notation used to refer to its functions, modname.itemname.

There is a variant of the import statement that imports names from a module directly into the importing module’s symbol table.

    >>> from fibo import fib, fib2
    >>> fib(500)

#### 6.1.1. Executing modules as scripts

When you run a Python module with

    python fibo.py <arguments>

the code in the module will be executed, just as if you imported it, but with the _\_\_name___ set to "_\_\_main___". That means that by adding this code at the end of your module:

    if __name__ == "__main__":
        pass

#### 6.1.2. The Module Search Path

When a module named spam is imported, the interpreter first searches for a built-in module with that name. If not found, it then searches for a file named spam.py in a list of directories given by the variable sys.path. sys.path is initialized from these locations:

* The directory containing the input script (or the current directory when no file is specified).
* PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
* The installation-dependent default.

On file systems which support symlinks, the directory containing the input script is calculated after the symlink is followed. In other words the directory containing the symlink is not added to the module search path.

After initialization, Python programs can modify sys.path. The directory containing the script being run is placed at the beginning of the search path, ahead of the standard library path. This means that scripts in that directory will be loaded instead of modules of the same name in the library directory. 

#### 6.1.3. “Compiled” Python files

To speed up loading modules, Python caches the compiled version of each module in the _\_\_pycache___ directory under the name module.version.pyc, where the version encodes the format of the compiled file; it generally contains the Python version number.

### 6.2. Standard Modules

### 6.3. The dir() Function

### 6.4. Packages

The _\_\_init___.py files are required to make Python treat the directories as containing packages; this is done to prevent directories with a common name, such as string, from unintentionally hiding valid modules that occur later on the module search path.

When using _from package import item_, the _item_ can be either a submodule (or subpackage) of the package, or some other name defined in the package, like a function, class or variable.

When using syntax like import item.subitem.subsubitem, each item except for the last must be a package; the last item can be a module or a package but can’t be a class or function or variable defined in the previous item.

    >>> import sound.effects.echo
    >>> sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

    >>> from sound.effects import echo
    >>> echo.echofilter(input, output, delay=0.7, atten=4)

#### 6.4.1. Importing * From a Package

The import statement uses the following convention: if a package’s _\_\_init___.py code defines a list named _\_\_all___, it is taken to be the list of module names that should be imported when from package import * is encountered.

    __all__ = ["echo", "surround", "reverse"]

#### 6.4.2. Intra-package References

When packages are structured into subpackages, you can use absolute imports to refer to submodules of siblings packages.

You can also write relative imports, with the from module import name form of import statement. These imports use leading dots to indicate the current and parent packages involved in the relative import.

    >>> from . import echo                  # The same module
    >>> from .. import formats              # The parent module
    >>> from ..filters import equalizer     # The sibling module.

Note that relative imports are based on the name of the current module. Since the name of the main module is always "__main__", modules intended for use as the main module of a Python application must always use absolute imports.

#### 6.4.3. Packages in Multiple Directories

## 7. Input and Output

### 7.1. Fancier Output Formatting

The str() function is meant to return representations of values which are fairly human-readable, while repr() is meant to generate representations which can be read by the interpreter.

Basic usage of the str.format() method looks like this.

    >>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
    We are the knights who say "Ni!"
    >>> print('{0} and {1}'.format('spam', 'eggs'))
    spam and eggs
    >>> print('{1} and {0}'.format('spam', 'eggs'))
    eggs and spam
    >>> print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
    This spam is absolutely horrible.

An optional ':' and format specifier can follow the field name.

    >>> print('The value of PI is approximately {0:.3f}.'.format(math.pi))

Passing an integer after the ':' will cause that field to be a minimum number of characters wide.

    >>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
    >>> for name, phone in table.items():
    ...     print('{0:10} ==> {1:10d}'.format(name, phone))

If you have a really long format string that you don’t want to split up, it would be nice if you could reference the variables to be formatted by name instead of by position. This can be done by simply passing the dict and using square brackets '[]' to access the keys.

    >>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
    >>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
    ...       'Dcab: {0[Dcab]:d}'.format(table))
    Jack: 4098; Sjoerd: 4127; Dcab: 8637678
    >>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
    Jack: 4098; Sjoerd: 4127; Dcab: 8637678

This is particularly useful in combination with the built-in function _vars()_, which returns a dictionary containing all local variables.

#### 7.1.1. Old string formatting

### 7.2. Reading and Writing Files

It is good practice to use the _with_ keyword when dealing with file objects. The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point. Using _with_ is also much shorter than writing equivalent try-finally blocks.

    >>> with open('workfile') as f:
    ...     read_data = f.read()
    >>> f.closed                    # Double check whether the file is closed.

Normally, files are opened in text mode, that means, you read and write strings from and to the file, which are encoded in a specific encoding. If encoding is not specified, the default is platform dependent (see _open()_).

In text mode, the default when reading is to convert platform-specific line endings (\n on Unix, \r\n on Windows) to just \n. When writing in text mode, the default is to convert occurrences of \n back to platform-specific line endings.

#### 7.2.1. Methods of File Objects

If the end of the file has been reached, _f.read()_ will return an empty string ('').

_f.readline()_ reads a single line from the file; a newline character (\n) is left at the end of the string, and is only omitted on the last line of the file if the file doesn’t end in a newline. If _f.readline()_ returns an empty string, the end of the file has been reached.

For reading lines from a file, you can loop over the file object. This is memory efficient, fast, and leads to simple code:

    >>> for line in f:
    ...     print(line, end='')

If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().

#### 7.2.2. Saving structured data with json

    >>> import json
    >>> json.dumps([1, 'simple', 'list'])
    '[1, "simple", "list"]'
    >>> json.dump(x, f)
    >>> x = json.load(f)

## 8. Errors and Exceptions

### 8.1. Syntax Errors

### 8.2. Exceptions

### 8.3. Handling Exceptions

    >>> try:
    ...     raise Exception('spam', 'eggs')
    >>> except ExceptionType [as err]:
    ...     x, y = err.args
    >>> except (ExceptionType1, ExceptionType2, ..., ExceptionTypeN):
    ...     pass
    >>> except:
    ...     raise
    >>> else:
    ...     pass    # It is useful for code that must be executed if the try clause does not raise an exception.

The except clause may specify a variable after the exception name. The variable is bound to an exception instance with the arguments stored in instance.args.

### 8.4. Raising Exceptions

### 8.5. User-defined Exceptions

### 8.6. Defining Clean-up Actions

A _finally_ clause is always executed before leaving the _try_ statement, whether an exception has occurred or not.

    >>> try:
    ...     raise KeyboardInterrupt
    ... finally:
    ...     print('Goodbye, world!')

The _finally_ clause is also executed “on the way out” when any other clause of the _try_ statement is left via a _break_, _continue_ or _return_ statement.

In real world applications, the _finally_ clause is useful for releasing external resources (such as files or network connections), regardless of whether the use of the resource was successful.

### 8.7. Predefined Clean-up Actions

Some objects define standard clean-up actions to be undertaken when the object is no longer needed, regardless of whether or not the operation using the object succeeded or failed. The _with_ statement allows objects like files to be used in a way that ensures they are always cleaned up promptly and correctly.

## 9. Classes

### 9.1. A Word About Names and Objects

### 9.2. Python Scopes and Namespaces

The _nonlocal_ statement causes the listed identifiers to refer to previously bound variables in the nearest enclosing scope excluding globals.

The _global_ statement is a **declaration** which holds for the entire current code block.

#### 9.2.1. Scopes and Namespaces Example

### 9.3. A First Look at Classes

#### 9.3.1. Class Definition Syntax

#### 9.3.2. Class Objects

Class objects support two kinds of operations: attribute references and instantiation.

Attribute references use the standard syntax used for all attribute references in Python: obj.name. Valid attribute names are all the names that were in the class’s namespace when the class object was created.

Class instantiation uses function notation. Just pretend that the class object is a parameterless function that returns a new instance of the class.

The instantiation operation (“calling” a class object) creates an empty object.

#### 9.3.3. Instance Objects

The only operations understood by instance objects are attribute references. There are two kinds of valid attribute names, data attributes and methods.

Data attributes need not be declared; like local variables, they spring into existence when they are first assigned to.

By definition, all attributes of a class that are **function objects** define corresponding **methods** of its instances.

#### 9.3.4. Method Objects

When an instance attribute is referenced that isn’t a data attribute, its class is searched. If the name denotes a valid class attribute that is a function object, a method object is created by packing (pointers to) the instance object and the function object just found together in an abstract object: **this is the method object**. When the method object is called with an argument list, a new argument list is constructed from the instance object and the argument list, and the function object is called with this new argument list.

#### 9.3.5. Class and Instance Variables

Generally speaking, instance variables are for data unique to each instance and class variables are for attributes and methods shared by all instances of the class.

### 9.4. Random Remarks

Data attributes override method attributes with the same name; to avoid accidental name conflicts, which may cause hard-to-find bugs in large programs, it is wise to use some kind of convention that minimizes the chance of conflicts. Possible conventions include capitalizing method names, prefixing data attribute names with a small unique string (perhaps just an underscore), or using verbs for methods and nouns for data attributes.

Any function object that is a class attribute defines a method for instances of that class. It is not necessary that the function definition is textually enclosed in the class definition: assigning a function object to a local variable in the class is also ok.

    # Function defined outside the class
    def f1(self, x, y):
        return min(x, x+y)

    class C:
        f = f1

Methods may call other methods by using method attributes of the _self_ argument.

### 9.5. Inheritance

    class DerivedClassName(BaseClassName):

Execution of a derived class definition proceeds the same as for a base class. When the class object is constructed, the base class is remembered. This is used for resolving attribute references: if a requested attribute is not found in the class, the search proceeds to look in the base class. This rule is applied recursively if the base class itself is derived from some other class.

Derived classes may override methods of their base classes. Because methods have no special privileges when calling other methods of the same object, a method of a base class that calls another method defined in the same base class may end up calling a method of a derived class that overrides it.

An overriding method in a derived class may in fact want to extend rather than simply replace the base class method of the same name. There is a simple way to call the base class method directly: just call _BaseClassName.methodname(self, arguments)_.

#### 9.5.1. Multiple Inheritance

    class DerivedClassName(Base1, Base2, Base3):

For most purposes, in the simplest cases, you can think of the search for attributes inherited from a parent class as depth-first, left-to-right, not searching twice in the same class where there is an overlap in the hierarchy.

### 9.6. Private Variables

“Private” instance variables that cannot be accessed except from inside an object don’t exist in Python. However, there is a convention that is followed by most Python code: a name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API (whether it is a function, a method or a data member).

Name mangling: any identifier of the form \_\_spam (at least two leading underscores, at most one trailing underscore) is textually replaced with _classname__spam, where classname is the current class name with leading underscore(s) stripped. This mangling is done without regard to the syntactic position of the identifier, as long as it occurs within the definition of a class.

Name mangling is helpful for letting subclasses override methods without breaking intraclass method calls.

### 9.7. Odds and Ends

### 9.8. Iterators

The for statement calls _iter()_ on the container object. The function returns an iterator object that defines the method _\_\_next\_\_()_ which accesses elements in the container one at a time. When there are no more elements, _\_\_next\_\_()_ raises a _StopIteration_ exception which tells the for loop to terminate.

### 9.9. Generators

Generators are a simple and powerful tool for creating iterators. They are written like regular functions but use the _yield_ statement whenever they want to return data. Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed).

    def reverse(data):
        for index in range(len(data)-1, -1, -1):
            yield data[index]

### 9.10. Generator Expressions

Some simple generators can be coded succinctly as expressions using a syntax similar to list comprehensions but with parentheses instead of brackets.

## 10. Brief Tour of the Standard Library

### 10.1. Operating System Interface

The _os_ module provides dozens of functions for interacting with the operating system.

For daily file and directory management tasks, the _shutil_ module provides a higher level interface that is easier to use.

### 10.2. File Wildcards

The _glob_ module provides a function for making file lists from directory wildcard searches.

### 10.3. Command Line Arguments

    >>> import sys
    >>> print(sys.argv)

The _getopt_ module processes _sys.argv_ using the conventions of the Unix getopt() function. More powerful and flexible command line processing is provided by the _argparse_ module.

### 10.4. Error Output Redirection and Program Termination

The _sys_ module also has attributes for _stdin_, _stdout_, and _stderr_.

    >>> sys.stderr.write('Warning, log file not found starting a new one\n')

The most direct way to terminate a script is to use _sys.exit()_.

### 10.5. String Pattern Matching

The _re_ module provides regular expression tools for advanced string processing.

When only simple capabilities are needed, string methods are preferred because they are easier to read and debug.

### 10.6. Mathematics

The _math_ module gives access to the underlying C library functions for floating point math.

The _random_ module provides tools for making random selections.

The _statistics_ module calculates basic statistical properties (the mean, median, variance, etc.) of numeric data.

The SciPy project <https://scipy.org> has many other modules for numerical computations.

### 10.7. Internet Access

Two of the simplest are _urllib.request_ for retrieving data from URLs and _smtplib_ for sending mail.

    >>> from urllib.request import urlopen
    >>> with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    ...     for line in response:
    ...         line = line.decode('utf-8')  # Decoding the binary data to text.
    ...         if 'EST' in line or 'EDT' in line:  # look for Eastern Time
    ...             print(line)

    <BR>Nov. 25, 09:43:32 PM EST

    >>> import smtplib
    >>> server = smtplib.SMTP('localhost')
    >>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
    ... """To: jcaesar@example.org
    ... From: soothsayer@example.org
    ...
    ... Beware the Ides of March.
    ... """)
    >>> server.quit()

### 10.8. Dates and Times

The _datetime_ module supplies classes for manipulating dates and times in both simple and complex ways.

### 10.9. Data Compression

Common data archiving and compression formats are directly supported by modules including: _zlib_, _gzip_, _bz2_, _lzma_, _zipfile_ and _tarfile_.

### 10.10. Performance Measurement

The _timeit_ module quickly demonstrates a modest performance advantage.

In contrast to _timeit_‘s fine level of granularity, the _profile_ and _pstats_ modules provide tools for identifying time critical sections in larger blocks of code.

### 10.11. Quality Control

The _doctest_ module provides a tool for scanning a module and validating tests embedded in a program’s docstrings.

    def average(values):
        """Computes the arithmetic mean of a list of numbers.

        >>> print(average([20, 30, 70]))
        40.0
        """
        return sum(values) / len(values)

    import doctest
    doctest.testmod()   # automatically validate the embedded tests

The _unittest_ module is not as effortless as the doctest module, but it allows a more comprehensive set of tests to be maintained in a separate file.

    import unittest

    class TestStatisticalFunctions(unittest.TestCase):

        def test_average(self):
            self.assertEqual(average([20, 30, 70]), 40.0)
            self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
            with self.assertRaises(ZeroDivisionError):
                average([])
            with self.assertRaises(TypeError):
                average(20, 30, 70)

    unittest.main()  # Calling from the command line invokes all tests

### 10.12. Batteries Included

## 11. Brief Tour of the Standard Library — Part II

### 11.1. Output Formatting

The _reprlib_ module provides a version of _repr()_ customized for abbreviated displays of large or deeply nested containers.

The _pprint_ module offers more sophisticated control over printing both built-in and user defined objects in a way that is readable by the interpreter.

The _textwrap_ module formats paragraphs of text to fit a given screen width.

The _locale_ module accesses a database of culture specific data formats.

### 11.2. Templating

The _string_ module includes a versatile _Template_ class with a simplified syntax suitable for editing by end-users.

The format uses placeholder names formed by $ with valid Python identifiers (alphanumeric characters and underscores). Surrounding the placeholder with braces allows it to be followed by more alphanumeric letters with no intervening spaces. Writing $$ creates a single escaped $.

    >>> t = Template('Return the $item to $owner.')
    >>> d = dict(item='unladen swallow')
    >>> t.substitute(d)
    Traceback (most recent call last):
    ...
    KeyError: 'owner'
    >>> t.safe_substitute(d)
    'Return the unladen swallow to $owner.'

Template subclasses can specify a custom _delimiter_.

### 11.3. Working with Binary Data Record Layouts

The _struct_ module provides _pack()_ and _unpack()_ functions for working with variable length binary record formats.

### 11.4. Multi-threading

The high level _threading_ module can run tasks in background.

So, the **preferred approach** to task coordination is to concentrate all access to a resource in a single thread and then use the _queue_ module to feed that thread with requests from other threads. Applications using _Queue_ objects for inter-thread communication and coordination are easier to design, more readable, and more reliable.

### 11.5. Logging

    import logging
    logging.debug('Debugging information')
    logging.info('Informational message')
    logging.warning('Warning:config file %s not found', 'server.conf')
    logging.error('Error occurred')
    logging.critical('Critical error -- shutting down')

By default, informational and debugging messages are suppressed and the output is sent to standard error. Other output options include routing messages through email, datagrams, sockets, or to an HTTP Server. New filters can select different routing based on message priority: DEBUG, INFO, WARNING, ERROR, and CRITICAL.

The logging system can be configured directly from Python or can be loaded from a user editable configuration file for customized logging without altering the application.

### 11.6. Weak References

The _weakref_ module provides tools for tracking objects without creating a reference. When the object is no longer needed, it is automatically removed from a weakref table and a callback is triggered for weakref objects.

    >>> import weakref
    >>> a = A(10)                   # create a reference
    >>> d = weakref.WeakValueDictionary()
    >>> d['primary'] = a            # does not create a reference
    >>> d['primary']                # fetch the object if it is still alive


### 11.7. Tools for Working with Lists

The _array_ module provides an array() object that is like a list that stores only homogeneous data and stores it more compactly.

    >>> from array import array
    >>> a = array('H', [4000, 10, 700, 22222])

The _collections_ module provides a _deque()_ object that is like a list with faster appends and pops from the left side but slower lookups in the middle.

    >>> from collections import deque
    >>> d = deque(["task1", "task2", "task3"])
    >>> d.append("task4")
    >>> print("Handling", d.popleft())

The _bisect_ module with functions for manipulating sorted lists.

    >>> import bisect
    >>> scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
    >>> bisect.insort(scores, (300, 'ruby'))

The _heapq_ module provides functions for implementing heaps based on regular lists. The lowest valued entry is always kept at position zero.

    >>> from heapq import heapify, heappop, heappush
    >>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    >>> heapify(data)                      # rearrange the list into heap order
    >>> heappush(data, -5)                 # add a new entry
    >>> [heappop(data) for i in range(3)]  # fetch the three smallest entries

### 11.8. Decimal Floating Point Arithmetic

The _decimal_ module offers a _Decimal_ datatype for decimal floating point arithmetic. Compared to the built-in _float_ implementation of binary floating point, the class is especially helpful for:

* financial applications and other uses which require exact decimal representation,
* control over precision,
* control over rounding to meet legal or regulatory requirements,
* tracking of significant decimal places, or
* applications where the user expects the results to match calculations done by hand.

The _decimal_ module provides arithmetic with as much precision as needed.

## 12. Virtual Environments and Packages

### 12.1. Introduction

A virtual environment is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.

Different applications can then use different virtual environments.

### 12.2. Creating Virtual Environments

The module used to create and manage virtual environments is called _venv_.

To create a virtual environment, decide upon a directory where you want to place it, and run the _venv_ module as a script with the directory path:

    python -m venv tutorial-env

This will create the tutorial-env directory if it doesn’t exist, and also create directories inside it containing a copy of the Python interpreter, the standard library, and various supporting files.

Once you’ve created a virtual environment, you may activate it.

On Windows, run:

    tutorial-env\Scripts\activate.bat

On Unix or MacOS, run:

    source tutorial-env/bin/activate

### 12.3. Managing Packages with pip

You can install the latest version of a package by specifying a package’s name.

    $ pip install novas

You can also install a specific version of a package by giving the package name followed by == and the version number.

    $ pip install requests==2.6.0
    $ pip install --upgrade requests    # Upgrade to the latest version

_pip uninstall_ followed by one or more package names will remove the packages from the virtual environment.

_pip show_ will display information about a particular package.

    $ pip show requests

_pip list_ will display all of the packages installed in the virtual environment.

    $ pip list

_pip freeze_ will produce a similar list of the installed packages, but the output uses the format that pip install expects. A common convention is to put this list in a _requirements.txt_ file. The _requirements.txt_ can then be committed to version control and shipped as part of an application. Users can then install all the necessary packages with install -r.

    $ pip install -r requirements.txt
