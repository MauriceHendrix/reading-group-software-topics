---
title: Performance testing & tips
teaching: 20
exercises: 0
questions:
- "How can I improve the performance of my program"
objectives:
- "Awareness of general software performance measures and techniques."
- "Awareness of python specific performance."
- "Know how to test performance."
---

We all want our code to run as fast as possibe. However sometimes it can be tricky to know why something is slow. In this section first some general techniques to meausre software performance, then some python specific issues and some measureing techniques.

## Measuring software performance

In formal computer science the performance of algorithms is described using what is known as big O notation. 
Big O notation is formally desined as:

![Big O definition](https://mauricehendrix.github.io/reading-group-software-topics/fig/0_cyqWw3UxODl-wqJi.jpg)

In a practical sense this means we measure the amount of operations as follows:
- a single operation is O(1)
- a loop through a list while doing stuff is O(N) we disregard constants so if there are 3 operations inside the loop we see O(N) and not O(3N).
- A loop in a loop: O(N^2), a loop in a loop in a loop O(n^3) etc.
- An algorithm that slits a list in 2 every step: O(log(N))
- Worst case: exponential O(c^N). E.g. plan the most efficient way for a traveling salesman. No other way than trying allpossible routes (though there are approximations)

**Example: Given list a list lst check that for every negative value it's square is also in the list**

### What is the big O of this implemntation?

~~~
def square_of_negative_in_list(lst):
    squares_in_list = True
    for v in lst:
        if v < 0:
            square_found = False
            for v2 in lst:
                square_found = square_found or v2 == v**2
            squares_in_list = squares_in_list and square_found
    return squares_in_list

~~~
{: .language-python}


### What is the big O of this implemntation?
~~~
def square_of_negative_in_list2(lst):
    found_squares = set()
    for v in lst:
        if v > 0:
            found_squares.add(v)
    for v in lst:
        if v < 0 and not v**2 in found_squares:
            return False
    return True
~~~
{: .language-python}


## Top tips

- Reduce work inside loops, list-, dicst-comprehensions etc.
- Especially avoid nested loops whenever possible, it can be worth going through a list multiple times just to avoid nesting!
- Sometimes sorting can be worth it if you can void nesting loops that way (best sorting algo is O(N log N).

## Tips for recursive algorithms
Any recursive algorithm can be written non-recursively (though it's not always straightforward).

Consider for example fibonacci numbers:
~~~
def fib(n):
    assert n >= 0, "Cannot calculate negative numbers"
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
~~~
{: .language-python}

We can speed this up really easily by keeping intermediate results:

### With some memory we can speed this up a lot:

~~~
fibo_numbers = [0,1]
def fib2(n):
    if n < len(fibo_numbers):
        return fibo_numbers[n]
    else:
        fib_num = fib2(n-1) + fib2(n-2)
        fibo_numbers.append(fib_num)
        return fib_num
~~~
{: .language-python}

### Turning recursive function non-recursive::

~~~
def fib3(n):
    fibo_numbers2 = [0,1]
    if n >= len(fibo_numbers2):
        for i in range(2, n+1):
            fibo_numbers2.append(fibo_numbers2[i-1] + fibo_numbers2[i-2])
    return fibo_numbers2[n]
~~~
{: .language-python}

## Testing software performance
Let's test these different implemntations. The easiest way is to run them on some (the same) sample data and time & compare.

~~~
import time

tic = time.time()
... code you want to time
toc = time.time()
print(toc-tic)
    
~~~
{: .language-python}

print('square_of_negative_in_list on list 1 takes': + str((toc-tic)/100))

## Python specific tips

Python has a distinction between mutable types (e.g. lists and string) and immutable types e.g. tuples and sets.
Looping over immutable types is slightly faster because python doesn't have to check for changes every step. However frequently creating a new tuple e.g. 

~~~
lst = []
for i in range(50000):
    lst.append(i)

tpl = tuple()
for i in range(50000):
    tpl = tpl + (i, )

~~~
{: .language-python}
You can also make use of this in other ways e.g.:

~~~
for v in list1:
    list1.append(v**2)
~~~
{: .language-python}

Will never finish! However the following adss the squares of the values in a list to the list just fine:

~~~
for v in tuple(list1):
    list1.append(v**2)
~~~
{: .language-python}

* Finally *
If there is a built-in python method you should probably use it as it's probably probably faster than what you can write. It may even have an underlying C implemntation. Many methods allow you flexibility e.g. sorting methods allow you to specify what to sort on. e.g.

~~~
example_dist_list = [{'name': 'Earth', 'num_moons': 1},
                     {'name': 'Jupiter', 'num_moons': 53},
                     {'name': 'Saturn', 'num_moons': 53},
                     {'name': 'Uranus', 'num_moons': 27},
                     {'name': 'Neptune', 'num_moons': 14}]

example_dist_list.sort(key=lambda p: p['num_moons'], reverse=True)
print(example_dist_list)
~~~
{: .language-python}

{% include links.md %}
