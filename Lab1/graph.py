# graph.py
# Kordel France
########################################################################################################################
# This file contains a function to graph and display algorithmic efficiency data
########################################################################################################################

import matplotlib.pyplot as plt
from Lab1.config import DEBUG_MODE
import numpy as np


def graph_runtime_data(demo_cost_list, add_cost_list, sub_cost_list, mul_cost_list):
    """
    Graphs the cost values of the brute-force and efficient algorithms to visually compare algorithm efficiency.
    :param demo_cost_list: list of cost values accumulated from demo DTM.
    :param add_cost_list: list of cost values accumulated from add DTM.
    :param sub_cost_list: list of cost values accumulated from subtract DTM.
    :param mul_cost_list: list of cost values accumulated from multiply DTM.
    """

    # set up the graph and plot the data
    counts = [2, 5, 10]
    n = []

    for count in counts:
        for i in range(0, 5):
            n.append(count)

    print(f'cost counts for all demo cost runs: {demo_cost_list}')
    print(f'cost counts for all add cost runs: {add_cost_list}')
    print(f'cost counts for all sub cost runs: {sub_cost_list}')
    print(f'cost counts for all mul cost runs: {mul_cost_list}')

    plt.scatter(n, demo_cost_list, label='cost of example DTM')
    plt.scatter(n, add_cost_list, label='cost of addition DTM')
    plt.scatter(n, sub_cost_list, label='cost of subtraction DTM')
    plt.scatter(n, mul_cost_list, label='cost of multiplication DTM')
    plt.title('Algorithm Cost Analysis')
    plt.xlabel('n')
    plt.ylabel('Number of Operation (Cost)')
    plt.legend()
    plt.show()

