#!/usr/bin/python3

from copy import deepcopy

def add(program, pos):
    '''pos is the position of the opcode'''
    pos_first_number = program[pos + 1]
    pos_second_number = program[pos + 2]
    pos_result = program[pos + 3]
    first_number = program[pos_first_number]
    second_number = program[pos_second_number]
    result = first_number + second_number
    program[pos_result] = result
    return program

def multiply(program, pos):
    '''pos is the position of the opcode'''
    pos_first_number = program[pos + 1]
    pos_second_number = program[pos + 2]
    pos_result = program[pos + 3]
    first_number = program[pos_first_number]
    second_number = program[pos_second_number]
    result = first_number * second_number
    program[pos_result] = result
    return program

def execute_program(program):
    instruction_pointer = 0
    instruction = program[instruction_pointer]
    while True:
        instruction = program[instruction_pointer]
        if instruction == 1:
            program = add(program, instruction_pointer)
            instruction_pointer += 4
        elif instruction == 2:
            program = multiply(program, instruction_pointer)
            instruction_pointer += 4
        elif instruction == 99:
            #print(program[0])
            return program
        else:
            raise Exception
    return program

def parse_program(string):
    program = string.split(',')
    for index in range(len(program)):
        program[index] = int(program[index])
    return program

with open('data/02a_input') as f:
    program_string = f.read()
    source_program = parse_program(program_string)
    for noun in range(100):
        for verb in range(100):
            program = deepcopy(source_program)
            program[1] = noun
            program[2] = verb
            try:
                program = execute_program(program)
            except Exception:
                pass
            if program[0] == 19690720:
                print('Noun is {} verb is {}'.format(noun, verb))
                exit()