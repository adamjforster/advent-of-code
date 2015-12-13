#!/usr/bin/python

from collections import deque


def is_nice(string):
    return (
        has_pair_repetition(string) and
        has_one_space_repetition(string)
    )


def has_pair_repetition(string):
    length = len(string)
    pairs = deque([line[index:index + 2] for index in xrange(length) if index != length - 1])
    while pairs:
        pair = pairs.popleft()
        if pair in list(pairs)[1:]:
            return True
    return False


def has_one_space_repetition(string):
    for index, c in enumerate(string):
        if index < 2:
            continue
            
        if c == string[index - 2] != string[index - 1]:
            return True
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
