"""
I Love Lance & Janice
=====================
You've caught two of your fellow minions passing coded notes back and forth - while they're on duty, no less! Worse, you're pretty sure it's not job-related - they're both huge fans of the space soap opera "Lance & Janice". You know how much Commander Lambda hates waste, so if you can prove that these minions are wasting her time passing non-job-related notes, it'll put you that much closer to a promotion.
Fortunately for you, the minions aren't exactly advanced cryptographers. In their code, every lowercase letter [a..z] is replaced with the corresponding one in [z..a], while every other character (including uppercase letters and punctuation) is left untouched.  That is, 'a' becomes 'z', 'b' becomes 'y', 'c' becomes 'x', etc.  For instance, the word "vmxibkgrlm", when decoded, would become "encryption".
Write a function called answer(s) which takes in a string and returns the deciphered string so you can show the commander proof that these minions are talking about "Lance & Janice" instead of doing their jobs.

Languages
=========
To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========
Inputs:
    (string) s = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"
Output:
    (string) "did you see last night's episode?"

Inputs:
    (string) s = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
Output:
    (string) "Yeah! I can't believe Lance lost his job at the colony!!"
"""


def decode(char):
    char_ascii = ord(char)

    # Define shifting boundaries. Minions are only shifting letters, not punctuation or white space.
    min_lower = ord('a')  # a (ascii) = 97
    max_lower = ord('z')  # z (ascii) = 122
    min_upper = ord('A')  # A (ascii) = 65
    max_upper = ord('Z')  # Z (ascii) = 90

    shift = 26  # The minions are shifting letters by 26. A=Z, Z=A, ...

    new_ord = char_ascii + shift - 1
    if min_lower <= char_ascii <= max_lower:
        if new_ord > max_lower:
            new_ord = min_lower + (new_ord - max_lower)
    elif min_upper <= char_ascii <= max_upper:
        if new_ord > max_upper:
            new_ord = min_upper + (new_ord - max_upper)
    else:
        return char

    return chr(new_ord)


def answer(s):
    ans = ''
    for char in s:  # Iterate through each character
        ans += decode(char)
    return ans
