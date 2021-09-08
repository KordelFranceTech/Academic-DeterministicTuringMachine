# Rule.py
# Kordel France
########################################################################################################################
# This file establishes a class for an object called Rule, which is a logic argument for a DTM.
########################################################################################################################


class Rule(object):

    """
    Object class that establishes a logic principle that governs a DTM
    :param state: an int that specifies the current execution environment of the DTM
    :param head: a string representing the current value that the "head" of the DTM is reading
    :param next_state: an int that specifies the next execution environment of the DTM
    :param write: a string representing the value to be written to the Tape given current state
    :param move: a string of either 'LEFT' or 'RIGHT' indicating which direction the head should move
    """
    def __init__(self, state, head, next_state, write, move):
        self.state = state
        self.head = head
        self.next_state = next_state
        self.write = write
        self.move = move


    def print_rule(self) -> str:
        """
        prints the current execution environment and rule to the console
        :returns str: a string that describes the current execution environment of the DTM
        """
        r = f'\nrule:\n\tstate: {self.state}' \
            f'\n\thead: {self.head}' \
            f'\n\tnext state: {self.next_state}' \
            f'\n\twrite: {self.write}' \
            f'\n\tmove: {self.move}'
        return r

