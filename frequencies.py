"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in range(len(items)):
        item = items[i]
        item = str(item)
        if item in frequencies:
            freq = frequencies.get(item) + 1
            frequencies.pop(item)
            frequencies.update({item: freq})
        else:
            frequencies.update({item: 1})
    return frequencies
