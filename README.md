# FranceLab 1 - Kordel K. France

*This project was constructed for the Foundations of Algorithms class, 605.621 section 83, at Johns Hopkins University.*

The project illustrates the definition, construction, and asymptotic costs of different Deterministic Turing Machines (DTMs).
The file `DTM_handler.py` contains the construction of all four required DTMs. There is one DTM for each of the following:
a) a pattern recognition DTM leveraged from the class notes called "DEMO" that detects a pattern of multiple zeros in 
binary strings (see `build_dtm_demo`), b) an addition DTM that adds two binary strings (see `build_dtm_add`), c) a 
subtractive DTM that subtracts one binary string from the other (see `build_dtm_sub`), and d) a multiplicative DTM that
multiplies two binary strings together (see `build_mul_dtm`).

**IMPORTANT: Please note that when n is mentioned, it refers to the length of a binary string, such that 10 represents a 
binary string of n=2, and 1001 represents a binary string of n=4. Obviously larger values of n will result in more 
algorithmic operations by the DTM, so this was the metric scaled to determine the associated runtime complexities for 
each DTM.**

## Running FranceLab1
1. **Ensure Python 3.7 is installed on your computer.**
2. **Navigate to the Lab0 directory.** For example, `cd User\Documents\PythonProjects\FranceLab1`.
Do NOT `cd` into the `Lab1` module.
3. **Run the program as a module: `python -m Lab1`.**
4. **Input and output files ar located in the `io_files` subdirectory.** 
In here, here are `input` and `output` folders containing files of the same type.
In the `input`, the input required from class is inside files with `reqInput` in the name and the names are formatted 
as `traceRun_{DTM_TYPE}_correctness_reqInput.txt` where `DTM_TYPE` is the type of DTM used count. 

**Note: When the module is run, traceRuns will automatically regenerate for different counts of `n`. These files are coded
as `traceRun_{DTM_TYPE}_{RUN_TYPE}_n{n}` where `DTM_TYPE` is the specific DTM used for the run, `RUN_TYPE` specifies either
`cost` or `correctness` run, and `n` specifies the number of digits in each binary operand for that run.
You will see traceRuns for `n = 100` in the `io_files` directory but these are provided for reference and will not
regenerate at runtime due to the time it takes to complete these trace runs.**

### Lab1 Usage

```commandline
usage: python -m Lab1
```

Note that the project takes about 3 minutes to fully execute since time delays are incorporated to easier visualize 
execution of the DTM.

### Project Layout

Here is how the project is structured and organized.

* `FranceLab1`: *The parent folder of the project. This should be the last subdirectory you navigate to to run the
project.*
    * `README.md`:
      *A guide on what the project does, how to run the project, etc.*
    * `io_files`:
      *A subdirectory containing all of the input and output `.txt` files.*
    * `Lab1`: This is the module of the entire program package. It is not a directory. Do not navigate into it.
      * `__init__.py`
        *As the name suggests, this file initializes the program and gives access to the file processing capabilities
        to other programs.*
      * `__main__.py` 
        *This file processes the I/O files, begins the general program, generates trace runs, and facilitates the 
        presentation of the final graph.*
      * `DTM.py`
        *This file establishes a class for a Deterministic Turing Machine and its functionality.*
      * `DTM_handler.py`
        *This file contains handlers to build and run DTM algorithms. It facilitates the construction and operation of
        each DTM.*
      * `Rule.py`
        *This file establishes a class for an object called Rule, which is a logic argument for a DTM.*
      * `Tape.py`
        *This file establishes a class for a set of inputs called Tape that is read by a DTM and gives it directions.*
      * `config.py`
        *This file contains hyperparameters to control debugging features.*
      * `file_processing.py`
        *This file contains I/O methods for processing the input and output .txt files contained in the `io_files` directory.*
      * `helpers.py`
        *This file contains helper methods for common utilities used throughout the app, including cost counters.*
      * `graph.py`
        *This file contains a function to graph and display algorithmic efficiency data.*

###References
The following items were used as references for the construction of this project. 
1) Miller, B. N., & Ranum, D. L. (2014). Problem solving with algorithms and data structures using Python (2nd ed.). 
Decorah, IA: Brad Miller, David Ranum.
2) Cormen, T. H., & Leiserson, C. E. (2009). Introduction to Algorithms, 3rd edition. 
3) Kleinberg, John & Tardos, Eva. (2014). Algorithm Design. Dorling Kindersley.
