# graph.py
# Kordel France
########################################################################################################################
# This file contains handlers to build and run DTM algorithms.
########################################################################################################################

from Lab1.DTM import DTM
from Lab1.Rule import Rule
from Lab1.Tape import Tape
import Lab1.helpers as helpers


LEFT = 'left'
RIGHT = 'right'
BLANK = '_'
OP_ADD = '+'
OP_SUB = '-'
OP_MUL = '*'
BYPASS = '#'
OP_DEMO = '&'
STATE_TERMINATE = 100
STATE_ACCEPT = 99


def build_demo_dtm(left, right):
    """
    Builds a deterministic turing machine, runs it, and achieves the results.
    :param left: left side of 'equation' of type int[]
    :param right: right side of 'equation of type int[]
    """
    # define the tape
    t = Tape(left=right, right=left, middle=BLANK)

    # vars indicating DTM final state and state result
    global accept
    accept = 'REJECTED'
    initial_state = 0

    # set of rules for the DTM to work by
    rules = []

    # counter for cost comparison
    helpers.COUNTER = 0

    # define the rules
    # initial state
    r0e = Rule(state=0, head=BLANK, next_state=1, write=BLANK, move=RIGHT)

    # initialized, scanning right number
    r1e = Rule(state=1, head='0', next_state=1, write='0', move=RIGHT)
    r2e = Rule(state=1, head='1', next_state=1, write='1', move=RIGHT)
    r3e = Rule(state=1, head=BLANK, next_state=2, write=BLANK, move=LEFT)

    r4e = Rule(state=2, head='0', next_state=3, write=BLANK, move=LEFT)
    r5e = Rule(state=2, head='1', next_state=2, write='1', move=LEFT)
    r6e = Rule(state=2, head=BLANK, next_state=STATE_TERMINATE, write=BLANK, move=RIGHT)

    r7e = Rule(state=3, head='0', next_state=STATE_ACCEPT, write='0', move=RIGHT)
    r8e = Rule(state=3, head='1', next_state=2, write='1', move=LEFT)
    r9e = Rule(state=3, head=BLANK, next_state=STATE_TERMINATE, write=BLANK, move=RIGHT)

    rules.append(r0e)
    rules.append(r1e)
    rules.append(r2e)
    rules.append(r3e)
    rules.append(r4e)
    rules.append(r5e)
    rules.append(r6e)
    rules.append(r7e)
    rules.append(r8e)
    rules.append(r9e)

    # build the DTM based off the rules above
    dtm_demo = DTM(terminate_states=[STATE_TERMINATE, STATE_ACCEPT], rules=rules, state=initial_state, tape=t)
    orig_tape = dtm_demo.tape
    steps = ''

    # step through each move of the DTM to build a sequence of steps to display to user
    while dtm_demo.state != STATE_TERMINATE and dtm_demo.state != STATE_ACCEPT:
        steps += f'\tstate: {dtm_demo.state}'
        steps += f'\ttape: {dtm_demo.tape}\n'
        dtm_demo.step()

    # run the DTM from the beginning
    dtm_demo.run()

    # get final tape to show user
    final_tape = helpers.get_string_from_tape(dtm_demo.tape)
    if dtm_demo.state == STATE_ACCEPT:
        accept = 'ACCEPTED'

    return final_tape, steps, accept


