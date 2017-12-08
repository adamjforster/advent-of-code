# -*- coding: utf-8 -*-

with open('input.txt', 'r') as f:
    digits = f.read().strip()
    
    total = 0
    previous = int(digits[-1])

    for digit in digits:
        digit = int(digit)
        if digit == previous:
            total += digit
        previous = digit

    print total
