from collections import defaultdict

"""
Find the Access Codes
=====================

In order to destroy Commander Lambda's LAMBCHOP doomsday device, you'll need access to it.
But the only door leading to the LAMBCHOP chamber is secured with a unique lock system whose number of passcodes changes daily.
Commander Lambda gets a report every day that includes the locks' access codes,
but only she knows how to figure out which of several lists contains the access codes.
You need to find a way to determine which list contains the access codes once you're ready to go in.

Fortunately, now that you're Commander Lambda's personal assistant, she's confided to you that she made all
the access codes "lucky triples" in order to help her better find them in the lists.
A "lucky triple" is a tuple (x, y, z) where x divides y and y divides z, such as (1, 2, 4).
With that information, you can figure out which list contains the number of access codes that matches the number
of locks on the door when you're ready to go in (for example, if there's 5 passcodes, you'd need to find a list with 5 "lucky triple" access codes).

Write a function answer(l) that takes a list of positive integers l and counts the number of "lucky triples" of
(li, lj, lk) where the list indices meet the requirement i < j < k.  The length of l is between 2 and 2000 inclusive.
The elements of l are between 1 and 999999 inclusive.  The answer fits within a signed 32-bit integer.
Some of the lists are purposely generated without any access codes to throw off spies, so if no triples are found, return 0.

For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], making the answer 3 total.
"""


def lucky_triples(l):
    # Factoring is hard when you don't have a quantum computer to run Shor's algorithm.
    triples_count = 0

    divisibles_dict = defaultdict(list)
    special_cases = defaultdict(list)
    for i, li in enumerate(l):  # O(n^2) method of getting all divisors into a list.
        for j, lj in enumerate(l[i+1:]):
            if li == lj:  # Special case.
                special_cases[li].append(lj)
            elif lj % li == 0:
                divisibles_dict[li].append(lj)

    for number, num_list in special_cases.iteritems():
        triples_count += len(num_list) / 3  # +1 if there are 3 elements.

        if len(num_list) >= 2:
            triples_count += len(divisibles_dict[number])  # If we've got (x,x), then we can make a lucky pair with all numbers divisible by x.

    for number, div_list in divisibles_dict.iteritems():
        for divisible in div_list:
            if divisible in divisibles_dict:
                triples_count += len(divisibles_dict[divisible])

    return triples_count