def build_add_dtm(left, right):
    """
    Builds an addition deterministic turing machine, runs it, and achieves the results.
    :param left: left side of 'equation' of type int[]
    :param right: right side of 'equation of type int[]
    """
    # define the tape
    t = Tape(left=left, right=right, middle=OP_ADD)

    # vars indicating DTM final state and state result
    global accept
    accept = 'REJECTED'
    initial_state = 0

    # set of rules for the DTM to work by
    rules = []

    # counter for cost comparison
    helpers.COUNTER = 0

    # define the rules
    # initial state
    r0a = Rule(state=0, head=OP_ADD, next_state=1, write=OP_ADD, move=RIGHT)

    # initialized, scanning right number
    r1a = Rule(state=1, head='0', next_state=1, write='0', move=RIGHT)
    r2a = Rule(state=1, head='1', next_state=1, write='1', move=RIGHT)
    # reached end of right number. right number scanned, reverse head
    r3a = Rule(state=1, head=BLANK, next_state=2, write=BLANK, move=LEFT)

    # right number scanned
    # decrement mode, can't decrement
    r4a = Rule(state=2, head='0', next_state=2, write='0', move=LEFT)
    # decrement mode, can decrement
    r5a = Rule(state=2, head='1', next_state=3, write='0', move=RIGHT)
    # decrement mode, found nothing more to decrement, now increment right
    r6a = Rule(state=2, head=BLANK, next_state=4, write=BLANK, move=LEFT)
    # right number is all zeros, nothing left to operate so terminate session
    r7a = Rule(state=2, head=OP_ADD, next_state=STATE_ACCEPT, write=OP_ADD, move=LEFT)

    # decrement mode, decremented
    r8a = Rule(state=3, head='0', next_state=3, write='1', move=RIGHT)
    # decrement successful, now carry value to increment left side (add)
    r9a = Rule(state=3, head=BLANK, next_state=4, write=BLANK, move=LEFT)
    # decrement successful, now carry value to increment left side (add)
    r10a = Rule(state=3, head=OP_ADD, next_state=4, write=OP_ADD, move=LEFT)

    # increment mode, carrying value over to left side
    r11a = Rule(state=4, head='0', next_state=4, write='0', move=LEFT)
    r12a = Rule(state=4, head='1', next_state=4, write='1', move=LEFT)
    # carried value over to left side, now figure out which value to increment (add)
    r13a = Rule(state=4, head=OP_ADD, next_state=5, write=OP_ADD, move=LEFT)

    # increment the left side, found value to drop, now move back to right side (add)
    r14a = Rule(state=5, head='0', next_state=7, write='1', move=RIGHT)
    # increment the left side, need to continue carrying value (add)
    r15a = Rule(state=5, head='1', next_state=6, write='0', move=LEFT)

    # found value to drop, now move back to right side
    r16a = Rule(state=6, head='0', next_state=7, write='1', move=RIGHT)
    # continue carrying value
    r17a = Rule(state=6, head='1', next_state=6, write='0', move=LEFT)
    # exceeded digit count - need to add another digit
    r18a = Rule(state=6, head=BLANK, next_state=7, write='1', move=RIGHT)

    # still traversing left side, no change in value
    r19a = Rule(state=7, head='0', next_state=7, write='0', move=RIGHT)
    # still traversing left side, no change in value
    r20a = Rule(state=7, head='1', next_state=7, write='1', move=RIGHT)
    # finished traversing left side, change state back to 1 (add)
    r21a = Rule(state=7, head=OP_ADD, next_state=1, write=OP_ADD, move=RIGHT)

    rules.append(r0a)
    rules.append(r1a)
    rules.append(r2a)
    rules.append(r3a)
    rules.append(r4a)
    rules.append(r5a)

    rules.append(r6a)
    rules.append(r7a)
    rules.append(r8a)
    rules.append(r9a)
    rules.append(r10a)
    rules.append(r11a)

    rules.append(r12a)
    rules.append(r13a)
    rules.append(r14a)
    rules.append(r15a)
    rules.append(r16a)
    rules.append(r17a)

    rules.append(r18a)
    rules.append(r19a)
    rules.append(r20a)
    rules.append(r21a)

    # build the DTM based off the rules above
    dtm_add = DTM(terminate_states=[STATE_TERMINATE, STATE_ACCEPT], rules=rules, state=initial_state, tape=t)
    orig_tape = dtm_add.tape
    steps = ''

    # step through each move of the DTM to build a sequence of steps to display to user
    while dtm_add.state != STATE_TERMINATE and dtm_add.state != STATE_ACCEPT:
        steps += f'\tstate: {dtm_add.state}'
        steps += f'\ttape: {dtm_add.tape}\n'
        dtm_add.step()

    # run the DTM from the beginning
    dtm_add.run()

    # get final tape to show user
    final_tape = helpers.get_string_from_tape(dtm_add.tape)
    if dtm_add.state == STATE_ACCEPT:
        accept = 'ACCEPTED'

    return final_tape, steps, accept


