# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals


with open('input.txt', 'r') as f:
    print(sum(int(value) for value in f))
