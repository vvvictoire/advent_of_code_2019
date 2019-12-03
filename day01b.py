#!/usr/bin/python3

from math import floor

def compute_fuel(weight):
    fuel = floor(weight / 3) - 2
    if fuel > 0:
        return fuel + compute_fuel(fuel)
    return 0

total_fuel = 0
with open('data/01a_input') as f:
    lines = f.readlines()
    for line in lines:
        module_weight = int(line)
        fuel_needed = compute_fuel(module_weight)
        total_fuel += fuel_needed

print(total_fuel)
