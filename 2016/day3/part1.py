#!/usr/bin/python


def is_possible(*args):
    (a, b, c) = map(int, *args)
    return (a + b > c) and (b + c > a) and (c + a > b)


with open('input.txt', 'r') as f:
    print len([True for line in f if is_possible(line.split())])
