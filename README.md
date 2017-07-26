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
