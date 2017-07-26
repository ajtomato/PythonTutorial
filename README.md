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

