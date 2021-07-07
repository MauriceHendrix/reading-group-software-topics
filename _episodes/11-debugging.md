---
title: Debugging
teaching: 20
exercises: 0
questions:
- "How can I debug my program?"
objectives:
- "Debug code containing an error systematically."
- "Identify ways of making code less error-prone and more easily tested."
keypoints:
- "Know what code is supposed to do *before* trying to debug it."
- "Make it fail every time."
- "Make it fail fast."
- "Change one thing at a time, and for a reason."
- "Keep track of what you've done."
---

Once testing has uncovered problems,
the next step is to fix them.
Many novices do this by making more-or-less random changes to their code
until it seems to produce the right answer,
but that's very inefficient
(and the result is usually only correct for the one case they're testing).
The more experienced a programmer is,
the more systematically they debug,
and most follow some variation on the rules explained below.

## Know What It's Supposed to Do

The first step in debugging something is to
*know what it's supposed to do*.
"My program doesn't work" isn't helpful:
in order to diagnose and fix problems,
we need to be able to tell correct output from incorrect.
If we can write a test case for the failing case --- i.e.,
if we can assert that with *these* inputs,
the function should produce *that* result ---
then we're ready to start debugging.
If we can't,
then we need to figure out how we're going to know when we've fixed things.

Suggestions to make things easier:

1.  *Test with simplified data.*
    Before doing statistics on a real data set,
    we should try calculating statistics for a single record,
    for two identical records,
    for two records whose values are one step apart,
    or for some other case where we can calculate the right answer by hand.

2.  *Test a simplified case.*
    If our program is supposed to simulate
    magnetic eddies in rapidly-rotating blobs of supercooled helium,
    our first test should be a blob of helium that isn't rotating,
    and isn't being subjected to any external electromagnetic fields.
    Similarly,
    if we're looking at the effects of climate change on speciation,
    our first test should hold temperature, precipitation, and other factors constant.

3.  *Compare to an oracle.*
    A [test oracle]({{ page.root }}/reference.html#test-oracle)
    is something whose results are trusted,
    such as experimental data, an older program, or a human expert.
    We use test oracles to determine if our new program produces the correct results.
    If we have a test oracle,
    we should store its output for particular cases
    so that we can compare it with our new results as often as we like
    without re-running that program.

4.  *Visualize.*
    Data analysts frequently use simple visualizations to check both
    the science they're doing
    and the correctness of their code
    (just as we did in the [opening lesson]({{ page.root }}/01-numpy/) of this tutorial).
    This should only be used for debugging as a last resort,
    though,
    since it's very hard to compare two visualizations automatically.

## Make It Fail Every Time

We can only debug something when it fails,
so the second step is always to find a test case that
*makes it fail every time*.
The "every time" part is important because
few things are more frustrating than debugging an intermittent problem:
if we have to call a function a dozen times to get a single failure,
the odds are good that we'll scroll past the failure when it actually occurs.

As part of this,
it's always important to check that our code is "plugged in",
i.e.,
that we're actually exercising the problem that we think we are.
Every programmer has spent hours chasing a bug,
only to realize that they were actually calling their code on the wrong data set
or with the wrong configuration parameters,
or are using the wrong version of the software entirely.
Mistakes like these are particularly likely to happen when we're tired,
frustrated,
and up against a deadline,
which is one of the reasons late-night (or overnight) coding sessions
are almost never worthwhile.

Code depending on external things such as data from web pages, or code running in parallel can cause intermittent faults, these are very tough to fix, in this case try the code on a local version of the data and not in parallel if possible.

## Make It Fail Fast

If it takes 20 minutes for the bug to surface,
we can only do three experiments an hour.
This means that we'll get less data in more time and that
we're more likely to be distracted by other things as we wait for our program to fail,
which means the time we *are* spending on the problem is less focused.
It's therefore critical to *make it fail fast*.

As well as making the program fail fast in time,
we want to make it fail fast in space,
i.e.,
we want to localize the failure to the smallest possible region of code:

1.  The smaller the gap between cause and effect,
    the easier the connection is to find.
    Many programmers therefore use a divide and conquer strategy to find bugs,
    i.e.,
    if the output of a function is wrong,
    they check whether things are OK in the middle,
    then concentrate on either the first or second half,
    and so on.

2.  N things can interact in N! different ways,
    so every line of code that *isn't* run as part of a test
    means more than one thing we don't need to worry about.

## Change One Thing at a Time, For a Reason

Replacing random chunks of code is unlikely to do much good.
(After all,
if you got it wrong the first time,
you'll probably get it wrong the second and third as well.)
Good programmers therefore
*change one thing at a time, for a reason*.
They are either trying to gather more information
("is the bug still there if we change the order of the loops?")
or test a fix
("can we make the bug go away by sorting our data before processing it?").

Every time we make a change,
however small,
we should re-run our tests immediately,
because the more things we change at once,
the harder it is to know what's responsible for what
(those N! interactions again).
And we should re-run *all* of our tests:
more than half of fixes made to code introduce (or re-introduce) bugs,
so re-running all of our tests tells us whether we have regressed.

## Keep Track of What You've Done

Write notes and/or comments and when done check the cahnged in using version control (git). That way you can find things back later if needed.

## Using a debugger (demo)
Many programmers use print statements and asserts, whcih is fine. however if things get complex it can be difficult to know in advance what to print and what to assert. A debugger can help.

{% include links.md %}