def build_sub_dtm(left, right):
    """
    Builds a subtractive deterministic turing machine, runs it, and achieves the results.
    :param left: left side of 'equation' of type int[]
    :param right: right side of 'equation of type int[]
    """

    # define the tape
    t = Tape(left=left, right=right, middle=OP_SUB)

    # vars indicating DTM final state and state result
    global accept
    accept = 'REJECTED'
    initial_state = 0

    # set of rules for the DTM to work by
    rules = []

    # counter for cost comparison
    helpers.COUNTER = 0

    # define the rules
    # initial state
    r0s = Rule(state=0, head=OP_SUB, next_state=1, write=OP_SUB, move=RIGHT)

    # initialized, scanning right number
    r1s = Rule(state=1, head='0', next_state=1, write='0', move=RIGHT)
    r2s = Rule(state=1, head='1', next_state=1, write='1', move=RIGHT)
    # reached end of right number. right number scanned, reverse head
    r3s = Rule(state=1, head=BLANK, next_state=2, write=BLANK, move=LEFT)

    # right number scanned
    # decrement mode, can't decrement
    r4s = Rule(state=2, head='0', next_state=2, write='0', move=LEFT)
    # decrement mode, can decrement
    r5s = Rule(state=2, head='1', next_state=3, write='0', move=RIGHT)
    # decrement mode, found nothing more to decrement, now increment right
    r6s = Rule(state=2, head=BLANK, next_state=4, write=BLANK, move=LEFT)
    # right number is all zeros, nothing left to operate so terminate session
    r7s = Rule(state=2, head=OP_SUB, next_state=STATE_ACCEPT, write=OP_SUB, move=LEFT)

    # decrement mode, decremented
    r8s = Rule(state=3, head='0', next_state=3, write='1', move=RIGHT)
    # decrement successful, now carry value to increment left side (sub)
    r9s = Rule(state=3, head=OP_SUB, next_state=4, write=OP_SUB, move=LEFT)
    # decrement successful, now carry value to increment left side (add)
    r29s = Rule(state=3, head=BLANK, next_state=4, write=BLANK, move=LEFT)

    # increment mode, carrying value over to left side
    r10s = Rule(state=4, head='0', next_state=4, write='0', move=LEFT)
    r11s = Rule(state=4, head='1', next_state=4, write='1', move=LEFT)
    # carried value over to left side, now figure out which value to increment (sub)
    r12s = Rule(state=4, head=OP_SUB, next_state=5, write=OP_SUB, move=LEFT)

    # decrement the left side, found value to drop, now move back to right side (sub)
    r13s = Rule(state=5, head='1', next_state=7, write='0', move=RIGHT)
    # decrement the left side, need to continue carrying value (sub)
    r14s = Rule(state=5, head='0', next_state=6, write='1', move=LEFT)

    # found value to drop, now move back to right side
    r15s = Rule(state=6, head='0', next_state=7, write='1', move=RIGHT)
    # continue carrying value
    r16s = Rule(state=6, head='1', next_state=6, write='0', move=LEFT)
    # exceeded digit count - need to add another digit
    r17s = Rule(state=6, head=BLANK, next_state=7, write='1', move=RIGHT)

    # found value to drop, now move back to right side (sub)
    r18s = Rule(state=6, head='1', next_state=7, write='0', move=RIGHT)
    # continue carrying value (sub)
    r19s = Rule(state=6, head='0', next_state=6, write='1', move=LEFT)

    # still traversing left side, no change in value
    r20s = Rule(state=7, head='0', next_state=7, write='0', move=RIGHT)
    # still traversing left side, no change in value
    r21s = Rule(state=7, head='1', next_state=7, write='1', move=RIGHT)
    # finished traversing left side, change state back to 1 (sub)
    r22s = Rule(state=7, head=OP_SUB, next_state=1, write=OP_SUB, move=RIGHT)

    rules.append(r0s)
    rules.append(r1s)
    rules.append(r2s)
    rules.append(r3s)
    rules.append(r4s)
    rules.append(r5s)

    rules.append(r6s)
    rules.append(r7s)
    rules.append(r8s)
    rules.append(r9s)
    rules.append(r10s)
    rules.append(r11s)

    rules.append(r12s)
    rules.append(r13s)
    rules.append(r14s)
    rules.append(r15s)
    rules.append(r16s)
    rules.append(r17s)

    rules.append(r18s)
    rules.append(r19s)
    rules.append(r20s)
    rules.append(r21s)
    rules.append(r22s)
    rules.append(r29s)

    # build the DTM based off the rules above
    dtm_sub = DTM(terminate_states=[STATE_TERMINATE, STATE_ACCEPT], rules=rules, state=initial_state, tape=t)
    orig_tape = dtm_sub.tape
    steps = ''

    # step through each move of the DTM to build a sequence of steps to display to user
    while dtm_sub.state != STATE_TERMINATE and dtm_sub.state != STATE_ACCEPT:
        steps += f'\tstate: {dtm_sub.state}'
        steps += f'\ttape: {dtm_sub.tape}\n'
        dtm_sub.step()

    # run the DTM from the beginning
    dtm_sub.run()

    # get final tape to show user
    final_tape = helpers.get_string_from_tape(dtm_sub.tape)
    if dtm_sub.state == STATE_ACCEPT:
        accept = 'ACCEPTED'

    return final_tape, steps, accept


