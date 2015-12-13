#!/usr/bin/python


VOWELS = 'aeiou'
NAUGHTY_PAIRS = ['ab', 'cd', 'pq', 'xy']


def is_nice(string):
    return (
        not contains_naughty_pair(string) and
        num_vowels(string) >= 3 and
        has_adjacent_repetition(string)
    )


def contains_naughty_pair(string):
    for pair in NAUGHTY_PAIRS:
        if pair in string:
            return True
    return False
    
    
def num_vowels(string):
    return sum(string.count(v) for v in VOWELS)


def has_adjacent_repetition(string):
    last_char = ''
    for c in string:
        if c == last_char:
            return True
        last_char = c
    return False
    

with open('input.txt', 'r') as f:
    naughty = []
    nice = []
    
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        if is_nice(line):
            nice.append(line)
        else:
            naughty.append(line)
            
    print len(nice)
