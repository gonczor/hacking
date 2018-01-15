#!/usr/bin/env python

with open('input.txt') as f:
    data = [int(line) for line in f.readlines()]

for _ in range(len(data)):
    for i in range(len(data)-1):
        if data[i] > data[i+1]:
            data[i], data[i+1] = data[i+1], data[i]

with open('output.txt', 'w') as f:
    f.write(data)

