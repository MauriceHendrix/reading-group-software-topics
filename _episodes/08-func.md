---
title: Readable code
teaching: 5
exercises: 0
questions:
- "Writing readable code"
objectives:
- "Understand how to make code more readable"
keypoints:
- "Code readability."
---
## Readable functions

Consider the following function:

~~~
def s(p):
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



{% include links.md %}
