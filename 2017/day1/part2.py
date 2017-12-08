# -*- coding: utf-8 -*-

with open('input.txt', 'r') as f:
    digits = f.read().strip()
    
    total = 0
    offset = len(digits) / 2

    for index, digit in enumerate(digits):
        digit = int(digit)
        previous = int(digits[index - offset])
        
        if digit == previous:
            total += digit
        previous = digit

    print total
