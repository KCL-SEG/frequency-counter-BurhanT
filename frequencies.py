"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i=0 to len(items)-1:
        item = items[i]
        item = str(item)
        if item in frequencies:
            item_amount = frequencies.get(item) + 1
            frequencies.pop(item)
            frequencies.update({item: item_amount})
        else:
            frequencies.update({item}: 1)
    return frequencies
