#!/usr/bin/python

import hashlib

secret = 'iwrupvqb'

index = 1
while True:
    digest = hashlib.md5('{}{}'.format(secret, index)).hexdigest()
    if digest.startswith('00000'):
        print '{} - {}'.format(index, digest)
        break
    index += 1
