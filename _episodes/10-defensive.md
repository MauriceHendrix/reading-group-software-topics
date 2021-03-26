---
title: Defensive Programming
teaching: 25
exercises: 0
questions:
- "How can I make my programs more reliable?"
objectives:
- "Explain what an assertion is."
- "Add assertions that check the program's state is correct."
- "Correctly add precondition and postcondition assertions to functions."
- "Explain what test-driven development is, and use it when creating new functions."
- "Explain why variables should be initialized using actual data values
   rather than arbitrary constants."
keypoints:
- "Program defensively, i.e., assume that errors are going to arise,
   and write code to detect them when they do."
- "Put assertions in programs to check their state as they run,
   and to help readers understand how those programs are supposed to work."
- "Use preconditions to check that the inputs to a function are safe to use."
- "Use postconditions to check that the output from a function is safe to use."
- "Write tests before writing code in order to help determine exactly
   what that code is supposed to do."
---

Our previous lessons have introduced the basic tools of programming:
variables and lists,
file I/O,
loops,
conditionals,
and functions.
What they *haven't* done is show us how to tell
whether a program is getting the right answer,
and how to tell if it's *still* getting the right answer
as we make changes to it.

To achieve that,
we need to:

*   Write programs that check their own operation.
*   Write and run tests for widely-used functions.
*   Make sure we know what "correct" actually means.

The good news is,
doing these things will speed up our programming,
not slow it down.
As in real carpentry --- the kind done with lumber --- the time saved
by measuring carefully before cutting a piece of wood
is much greater than the time that measuring takes.

## Assertions

