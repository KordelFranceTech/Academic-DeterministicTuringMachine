# Tape.py
# Kordel France
########################################################################################################################
# This file establishes a class for a set of inputs called Tape that is read by a DTM.
########################################################################################################################


# options for movement of the mechanical head
LEFT = 'left'
RIGHT = 'right'

# available read/write options of the DTM on the tape
BLANK = '_'
OP_MUL = '*'
OP_ADD = '+'
OP_SUB = '-'
OP_TERM = '#'

class Tape(object):
    """
    Object class that represents a string of inputs and outputs to be executed upon by a DTM
    :param left: str[] as the left binary number
    :param right: str[] as the right binary number
    :param middle: str as the operand or BLANK value
    :param blank: str that specifies which value is considered as a BLANK
    """
    def __init__(self, left=None, middle=None, right=None, blank=BLANK):
        self.left = left or []
        self.right = right or []
        self.middle = middle
        if self.middle is None:
            self.middle = blank
        self.blank = blank


    def shift_head_right(self):
        """
        moves the DTM head right
        """
        self.left = self.left + [self.middle]
        if self.right:
            self.middle = self.right.pop(0)
        else:
            self.middle = self.blank

    def shift_head_left(self):
        """
        moves the DTM head left
        """
        self.right = [self.middle] + self.right
        if self.left:
            self.middle = self.left.pop()
        else:
            self.middle = self.blank

    @property
    def head(self):
        """
        defines the value that is currently being read by the DTM head
        :returns middle: str that indicates the current value being read by the DTM
        """
        return str(self.middle)

    def shift_head(self, direction):
        """
        indicates to the head of the DTM that it should move either left or right
        :param direction: str indicating either "LEFT" or "RIGHT
        :returns middle: str indicating the new value being read by the DTM head
        """
        # if not direction in [LEFT, RIGHT, OP_ADD, OP_SUB, OP_MUL, OP_TERM]:
        if not direction in [LEFT, RIGHT]:
            raise RuntimeError('unrecognized direction "%s"'% direction)
        if direction == LEFT:
            return self.shift_head_left()
        if direction == RIGHT:
            return self.shift_head_right()

    def __repr__(self):
        out = '{}[{}]{}'.format(''.join(map(str, self.left)), self.middle, ''.join(map(str, self.right)))
        return out