def build_mul_dtm(left, right):
    """
    Builds a multiplicative deterministic turing machine, runs it, and achieves the results.
    :param left: left side of 'equation' of type int[]
    :param right: right side of 'equation of type int[]
    """

    # define the tape
    t = Tape(left=right, right=left, middle=OP_MUL)

    # vars indicating DTM final state and state result
    initial_state = 0
    global accept
    accept = 'REJECTED'

    # set of rules for the DTM to work by
    rules = []

    # counter for cost comparison
    helpers.COUNTER = 0

    # define the rules
    r0m = Rule(state=0, head=OP_MUL, next_state=1, write=OP_MUL, move=LEFT)

    r1m = Rule(state=1, head='0', next_state=3, write=BYPASS, move=RIGHT)
    r2m = Rule(state=1, head='1', next_state=2, write='0', move=RIGHT)
    # reached end of right number. right number scanned, reverse head
    r3m = Rule(state=1, head=BLANK, next_state=STATE_ACCEPT, write=BLANK, move=LEFT)
    r4m = Rule(state=1, head=BYPASS, next_state=1, write='#', move=LEFT)

    # left number scanned
    # decrement mode, can't decrement
    r5m = Rule(state=2, head='0', next_state=2, write='0', move=RIGHT)
    r6m = Rule(state=2, head='1', next_state=2, write='1', move=RIGHT)
    # reached multiplication operator, now start multiplying the values on left
    r7m = Rule(state=2, head=OP_MUL, next_state=2, write=OP_MUL, move=RIGHT)
    r8m = Rule(state=2, head=BLANK, next_state=4, write=BLANK, move=LEFT)
    r9m = Rule(state=2, head=BYPASS, next_state=2, write=BYPASS, move=RIGHT)

    r10m = Rule(state=3, head='1', next_state=5, write='1', move=RIGHT)
    r11m = Rule(state=3, head='0', next_state=3, write='0', move=RIGHT)
    r12m = Rule(state=3, head=BLANK, next_state=4, write='0', move=LEFT)
    r13m = Rule(state=3, head=OP_MUL, next_state=3, write=OP_MUL, move=RIGHT)
    r14m = Rule(state=3, head=BYPASS, next_state=3, write=BYPASS, move=RIGHT)

    r15m = Rule(state=4, head='1', next_state=4, write='1', move=LEFT)
    r16m = Rule(state=4, head='0', next_state=4, write='0', move=LEFT)
    r17m = Rule(state=4, head=OP_MUL, next_state=1, write=OP_MUL, move=LEFT)

    r18m = Rule(state=5, head='0', next_state=5, write='1', move=RIGHT)
    r19m = Rule(state=5, head='1', next_state=5, write='0', move=RIGHT)
    r20m = Rule(state=5, head=BLANK, next_state=4, write='0', move=LEFT)

    rules.append(r0m)
    rules.append(r1m)
    rules.append(r2m)
    rules.append(r3m)
    rules.append(r4m)
    rules.append(r5m)
    rules.append(r6m)
    rules.append(r7m)
    rules.append(r8m)
    rules.append(r9m)
    rules.append(r10m)
    rules.append(r11m)
    rules.append(r12m)
    rules.append(r13m)
    rules.append(r14m)
    rules.append(r15m)
    rules.append(r16m)
    rules.append(r17m)
    rules.append(r18m)
    rules.append(r19m)
    rules.append(r20m)

    # build the DTM based off the rules above
    dtm_mul = DTM(terminate_states=[STATE_TERMINATE, STATE_ACCEPT], rules=rules, state=initial_state, tape=t)
    orig_tape = dtm_mul.tape
    steps = ''

    # step through each move of the DTM to build a sequence of steps to display to user
    while dtm_mul.state != STATE_TERMINATE and dtm_mul.state != STATE_ACCEPT:
        steps += f'\tstate: {dtm_mul.state}'
        steps += f'\ttape: {dtm_mul.tape}\n'
        dtm_mul.step()

    # run the DTM from the beginning
    dtm_mul.run()

    # get final tape to show user
    final_tape = helpers.get_string_from_tape(dtm_mul.tape)
    if dtm_mul.state == STATE_ACCEPT:
        accept = 'ACCEPTED'

    return final_tape, steps, accept