# DTM.py
# Kordel France
########################################################################################################################
# This file establishes a class for a Deterministic Turing Machine.
########################################################################################################################

from Lab1 import helpers
from Lab1 import config

class DTM(object):

    """
    Object class that represents a Deterministic Turing Machine
    :param terminate_states: states at which the DTM is determined to have finished execution
    :param rules: set of logic arguments of type Rule[] that govern behavior of DTM
    :param tape: object of type Tape that gives the DTM input to execute instructions upon
    """
    def __init__(self, terminate_states, rules, state, tape):
        self.terminate_states = terminate_states
        self.rules = rules
        self.state = state
        self.tape = tape

    @property
    def terminating(self):
        """
        tells the DTM when to terminate execution, or "halt" execution
        :returns state: the state of type int that indicates the DTM has finished execution
        """
        return self.state in self.terminate_states


    @property
    def idle(self):
        """
        tells the DTM to "idle" and not get next rule for execution, not in terminal state
        :returns get_next_rule: boolean value indicating DTM to remain idle until otherwise specified
        """
        return not self.get_next_rule


    @property
    def processing_state(self):
        """
        indicates what state the DTM is currently in
        :returns state: object of type int indicating the current state of processing of the DTM
        """
        return not (self.terminating or self.idle)


    @property
    def get_next_rule(self):
        """
        tells the DTM to fetch the next rule, or instruction, in the set of rules
        :returns did_find_rules: object of type Rule[] that specifies list of logic to follow for execution
        """
        did_find_rules = self.search_for_rules()
        if did_find_rules:
            return did_find_rules[0]
        return did_find_rules


    def search_for_rules(self):
        """
        finds and, if found, establishes the set of rules that will be used for this execution
        :returns state: the state of type int that indicates the DTM has finished execution
        """
        # found_rules = [rule for rule in self.rules if helpers.should_obey_rule(rule, self.state, self.tape)]
        found_rules = []
        for rule in self.rules:
            if helpers.should_obey_rule(rule, self.state, self.tape):
                found_rules.append(rule)
        return found_rules


    def step(self):
        """
        transition function that steps to the next state of execution for the DTm
        """
        _, self.state, self.tape = helpers.obey_rule(self.get_next_rule, self.state, self.tape)
        helpers.COUNTER += 1
        if config.DEBUG_MODE:
            print(f'\tstate: {self.state}\ttape: {self.tape}')


    def run(self):
        """
        routine that runs the entire DTM algorithm, establishes rules, and runs the Tape
        """
        while self.processing_state:
            self.step()




