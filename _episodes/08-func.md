---
title: Readable code
teaching: 5
exercises: 0
questions:
- "Writing readable code"
objectives:
- "Understand how to make code more readable"
keypoints:
- "Code readability tips."
- "Use `help(thing)` to view help for something."
- "Put docstrings in functions to provide help for that function."
- "Specify default values for parameters when defining a function using `name=value`
   in the parameter list."
- "Put code whose parameters change frequently in a function,
   then call it with different parameter values to customize its behavior."
---
## Readable functions

Consider the following function:

~~~
from math import sqrt

def W(p):
    a = 0
    for v in p:
        a += v
    m = a / len(p)
    d = 0
    for v in p:
        d += (v - m)**2
    return numpy.sqrt(d / (len(p) - 1))
~~~
{: .language-python}

What does this function do? How about the following function?

~~~
def std_dev(sample):
    sample_sum = 0
    for value in sample:
        sample_sum += value

    sample_mean = sample_sum / len(sample)

    sum_squared_devs = 0
    for value in sample:
        sum_squared_devs += (value - sample_mean)**2

    return numpy.sqrt(sum_squared_devs / (len(sample) - 1))
~~~
{: .language-python}

The functions s and std_dev are computationally equivalent (they both calculate the sample standard deviation), but to a human reader, they look very different. You probably found std_dev much easier to read and understand than s.

As this example illustrates, both documentation and a programmer’s coding style combine to determine how easy it is for others to read and understand the programmer’s code. Choosing meaningful variable names and using blank spaces to break the code into logical “chunks” are helpful techniques for producing readable code. This is useful not only for sharing code with others, but also for the original programmer. If you need to revisit code that you wrote months ago and haven’t thought about since then, you will appreciate the value of readable code!

If we use list comprehensions and/or maps and the built-in sum function
~~~
def std_dev(sample):
    sample_mean = sum(sample) / len(sample)

    #sum_squared_devs = sum([(value - sample_mean)**2 for value in sample])
    sum_squared_devs = sum(map(lambda value: (value - sample_mean)**2, sample))

    return sqrt(sum_squared_devs / (len(sample) - 1))
~~~
{: .language-python}

We could do all this in one line, but is that a good idea?

~~~
def std_dev(sample):
    return sqrt(sum([(value - (sum(sample) / len(sample)))**2 for value in sample]))
~~~
{: .language-python}
Since it's now a 1 liner you migh be tempted to use that one liner instead in code. Why is that a bad idea?


## Documenting

The usual way to put documentation in software is
to add [comments]({{ page.root }}/reference.html#comment) like this:

~~~
# offset_mean(data, target_mean_value):
# return a new array containing the original data with its mean offset to match the desired value.
def offset_mean(data, target_mean_value):
    return (data - numpy.mean(data)) + target_mean_value
~~~
{: .language-python}

There's a better way, though.
If the first thing in a function is a string that isn't assigned to a variable,
that string is attached to the function as its documentation:

~~~
def offset_mean(data, target_mean_value):
    """Return a new array containing the original data
       with its mean offset to match the desired value."""
    return (data - numpy.mean(data)) + target_mean_value
~~~
{: .language-python}

This is better because we can now ask Python's built-in help system to show us
the documentation for the function:

~~~
help(offset_mean)
~~~
{: .language-python}

~~~
Help on function offset_mean in module __main__:

offset_mean(data, target_mean_value)
    Return a new array containing the original data with its mean offset to match the desired value.
~~~
{: .output}

A string like this is called a [docstring]({{ page.root }}/reference.html#docstring).
We don't need to use triple quotes when we write one,
but if we do,
we can break the string across multiple lines:

~~~
def offset_mean(data, target_mean_value):
    """Return a new array containing the original data
       with its mean offset to match the desired value.

    Examples
    --------
    >>> offset_mean([1, 2, 3], 0)
    array([-1.,  0.,  1.])
    """
    return (data - numpy.mean(data)) + target_mean_value

help(offset_mean)
~~~
{: .language-python}

~~~
Help on function offset_mean in module __main__:

offset_mean(data, target_mean_value)
    Return a new array containing the original data
       with its mean offset to match the desired value.

    Examples
    --------
    >>> offset_mean([1, 2, 3], 0)
    array([-1.,  0.,  1.])
~~~
{: .output}


{% include links.md %}
