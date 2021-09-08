# file_processing.py
# Kordel France
########################################################################################################################
# This file contains functions that perform I/O file processing of the input and output files.
########################################################################################################################

from Lab1.config import DEBUG_MODE
import Lab1.DTM_handler as dtm_handler
import Lab1.helpers
import Lab1.Rule
import Lab1.helpers as helpers
import math
import time
import random


def process_file_data(input_text_file):
    """
    Reads in and parses input files into the format of Tape object to be read by a DTM object.
    :param input_text_file: the name of the file to read in and process of type str
    :returns left_file_array: a list object containing the left-hand side of binary equation
    :returns right_file_array: a list object containing the right-hand side of binary equation
    """
    input_file = open(str(input_text_file), 'r')
    global left_file_array, right_file_array, left_array, right_array, left_filled, last_char
    left_file_array = []
    right_file_array = []
    left_array = []
    right_array = []
    left_filled = False
    last_char = ''

    # read the entire file into an array so it can be cleaned
    # clean the data as it is read
    while 1:
        # read in one character at a time as specified by Programming Assignment Guidelines
        single_char = input_file.read(1)

        # a bit of error handling - only accept certain values
        if single_char in Lab1.helpers.acceptable_chars:
            if not left_filled:
                left_array.append(int(single_char))
            else:
                right_array.append(int(single_char))

        # this indicates the separator between left and right sides of equation
        elif single_char == ' ':
            left_filled = True
        elif single_char == '\n':
            left_file_array.append(left_array)
            right_file_array.append(right_array)
            left_array = []
            right_array = []
            left_filled = False
            continue
        # EOF found
        elif not single_char:
            break
        # EOF found
        elif last_char == '\n' and single_char == '\n':
            break
        else:
            continue
        last_char = single_char

    # close the processed file
    input_file.close()
    return left_file_array, right_file_array


def build_correctness_run(in_file, out_file, n, type):
    """
    Builds an output file from the input file that acts as a cost run to compare asymptotic cost of each algorithm.
    :param in_file: the name of the text file to read data in from.
    :param out_file: the name of the text file to write corresponding trace run output to.
    ;param n: an integer that dictates how large the trace run data set is.
    ;param type: a string indicating which type of DTM to build.
    """
    out_file = out_file[:-4] + '.txt'
    output_string = ''

    # begin formatting an output string
    output_string += f'\n\tCORRECTNESS RUN FOR DTM TYPE: {type}'
    output_string += '\n-----------------------------------------------------------------------------------------'
    output_string += '\n-----------------------------------------------------------------------------------------'

    # begin processing the data in the input file and format it for conversion of all DTM builds
    input_file = f'io_files/input/{in_file}'
    output_file = f'io_files/output/{out_file}'
    left_array, right_array = process_file_data(input_file)

    # iterate through each imported equation and build a DTM with corresponding tape for it
    for i in range(0, len(left_array)):
        left_side = left_array[i]
        right_side = right_array[i]
        global orig, result, steps, accept
        orig = ''
        result = ''
        steps = ''
        accept = False

        # decide which DTM type to build
        if type == 'DEMO':
            orig = helpers.list_to_string(left_side)
            orig += ' '
            orig += helpers.list_to_string(right_side)
            result, steps, accept = dtm_handler.build_demo_dtm(left_side, right_side)
        elif type == 'ADD':
            orig = helpers.list_to_string(left_side)
            orig += '+ '
            orig += helpers.list_to_string(right_side)
            result, steps, accept = dtm_handler.build_add_dtm(left_side, right_side)
        elif type == 'SUB':
            orig = helpers.list_to_string(left_side)
            orig += '- '
            orig += helpers.list_to_string(right_side)
            result, steps, accept = dtm_handler.build_sub_dtm(left_side, right_side)
        elif type == 'MUL':
            orig = helpers.list_to_string(left_side)
            orig += ' * '
            orig += helpers.list_to_string(right_side)
            result, steps, accept = dtm_handler.build_mul_dtm(left_side, right_side)

        # format the results into an aesthetic output string
        output_string += f'\n\tAnalyzed cost: {int(helpers.COUNTER)} total operations'
        output_string += f'\n\n{i + 1}\tThe original tape from the {type} DTM: {orig}'
        output_string += f'\n\nThe DTM resulted in a final state of {accept} with result: {result}'
        print(output_string)

        # time delays for easier visualization by user
        time.sleep(2.0)
        steps0 = steps.split('\n')
        for i in range(0, len(steps0)):
            print(steps0[i])
            time.sleep(0.01)

        output_string += f'\n\nThe tape generated from the DTM ([ ] represents head position):\n {steps}'
        output_string += '\n-----------------------------------------------------------------------------------------'
        output_string += '\n-----------------------------------------------------------------------------------------'

    # write the results to the output file
    output_text_file = open(str(output_file), 'a')
    output_text_file.truncate(0)
    output_text_file.write(output_string)
    output_text_file.close()
    Lab1.helpers.COUNTER = 0



