# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from collections import Counter


with open('input.txt', 'r') as f:
    twos = set()
    threes = set()
    
    for box_id in f:
        counter = Counter(box_id.strip('\n'))
        for letter in box_id:
            if counter[letter] == 2:
                twos.add(box_id)
            elif counter[letter] == 3:
                threes.add(box_id)
                
    print(len(twos) * len(threes))
        