The first step toward getting the right answers from our programs
is to assume that mistakes *will* happen
and to guard against them.
This is called [defensive programming]({{ page.root }}/reference.html#defensive-programming),
and the most common way to do it is to add
[assertions]({{ page.root }}/reference.html#assertion) to our code
so that it checks itself as it runs.
An assertion is simply a statement that something must be true at a certain point in a program.
When Python sees one,
it evaluates the assertion's condition.
If it's true,
Python does nothing,
but if it's false,
Python halts the program immediately
and prints the error message if one is provided.
For example,
this piece of code halts as soon as the loop encounters a value that isn't positive:

~~~
numbers = [1.5, 2.3, 0.7, -0.001, 4.4]
total = 0.0
for num in numbers:
    assert num > 0.0, 'Data should only contain positive values'
    total += num
print('total is:', total)
~~~
{: .language-python}

~~~
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-19-33d87ea29ae4> in <module>()
      2 total = 0.0
      3 for num in numbers:
----> 4     assert num > 0.0, 'Data should only contain positive values'
      5     total += num
      6 print('total is:', total)

AssertionError: Data should only contain positive values
~~~
{: .error}

Programs like the Firefox browser are full of assertions:
10-20% of the code they contain
are there to check that the other 80–90% are working correctly.
Broadly speaking,
assertions fall into three categories:

*   A [precondition]({{ page.root }}/reference.html#precondition)
    is something that must be true at the start of a function in order for it to work correctly.

*   A [postcondition]({{ page.root }}/reference.html#postcondition)
    is something that the function guarantees is true when it finishes.

*   An [invariant]({{ page.root }}/reference.html#invariant)
    is something that is always true at a particular point inside a piece of code.

For example,
suppose we are representing rectangles using a [tuple]({{ page.root }}/reference.html#tuple)
of four coordinates `(x0, y0, x1, y1)`,
representing the lower left and upper right corners of the rectangle.
In order to do some calculations,
we need to normalize the rectangle so that the lower left corner is at the origin
and the longest side is 1.0 units long.
This function does that,
but checks that its input is correctly formatted and that its result makes sense:

~~~
def normalize_rectangle(rect):
    """Normalizes a rectangle so that it is at the origin and 1.0 units long on its longest axis.
    Input should be of the format (x0, y0, x1, y1).
    (x0, y0) and (x1, y1) define the lower left and upper right corners
    of the rectangle, respectively."""
    assert len(rect) == 4, 'Rectangles must contain 4 coordinates'
    x0, y0, x1, y1 = rect
    assert x0 < x1, 'Invalid X coordinates'
    assert y0 < y1, 'Invalid Y coordinates'

    dx = x1 - x0
    dy = y1 - y0
    if dx > dy:
        scaled = float(dx) / dy
        upper_x, upper_y = 1.0, scaled
    else:
        scaled = float(dx) / dy
        upper_x, upper_y = scaled, 1.0

    assert 0 < upper_x <= 1.0, 'Calculated upper X coordinate invalid'
    assert 0 < upper_y <= 1.0, 'Calculated upper Y coordinate invalid'

    return (0, 0, upper_x, upper_y)
~~~
{: .language-python}

The preconditions on lines 6, 8, and 9 catch invalid inputs:

~~~
print(normalize_rectangle( (0.0, 1.0, 2.0) )) # missing the fourth coordinate
~~~
{: .language-python}

~~~
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-2-1b9cd8e18a1f> in <module>
----> 1 print(normalize_rectangle( (0.0, 1.0, 2.0) )) # missing the fourth coordinate

<ipython-input-1-c94cf5b065b9> in normalize_rectangle(rect)
      4     (x0, y0) and (x1, y1) define the lower left and upper right corners
      5     of the rectangle, respectively."""
----> 6     assert len(rect) == 4, 'Rectangles must contain 4 coordinates'
      7     x0, y0, x1, y1 = rect
      8     assert x0 < x1, 'Invalid X coordinates'

AssertionError: Rectangles must contain 4 coordinates
~~~
{: .error}

The post-conditions on lines 20 and 21 help us catch bugs by telling us when our
calculations might have been incorrect.
For example, if we normalize a rectangle that's wider than it is tall,
the assertion is triggered:

~~~
print(normalize_rectangle( (0.0, 0.0, 5.0, 1.0) ))
~~~
{: .language-python}

~~~
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-5-8d4a48f1d068> in <module>
----> 1 print(normalize_rectangle( (0.0, 0.0, 5.0, 1.0) ))

<ipython-input-1-c94cf5b065b9> in normalize_rectangle(rect)
     19
     20     assert 0 < upper_x <= 1.0, 'Calculated upper X coordinate invalid'
---> 21     assert 0 < upper_y <= 1.0, 'Calculated upper Y coordinate invalid'
     22
     23     return (0, 0, upper_x, upper_y)

AssertionError: Calculated upper Y coordinate invalid
~~~
{: .error}

## Test-Driven Development

An assertion checks that something is true at a particular point in the program.
The next step is to check the overall behavior of a piece of code,
i.e.,
to make sure that it produces the right output when it's given a particular input.
For example,
suppose we need to find where two or more time series overlap.
The range of each time series is represented as a pair of numbers,
which are the time the interval started and ended.
The output is the largest range that they all include:

![Overlapping Ranges](../fig/python-overlapping-ranges.svg)

Most novice programmers would solve this problem like this:

1.  Write a function `range_overlap`.
2.  Call it interactively on two or three different inputs.
3.  If it produces the wrong answer, fix the function and re-run that test.

This clearly works --- after all, thousands of scientists are doing it right now --- but
there's a better way:

1.  Write a short function for each test.
2.  Write a `range_overlap` function that should pass those tests.
3.  If `range_overlap` produces any wrong answers, fix it and re-run the test functions.

Writing the tests *before* writing the function they exercise
is called [test-driven development]({{ page.root }}/reference.html#test-driven-development) (TDD).
Its advocates believe it produces better code faster because:

1.  If people write tests after writing the thing to be tested,
    they are subject to confirmation bias,
    i.e.,
    they subconsciously write tests to show that their code is correct,
    rather than to find errors.
2.  Writing tests helps programmers figure out what the function is actually supposed to do.

Here are three test functions for `range_overlap`:

~~~
assert range_overlap([ (0.0, 1.0) ]) == (0.0, 1.0)
assert range_overlap([ (2.0, 3.0), (2.0, 4.0) ]) == (2.0, 3.0)
assert range_overlap([ (0.0, 1.0), (0.0, 2.0), (-1.0, 1.0) ]) == (0.0, 1.0)
~~~
{: .language-python}

~~~
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-25-d8be150fbef6> in <module>()
----> 1 assert range_overlap([ (0.0, 1.0) ]) == (0.0, 1.0)
      2 assert range_overlap([ (2.0, 3.0), (2.0, 4.0) ]) == (2.0, 3.0)
      3 assert range_overlap([ (0.0, 1.0), (0.0, 2.0), (-1.0, 1.0) ]) == (0.0, 1.0)

AssertionError:
~~~
{: .error}

The error is actually reassuring:
we haven't written `range_overlap` yet,
so if the tests passed,
it would be a sign that someone else had
and that we were accidentally using their function.

And as a bonus of writing these tests,
we've implicitly defined what our input and output look like:
we expect a list of pairs as input,
and produce a single pair as output.

Something important is missing, though.
We don't have any tests for the case where the ranges don't overlap at all or one bound is the same:

~~~
assert range_overlap([ (0.0, 1.0), (5.0, 6.0) ]) == ???
assert range_overlap([ (0.0, 1.0), (1.0, 2.0) ]) == ???
~~~
{: .language-python}

We're now ready to do so:

~~~
def range_overlap(ranges):
    """Return common overlap among a set of [left, right] ranges."""
    max_left = 0.0
    min_right = 1.0
    for (left, right) in ranges:
        max_left = max(max_left, left)
        min_right = min(min_right, right)
    return (max_left, min_right)
~~~
{: .language-python}

Take a moment to think about why we calculate the left endpoint of the overlap as
the maximum of the input left endpoints, and the overlap right endpoint as the minimum
of the input right endpoints.
We'd now like to re-run our tests,
but they're scattered across three different cells.
To make running them easier,
let's put them all in a function:

~~~
def test_range_overlap():
    assert range_overlap([ (0.0, 1.0), (5.0, 6.0) ]) == None
    assert range_overlap([ (0.0, 1.0), (1.0, 2.0) ]) == None
    assert range_overlap([ (0.0, 1.0) ]) == (0.0, 1.0)
    assert range_overlap([ (2.0, 3.0), (2.0, 4.0) ]) == (2.0, 3.0)
    assert range_overlap([ (0.0, 1.0), (0.0, 2.0), (-1.0, 1.0) ]) == (0.0, 1.0)
    assert range_overlap([]) == None
~~~
{: .language-python}

We can now test `range_overlap` with a single function call:

~~~
test_range_overlap()
~~~
{: .language-python}

## Automated tests
With pytest we can run such tests automaticly. All that's needed is:
- pytest installed:  `pip install pytest`
- tests are methods that start with `test_`
- files that are considered by pytest start with `test_`
- navigate to your code folder and run `pytest`
- within a python package tests are usually located in a tests folder

### Some useful advanced features:
- capsys / caplog to check what is in system outputs :
- tmp_path gives a temporary path where you can store files
- unittest.mock can mock passing command line arguments
~~~
def test_script_convert(caplog, tmp_path):
    """Convert a normal model via command line script"""
    model_file = os.path.join(CELLML_FOLDER, 'fox_mcharg_gilmour_2002' + '.cellml')
    assert os.path.isfile(model_file)
    target = os.path.join(tmp_path, model_name + '.cellml')
    shutil.copyfile(model_file, target)

    testargs = ['chaste_codegen', '--skip-ingularity-fixes', target]
    # Call commandline script
    with mock.patch.object(sys, 'argv', testargs):
        chaste_codegen()
        assert "The model has no capacitance tagged." in caplog.text

    reference = os.path.join(os.path.join(TESTS_FOLDER), 'chaste_reference_models', 'Normal')
    compare_file_against_reference(os.path.join(reference, model_name + '_console_script.cpp'),
                                   os.path.join(tmp_path, model_name + '.cpp'))
~~~
{: .language-python}

- fixtures allow you to srae things amoung multiple tests
~~~
def test_script_convert(caplog, tmp_path):
@pytest.fixture(scope='session')
def hh_model():
    model_name = os.path.join(CELLML_FOLDER, 'hodgkin_huxley_squid_axon_model_1952_modified.cellml')
    return load_model(model_name)

def test_partial_eval(hh_model):
...
~~~
{: .language-python}

- parameterisation allows running the same test on multiple inputs e.g.

chaste_normal_models = ...

@pytest.mark.parametrize(('model'), chaste_normal_models)
def test_Normal(model):
   ...

### Coverage
Code coverage is an interesting metric. Itindicated how much of the code is being run during the tests and generally gives a good indication of how complete the tests are. However it's worth keeping in mind that it's not a perfect measure.
To use it:
- install pytest-cov `pip install pytst-cov`
- then run `pytest --cov --cov-report term-missing`

### Linting & input sorting
flake8 and isort respectively test that your code is formatted following python's standard code style and that imports are ordered correctly according to this standard. Both tools can be installed via pip.

### Linking to github
When using test-driven development it's possible to automate these tests and checks even further and let your version control system run them (e.g. github)
For example in the chaste_codegen project we do:
- to make changes we make a new branch
- when ready we make a pull request that runs these checks and asks for a review
This makes it much less likley that you forget to run the checks. Also ou catch issues with code relying in files or components that you happen to have but aren't part of the codebase.
[Example pull request](https://github.com/ModellingWebLab/cellmlmanip/pull/334)
{% include links.md %}
