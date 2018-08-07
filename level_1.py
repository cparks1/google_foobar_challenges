"""
I Love Lance & Janice
=====================
You've caught two of your fellow minions passing coded notes back and forth - while they're on duty, no less!
Worse, you're pretty sure it's not job-related - they're both huge fans of the space soap opera "Lance & Janice".
You know how much Commander Lambda hates waste, so if you can prove that these minions
are wasting her time passing non-job-related notes, it'll put you that much closer to a promotion.

Fortunately for you, the minions aren't exactly advanced cryptographers.
In their code, every lowercase letter [a..z] is replaced with the corresponding one in [z..a],
while every other character (including uppercase letters and punctuation) is left untouched.
That is, 'a' becomes 'z', 'b' becomes 'y', 'c' becomes 'x', etc.  For instance, the word "vmxibkgrlm", when decoded, would become "encryption".
Write a function called answer(s) which takes in a string and returns the deciphered string so you can show the commander proof that these minions are talking about "Lance & Janice" instead of doing their jobs.
"""

# Dictionary mapping each letter to its "opposite" character on the alphabet.
# I used the following python code to generate the dictionary, and then just printed it and pasted it into the solution,
# as running the code once to generate a dictionary that will be used multiple times is better than generating it
# on every import.
# I figured Cmd. Lambda would enjoy the minimal solution.

# Generation code:
# from string import ascii_uppercase, ascii_lowercase
# opposites_map = {}
# for i, char in enumerate(ascii_lowercase):
#   opposites_map[char] = ascii_lowercase[-i+1]
# for char, opposite in opposites_map.iteritems():
#   print("'%s': '%s,'" % (char, opposite))

# I then took the output and removed the extra comma at the end,
# placed the brackets around the data, and formatted it a little.

opposites_map = {
    'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n',
    'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'
}


def answer(s):
    """
    Decodes a given string, based on the parameters given.
    Those parameters being that only lowercase characters are shifted, and that uppercase and punctuation is untouched.
    :param s: String to decode.
    :return:  Decoded string.
    """
    ans = ''
    for char in s:  # Iterate through each character
        ans += opposites_map[char] if char in opposites_map else char
    return ans
