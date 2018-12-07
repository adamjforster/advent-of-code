# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals


def hamming_distance(s1, s2):
    return sum(char_1 != char_2 for char_1, char_2 in zip(s1, s2))


with open('input.txt', 'r') as f:
    box_ids = [box_id.strip('\n') for box_id in list(f)]
    
    for id_1 in box_ids:
        for id_2 in box_ids:
            diff = hamming_distance(id_1, id_2)
            if diff == 1:
                print(''.join(char_1 for char_1, char_2 in zip(id_1, id_2) if char_1 == char_2))
