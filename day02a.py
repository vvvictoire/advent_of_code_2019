#!/usr/bin/python3

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
            print(program[0])
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
    program = parse_program(program_string)
    program = execute_program(program)
    #print(program)