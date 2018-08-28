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

    multiples_dict = defaultdict(set)  # Key: number, Value: list of numbers in l that can be divided evenly by number
    num_occurences = defaultdict(int)  # Key: number, Value: # times the number occurred in l.
    for i, li in enumerate(l):  # O(n^2) method of getting all divisors into a list.
        num_occurences[li] += 1
        for j, lj in enumerate(l[i+1:]):
            if li != lj and lj % li == 0:
                multiples_dict[li].add(lj)

    for number, occurrences in num_occurences.iteritems():
        if occurrences >= 3:  # We can make a lucky triple from JUST this number, as there are 3 or more.
            triples_count += 1
            print((number,)*3)

        if occurrences >= 2:  # We have (x, x) so we can make a lucky triple with all numbers that are divisible by x.
            if number in multiples_dict:  # If there are numbers divisible by x (var "number" is x in this case)
                triples_count += len(multiples_dict[number])
                for n in multiples_dict[number]:
                    print((number,)*2+(n,))

    for number, mult_set in multiples_dict.iteritems():  # For each number with multiples in the list (number, ?, ?)
        for multiple in mult_set:  # For each multiple of the number (number, multiple, ?)
            if num_occurences[multiple] >= 2:  # We can do a lucky triple of x,y,y where x=number and y=multiple.
                triples_count += 1
                print((number,)+(multiple,)*2)

            if multiple in multiples_dict:  # For each multiple of the multiple of the number (number, multiple, multiples[multiple])
                triples_count += len(multiples_dict[multiple])
                for n in multiples_dict[multiple]:
                    print((number, multiple, n))

    return triples_count
