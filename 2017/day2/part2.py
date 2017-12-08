# -*- coding: utf-8 -*-


def even_division_result(row):
    for i, cell_i in enumerate(row):
        for j, cell_j in enumerate(row):
            if i == j:
                continue
                
            if cell_i % cell_j == 0:
                yield cell_i / cell_j


with open('input.txt', 'r') as f:
    total = 0
    
    for line in f:
        row = sorted(map(int, line.split()), reverse=True)
        total += sum(even_division_result(row))
        
    print total
