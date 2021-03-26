---
title: Errors and Exceptions
teaching: 10
exercises: 0
questions:
- "How does Python report errors?"
- "How can I handle errors in Python programs?"
objectives:
- "To be able to read a traceback, and determine where the error took place and what type it is."
- "To be able to describe the types of situations in which syntax errors,
   indentation errors, name errors, index errors, and missing file errors occur."
keypoints:
- "Tracebacks can look intimidating, but they give us a lot of useful information about
   what went wrong in our program, including where the error occurred and
   what type of error it was."
- "An error having to do with the 'grammar' or syntax of the program is called a `SyntaxError`.
   If the issue has to do with how the code is indented,
   then it will be called an `IndentationError`."
- "A `NameError` will occur when trying to use a variable that does not exist. Possible causes are
  that a variable definition is missing, a variable reference differs from its definition
  in spelling or capitalization, or the code contains a string that is missing quotes around it."
- "Containers like lists and strings will generate errors if you try to access items
   in them that do not exist. This type of error is called an `IndexError`."
- "Trying to read a file that does not exist will give you an `FileNotFoundError`.
   Trying to read a file that is open for writing, or writing to a file that is open for reading,
   will give you an `IOError`."
---

Every programmer encounters errors,
both those who are just beginning,
and those who have been programming for years.
Encountering errors and exceptions can be very frustrating at times,
and can make coding feel like a hopeless endeavour.
However,
understanding what the different types of errors are
and when you are likely to encounter them can help a lot.
Once you know *why* you get certain types of errors,
they become much easier to fix.

Errors in Python have a very specific form,
called a [traceback]({{ page.root }}/reference.html#traceback).
Let's examine one:

~~~
# This code has an intentional error. You can type it directly or
# use it for reference to understand the error message below.
def favorite_ice_cream():
    ice_creams = [
        'chocolate',
        'vanilla',
        'strawberry'
    ]
    print(ice_creams[3])

favorite_ice_cream()
~~~
{: .language-python}

~~~
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-1-70bd89baa4df> in <module>()
      9     print(ice_creams[3])
      10
----> 11 favorite_ice_cream()

<ipython-input-1-70bd89baa4df> in favorite_ice_cream()
      7         'strawberry'
      8     ]
----> 9     print(ice_creams[3])
      10
      11 favorite_ice_cream()

IndexError: list index out of range
~~~
{: .error}

This particular traceback has two levels.
You can determine the number of levels by looking for the number of arrows on the left hand side.
In this case:

1.  The first shows code from the cell above,
    with an arrow pointing to Line 11 (which is `favorite_ice_cream()`).

2.  The second shows some code in the function `favorite_ice_cream`,
    with an arrow pointing to Line 9 (which is `print(ice_creams[3])`).

The last level is the actual place where the error occurred.
The other level(s) show what function the program executed to get to the next level down.
So, in this case, the program first performed a
[function call]({{ page.root }}/reference.html#function-call) to the function `favorite_ice_cream`.
Inside this function,
the program encountered an error on Line 6, when it tried to run the code `print(ice_creams[3])`.

> ## Long Tracebacks
>
> Sometimes, you might see a traceback that is very long
> -- sometimes they might even be 20 levels deep!
> This can make it seem like something horrible happened,
> but the length of the error message does not reflect severity, rather,
> it indicates that your program called many functions before it encountered the error.
> Most of the time, the actual place where the error occurred is at the bottom-most level,
> so you can skip down the traceback to the bottom.
{: .callout}

So what error did the program actually encounter?
In the last line of the traceback,
Python helpfully tells us the category or type of error (in this case, it is an `IndexError`)
and a more detailed error message (in this case, it says "list index out of range").

If you encounter an error and don't know what it means,
it is still important to read the traceback closely.
That way,
if you fix the error,
but encounter a new one,
you can tell that the error changed.
Additionally,
sometimes knowing *where* the error occurred is enough to fix it,
even if you don't entirely understand the message.

If you do encounter an error you don't recognize,
try looking at the
[official documentation on errors](http://docs.python.org/3/library/exceptions.html).
However,
note that you may not always be able to find the error there,
as it is possible to create custom errors.
In that case,
hopefully the custom error message is informative enough to help you figure out what went wrong.

## Common types of errors
- TabError: error in whitespacing
- NameError: getting the name of a variable/function wrong or using an undefined one
- IndexError (lists tuples etc)
- KeyError (dicts)
- FileNotFoundError
- UnsupportedOperation: e.g. trrying to write to a file that is open read only
- TypeError: wrong type supplied (e.g. numbers where strings are expected) or missing or too many function parameters

Often the error you are looking for is at the bottom, but if working with libraries it can be a bit higher up. Tip

> ## Tracebacks with libraries
>
> If using libraries you may have to start at the bottom and look backward till you find your own code referenced:
{: .callout}

~~~
>>> printer.doprint(oo)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\uczmh2\AppData\Local\Programs\Python\Python39\lib\site-packages\cellmlmanip\printer.py", line 136, in doprint
    return super().doprint(expr)
  File "C:\Users\uczmh2\AppData\Local\Programs\Python\Python39\lib\site-packages\sympy\printing\printer.py", line 291, in doprint
    return self._str(self._print(expr))
  File "C:\Users\uczmh2\AppData\Local\Programs\Python\Python39\lib\site-packages\sympy\printing\printer.py", line 331, in _print
    return self.emptyPrinter(expr)
  File "C:\Users\uczmh2\AppData\Local\Programs\Python\Python39\lib\site-packages\cellmlmanip\printer.py", line 167, in emptyPrinter
    raise ValueError(
ValueError: Unsupported expression type (<class 'type'>): <class '__main__.oo'>
~~~
{: .error}

{% include links.md %}
