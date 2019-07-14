#!/usr/bin/env python3

cipher = [[1, 48, 53, 53, 138], [13, 69, 123, 2, 103, 151], [4, 6, 1, 13, 26, 75, 102]]

_faf = open('./ls/Animal Farm.txt', 'r').read().split(' ') # 3
_f1984 = open('./ls/1984.txt', 'r').read().split(' ') # semua
_ftcintr = open('./ls/The Catcher in the Rye.txt', 'r').read().split(' ') # semua

text = [_faf, _f1984, _ftcintr]

for i in cipher[0]:
    print(_f1984[i-1][0])

for i in cipher[1]:
    print(_ftcintr[i-1][0])

for i in cipher[2]:
    print(_faf[i-1][0])

# NOT SOLVED
