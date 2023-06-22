"""
Read Second Half Module
======================

    Read the second half of each file specified in the file_paths and calculate the sum.

    Args:
        file_paths (list): A list of file paths.

    Returns:
        int: The sum of the values in the second half of the files.

    Raises:
        FileNotFoundError: If any of the specified files cannot be found.

    Note: 
        This script can be combined with its counterpart (read_second_half.py) to avoid
        code redundancy, however the assignment states that we are to have two separate programs
        run the first half and second half at the same time, so they are created as two individual scripts.
"""
import sys
import sum_calculator 

if __name__ == "__main__":
    file_path_str = sys.argv[1]
    file_paths = file_path_str.split(",") # use a delimiter to assist in serialization
    second_half_sum = 0

    for file in file_paths:
        with open(file) as f:
            lines = f.readlines()
        half = len(lines) // 2
        second_half_sum = sum_calculator.calculate(lines[half:]) # second half
        print(second_half_sum) # prints to stdout
        sys.stdout.flush() # immediately sends output for writing
