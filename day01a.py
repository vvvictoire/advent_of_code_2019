#!/usr/bin/python3

from math import floor

total_fuel = 0
with open('data/01a_input') as f:
    lines = f.readlines()
    for line in lines:
        module_weight = int(line)
        fuel_needed = floor(module_weight / 3) - 2
        total_fuel += fuel_needed

print(total_fuel)
    