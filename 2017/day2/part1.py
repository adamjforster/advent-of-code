# -*- coding: utf-8 -*-

with open('input.txt', 'r') as f:
    check_sum = 0
    
    for line in f:
        row = map(int, line.split())
        check_sum += max(row) - min(row)
    
    print check_sum
