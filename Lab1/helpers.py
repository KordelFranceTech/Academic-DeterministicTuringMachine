# helper.py
# Kordel France
########################################################################################################################
# This file contains helper methods for common utilities used throughout the app, including cost counters
########################################################################################################################

#characters that are acceptable as operands for the evaluation.
acceptable_chars = ['0','1','+','-','*','_','#']


# counters for asymptotic costs
COUNTER = 0
demo_cost_list = []
add_cost_list = []
sub_cost_list = []
mul_cost_list = []

def should_obey_rule(rule, state, tape):
    new_state = rule.state == state
    new_read = rule.head == tape.head
    return new_state and new_read

def obey_rule(rule, state, tape):
    if should_obey_rule(rule, state, tape):
        state = rule.next_state
        tape.middle = rule.write
        tape.shift_head(rule.move)
    return rule, state, tape

def get_string_from_tape(tape):
    """
    returns a string of what was read on the tape in readable format for output file
    :returns tape_string: human_readable format of 'left' and 'right' concatenated result
    """
    global tape_string
    tape_string = ''
    for i in range(0, len(str(tape))):
        tape_string += str(tape)[i]

    if '+' in tape_string:
        tape_string = tape_string.split('+')[0]
        tape_string = tape_string.replace('+', '')
    if '-' in tape_string:
        tape_string = tape_string.split('-')[0]
        tape_string = tape_string.replace('-', '')

    if '*' in tape_string:
        tape_string = tape_string.split('*')[1]
        tape_string = tape_string.replace('*', '')

    tape_string = tape_string.replace('_', '')
    tape_string = tape_string.replace('[', '')
    tape_string = tape_string.replace(']', '')
    tape_string = tape_string.replace('#', '')
    # print(f'TAPE STRING: {tape_string}')

    return tape_string

def list_to_string(list)->str:
    string = ''
    for index in list:
        string += str(index)
        string += ' '
    return string


# store number of operations of algorithms
brute_force_ops = []
efficient_ops = []
efficient_sort_ops = []

# global counters for number of operations for algorithms
op_count = 0
sort_count = 0

# helper methods for presenting points to user
global coord2coord_list
coord2coord_list = []


def sort_coord2coord_list():
    """
    Sorts a list of coordinates / points by distance betwen points.
    """
    for index in range(len(coord2coord_list) - 1, 0, -1):
        for subindex in range(index):
            if coord2coord_list[subindex].dist > coord2coord_list[subindex + 1].dist:
                temp = coord2coord_list[subindex]
                coord2coord_list[subindex] = coord2coord_list[subindex + 1]
                coord2coord_list[subindex + 1] = temp


def print_coord2coord_list(count):
    """
    Cleanly structures and prints a full list of coordinates / points to the console or writes to file.
    Prints the top n points with shortest distances as specified by count
    :param count: specifies the number of points to return
    """
    return_str = ''
    dist_list = []
    c = 0
    for index in range(0, len(coord2coord_list)):
        coord0 = coord2coord_list[index].coord0
        coord1 = coord2coord_list[index].coord1
        dist = coord2coord_list[index].dist
        if dist not in dist_list and c < count:
            c += 1
            return_str += f'\n{c}\tdistance {dist} from point ({coord0.x}, {coord0.y}) to point ({coord1.x}, {coord1.y})'
        dist_list.append(dist)
    return return_str


def remove_duplicates():
    """
    Removes duplicate coordinate pairs from the global coordinate list.
    For example, if we know the distance from A to B, we don't need the distance from B to A so remove it.
    """
    new_list = []
    global coord2coord_list
    global can_add
    for index in range(0, len(coord2coord_list)):
        can_add = True
        for subindex in range(index, len(coord2coord_list)):
            if coord2coord_list[index].coord0.x == coord2coord_list[subindex].coord1.x:
                if coord2coord_list[index].coord0.y == coord2coord_list[subindex].coord1.y:
                    can_add = False
        if can_add:
            new_list.append(coord2coord_list[index])
            coord0 = coord2coord_list[index].coord0
            coord1 = coord2coord_list[index].coord1
            dist = coord2coord_list[index].dist
            print(f'\n{index + 1}\tdistance {dist} from point ({coord0.x}, {coord0.y}) to point ({coord1.x}, {coord1.y})')
    coord2coord_list = new_list
