#!/usr/bin/python3

# X axis is (negatives) W-E (positives)
# Y axis is (negatives) S-N (positives)
# (X, Y)
NORTH = (0, 1)
SOUTH = (0, -1)
EAST = (1, 0)
WEST = (-1, 0)

def get_direction_tuple(direction):
    if direction == 'U':
        return NORTH
    elif direction == 'D':
        return SOUTH
    elif direction == 'R':
        return EAST
    elif direction == 'L':
        return WEST
    else:
        raise Exception

def addition(point_a, point_b):
    return (point_a[0] + point_b[0], point_a[1] + point_b[1])

def parse_wire(wire_path_string):
    wire_path_splitted = wire_path_string.split(',')
    wire_path = []
    for element in wire_path_splitted:
        direction = element[0]
        quantity = int(element[1:])
        parsed_element = (direction, quantity)
        wire_path.append(parsed_element)
    return wire_path

def compute_wire(wire_path):
    nodes = []
    current_node = (0,0)
    for element in wire_path:
        direction_str = element[0]
        quantity = element[1]
        direction = get_direction_tuple(direction_str)
        for _ in range(quantity):
            current_node = addition(current_node, direction)
            nodes.append(current_node)
    return nodes

def compare_nodes(wire_a, wire_b) :
    set_a = set(wire_a)
    set_b = set(wire_b)
    return set_a & set_b

def manhattan_distance(point_a, point_b):
    return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])

def manhattan_distance_from_center(point):
    return manhattan_distance(point, (0, 0))

def get_minimal_distance(common_nodes):
    minimal_distance = float("inf")
    minimal_node = (0, 0)
    for node in common_nodes:
        distance = manhattan_distance_from_center(node)
        if distance < minimal_distance:
            minimal_node = node
            minimal_distance = distance
    return (minimal_node, minimal_distance)

with open('data/03a_input') as f:
    string_a = f.readline()
    string_b = f.readline()
    wire_a = parse_wire(string_a)
    nodes_a = compute_wire(wire_a)
    wire_b = parse_wire(string_b)
    nodes_b = compute_wire(wire_b)
    common_nodes = compare_nodes(nodes_a, nodes_b)
    print(get_minimal_distance(common_nodes))
