from collections import defaultdict

"""
Bunny Prisoner Locating
=======================

Keeping track of Commander Lambda's many bunny prisoners is starting to get tricky.
You've been tasked with writing a program to match bunny prisoner IDs to cell locations.

The LAMBCHOP doomsday device takes up much of the interior of Commander Lambda's space station, and as a result the prison blocks have an unusual layout.
They are stacked in a triangular shape, and the bunny prisoners are given numerical IDs starting from the corner, as follows:

| 7
| 4 8
| 2 5 9
| 1 3 6 10
------------

Each cell can be represented as points (x, y), with x being the distance from the vertical wall, and y being the height from the ground.
For example, the bunny prisoner at (1, 1) has ID 1, the bunny prisoner at (3, 2) has ID 9, and the bunny prisoner at (2,3) has ID 8.
This pattern of numbering continues indefinitely (Commander Lambda has been taking a LOT of prisoners).

Write a function answer(x, y) which returns the prisoner ID of the bunny at location (x, y).
Each value of x and y will be at least 1 and no greater than 100,000.
Since the prisoner ID can be very large, return your answer as a string representation of the number.
"""


def bunny_prisoner_answer(x, y):
    # The cell number at the ground floor follows the pattern of
    # ID = x^2 + x
    #      -------
    #         2
    ans = (x**2 + x)/2  # Calculate the number at (x, 1)

    ans_y = 1
    while ans_y != y:  # Move up one cell from the ground
        ans += (x - 1) + ans_y
        ans_y += 1

    # Sum of (x-1+k) from 1 to y
    # is 2xy + y^2 - y
    #    -------------
    #         2

    return str(ans)


"""
Elevator Maintenance
====================

You've been assigned the onerous task of elevator maintenance - ugh!
It wouldn't be so bad, except that all the elevator documentation has been lying in a disorganized pile at the bottom of a filing cabinet for years,
and you don't even know what elevator version numbers you'll be working on. 

Elevator versions are represented by a series of numbers, divided up into major, minor and revision integers.
New versions of an elevator increase the major number, e.g. 1, 2, 3, and so on.
When new features are added to an elevator without being a complete new version, a second number named "minor" can be used to represent those new additions, e.g. 1.0, 1.1, 1.2, etc.
Small fixes or maintenance work can be represented by a third number named "revision", e.g. 1.1.1, 1.1.2, 1.2.0, and so on.
The number zero can be used as a major for pre-release versions of elevators, e.g. 0.1, 0.5, 0.9.2, etc
(Commander Lambda is careful to always beta test her new technology, with her loyal henchmen as subjects!).

Given a list of elevator versions represented as strings, write a function answer(l) that returns the same list sorted in ascending order by major, minor, and revision number so that you can identify the current elevator version.
The versions in list l will always contain major numbers, but minor and revision numbers are optional.
If the version contains a revision number, then it will also have a minor number.

For example, given the list l as ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"],
the function answer(l) would return the list ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"].
If two or more versions are equivalent but one version contains more numbers than the others, then these versions must be sorted ascending based on how many numbers they have, e.g ["1", "1.0", "1.0.0"].
The number of elements in the list l will be at least 1 and will not exceed 100.
"""


def bucketize_by_split_index(l, index, sep='.'):
    buckets = defaultdict(list)
    for version in l:
        split_ver = version.split(sep)
        num = int(split_ver[index]) if len(split_ver) > index else None
        buckets[num].append(version)

    return buckets.values()

def nested_final_bucket_to_list(final_bucket):
    ret_list = list()
    for minor_bucket in final_bucket:
        for rev_bucket in minor_bucket:
            ret_list.append(rev_bucket[0])

    return ret_list

def elevator_maintenance(l):
    major_buckets = bucketize_by_split_index(l, 0)
    print(major_buckets)

    minor_buckets = []
    for bucket in major_buckets:
        minor_buckets.append(bucketize_by_split_index(bucket, 1))
    print(minor_buckets)

    rev_buckets = []
    for something in minor_buckets:
        for bucket in something:
            rev_buckets.append(bucketize_by_split_index(bucket, 2))
    print(rev_buckets)

    return nested_final_bucket_to_list(rev_buckets)

