#__main__.py
#Kordel France
########################################################################################################################
#This file sets up file processing and generates the cost & correctness runs.
########################################################################################################################

from Lab1.file_processing import build_correctness_run, build_trace_runs
from Lab1.graph import graph_runtime_data
from Lab1.DTM import DTM
from Lab1.Rule import Rule
from Lab1.Tape import Tape
import Lab1.helpers as helpers

#print a header for UI aesthetics
#this same header is output to the file after the output file is specified by the user
print('*****************************************************************************************')
print('*****************************************************************************************')
print('*****************************************************************************************')
print('\t\t\t\tWelcome')
print('*****************************************************************************************')
print('*****************************************************************************************')

# build correctness and cost runs from Dr. Chlan's input files
build_correctness_run(in_file='reqInput_demo.txt', out_file='traceRun_demo_correctness_reqInput.txt', n=1,type='DEMO')
build_correctness_run(in_file='reqInput_add.txt', out_file='traceRun_add_correctness_reqInput.txt', n=1, type='ADD')
build_correctness_run(in_file='reqInput_sub.txt', out_file='traceRun_sub_correctness_reqInput.txt', n=1, type='SUB')
build_correctness_run(in_file='reqInput_mul.txt', out_file='traceRun_mul_correctness_reqInput.txt', n=1, type='MUL')

# # build correctness runs from custom input files
build_correctness_run(in_file='traceRun_demo_correctness_n5.txt', out_file='traceRun_demo_correctness_n5.txt', n=5,type='DEMO')
build_correctness_run(in_file='traceRun_add_correctness_n5.txt', out_file='traceRun_add_correctness_n5.txt', n=5, type='ADD')
build_correctness_run(in_file='traceRun_sub_correctness_n5.txt', out_file='traceRun_sub_correctness_n5.txt', n=5, type='SUB')
build_correctness_run(in_file='traceRun_mul_correctness_n5.txt', out_file='traceRun_mul_correctness_n5.txt', n=5, type='MUL')

# build cost runs - this builds a file with n randomly generated 2d points
build_trace_runs(count=2)
build_trace_runs(count=5)
build_trace_runs(count=10)
# build_trace_runs(count=20)    # disabled due to slow runtime

# graph the data
graph_runtime_data(helpers.demo_cost_list, helpers.add_cost_list, helpers.sub_cost_list, helpers.mul_cost_list)