def build_cost_run(in_file, out_file, n, type):
    """
    Builds an output file from the input file that acts as a cost run to compare asymptotic cost of each algorithm.
    :param in_file: the name of the text file to read data in from.
    :param out_file: the name of the text file to write corresponding trace run output to.
    ;param n: an integer that dictates how large the trace run data set is.
    ;param type: a string indicating which type of DTM to build.
    """
    out_file = out_file[:-4] + '.txt'

    # begin formatting an output string
    output_string = ''
    output_string += f'\tCOST RUN FOR N = {n}'
    output_string += '\n-----------------------------------------------------------------------------------------'
    output_string += '\n-----------------------------------------------------------------------------------------'
    output_string += '\n-----------------------------------------------------------------------------------------'
    output_string += '\n*****************************************************************************************'
    output_string += '\n*****************************************************************************************'
    output_string += '\n*****************************************************************************************'

    # begin processing the data in the input file and format it for conversion of all DTM builds
    input_file = f'io_files/input/{in_file}'
    output_file = f'io_files/output/{out_file}'
    left_array, right_array = process_file_data(input_file)

    # iterate through each imported equation and build a corresponding DTM for it
    for i in range(0, len(left_array)):
        left_side = left_array[i]
        right_side = right_array[i]
        global orig, result, steps, accept
        orig = ''
        result = ''
        steps = ''
        accept = False

        # decide which DTM to build
        if type == 'demo':
            orig = helpers.list_to_string(left_side)
            orig += ' '
            orig += helpers.list_to_string(right_side)
            result, steps, accept = dtm_handler.build_demo_dtm(left_side, right_side)
            helpers.demo_cost_list.append(helpers.COUNTER)
        elif type == 'add':
            orig = helpers.list_to_string(left_side)
            orig += '+ '
            orig += helpers.list_to_string(right_side)
            result, steps, accept = dtm_handler.build_add_dtm(left_side, right_side)
            helpers.add_cost_list.append(helpers.COUNTER)
        elif type == 'sub':
            orig = helpers.list_to_string(left_side)
            orig += '- '
            orig += helpers.list_to_string(right_side)
            result, steps, accept = dtm_handler.build_sub_dtm(left_side, right_side)
            helpers.sub_cost_list.append(helpers.COUNTER)
        elif type == 'mul':
            orig = helpers.list_to_string(left_side)
            orig += ' * '
            orig += helpers.list_to_string(right_side)
            result, steps, accept = dtm_handler.build_mul_dtm(left_side, right_side)
            helpers.mul_cost_list.append(helpers.COUNTER)

        # format the results into an aesthetic output string
        output_string += f'\n\tAnalyzed cost: {int(helpers.COUNTER)} total operations'
        output_string += f'\n\n{i + 1}\tThe original tape from the {type} DTM: {orig}'
        output_string += f'\n\nThe DTM resulted in a final state of {accept} with result: {result}'
        # output_string += f'\n\nThe tape generated from the DTM ([ ] represents head position):\n {steps}'
        output_string += '\n-----------------------------------------------------------------------------------------'
        output_string += '\n-----------------------------------------------------------------------------------------'
        print(output_string)

    # write the results to the output file
    output_text_file = open(str(output_file), 'a')
    output_text_file.truncate(0)
    output_text_file.write(output_string)
    output_text_file.close()
    Lab1.helpers.COUNTER = 0
    time.sleep(2.0)


def build_trace_runs(count):
    """
    Builds an input file of pseudo-randomly generated data that can be converted to binary equations and used for
    trace runs.
    :param count: an integer that dictates how large each binary number should be in the trace run.
    """
    op_list = ['demo', 'add', 'sub', 'mul']

    # build trace runs for each operation
    for op in op_list:
        trace_run_list = []
        trace_run = ''

        # build 5 trace runs for each file
        for index_j in range(0, 5):
            left_num = ''
            right_num = ''

            # build left and right operands of trace run
            for index_k in range(0, count):
                left_num += f'{random.randint(0, 1)}'
                right_num += f'{random.randint(0, 1)}'
            trace_run += left_num
            trace_run += ' '
            trace_run += right_num
            if index_j < 4:
                trace_run += '\n'
            trace_run_list.append(trace_run)

        # format the output file to write the trace run input data to
        output_file = f'traceRun_{op}_cost_n{count}.txt'
        output_dir = f'io_files/input/traceRun_{op}_cost_n{count}.txt'
        output_text_file = open(str(output_dir), 'a')
        output_text_file.truncate(0)
        for index in range(1, 3):
            output_text_file.write(f'{trace_run_list[index]}')
        output_text_file.close()

        # build the cost run for the trace run input file built above
        build_cost_run(output_file, output_file, count, op)

