"""
Process Big Data Module
=======================

This script is called by main.py to manipulate hugefile1.txt and hugefile2.txt,
each containing 1 billion lines of randomized numbers. The script processes the files by
adding the corresponding rows of each file together and placing the result into a new file.

The script provides functions for running the processing tasks in different ways,
including simultaneous runs and parallel runs on chunked files.

Usage:
    Call the desired functions from main.py to perform the processing tasks.

Dependencies:
    This script depends on the chunkify module and the sum_calculator module.

Modules:
    - subprocess: Used to run separate scripts as subprocesses.
    - time: Used to measure elapsed time.
    - chunkify: Contains functions for splitting files into chunks.
    - sum_calculator: Contains the calculate function for summing numbers.

Functions:
    - t(): Returns the current time in seconds.
    - get_elapsed_time(start, end): Calculates the elapsed time between two time points.
    - print_elapsed_time_for(process_name, start_time, end_time): Prints the elapsed time for a process.
    - run_script(script_name, file_paths_str, output_file): Runs a script as a subprocess.
    - run_simultaneously(file_paths_str, output_path): Runs scripts in simultaneous mode.
    - run_in_parallel(file_paths_str, output_path): Runs scripts in parallel mode on chunked files.

Note:
    Modify the file paths and output paths in the main.py script to match the desired files.
    Serialization and the use of a delimiter is used throughout to assist in allowing a function
    to accept multiple files such as: 'file_paths = "hugefile1.txt", "hugefile2.txt"'. The files
    can be passed as a single argument then separated by the delimiter to be used individually.

"""
import subprocess
import time
import chunkify as chunk

def t():
    return time.time()

def get_elapsed_time(start, end):
    return end - start

def print_elapsed_time_for(process_name, start_time, end_time):
    e = get_elapsed_time(start_time, end_time)
    print(f"{process_name} completed in {e} seconds.")

def run_script(script_name, file_paths_str, output_file):
    print("Calling script", script_name)
    kwargs_str = { # contains command-line arguments
        "command": "/usr/bin/python3",
        "--arg1" : file_paths_str,
    }
    # send output from subprocess to output_file
    subprocess.run([kwargs_str["command"], script_name, kwargs_str["--arg1"]],
        stdout=output_file
    )
    
def run_simultaneously(file_paths_str, output_path):
    """
    Run two programs simultaneously, where one program reads the first half of the files,
    and another program reads the second half. The subprocess module is used to launch
    each program as a separate process.

    Args:
        file_paths_str (str): Serialized string of file paths, separated by a delimiter.
        output_path (str): Path to the output file for storing the results.

    Returns:
        None

    Raises:
        None

    Note:
        - The file paths are passed as a serialized string to assist in argument serialization.
        - The subprocess module is used to run each program as a separate process.
        - The output from each program is redirected to the specified output file.

    Example:
        run_simultaneously("hugefile1.txt,hugefile2.txt", "totalfile1.txt")

    """
    process_name = "Simultaneous Runs"
    script1 = "read_first_half.py"
    script2 = "read_second_half.py"
    start_time = t()
    print("Starting simultaneous runs...")
    with open(output_path, "a") as out_file:
        run_script(script1, file_paths_str, out_file)
        run_script(script2, file_paths_str, out_file)
    end_time = t()
    print_elapsed_time_for(process_name, start_time, end_time)

def run_in_parallel(file_paths_str, output_path):
    """
    Break up the input files into chunks and run the processing on all sets in parallel.

    Args:
        file_paths_str (string): Serialized string of file paths, separated by a delimiter.
        output_path (str): Path to the output file for storing the results.

    Returns:
        None

    Raises:
        None

    Note:
        - The input files are split into chunks.
        - Each chunk is processed in parallel using multiple processes.
        - The results are written to the specified output file.

    Example:
        run_in_parallel(["hugefile1.txt", "hugefile2.txt"], "totalfile2.txt")

    """
    process_name = "Parallel Runs"
    chunk_size = 10
    chunk_directory = "chunked_files"
    start_time = t()
    chunk.split_file(file_paths_str, chunk_directory, chunk_size)
    chunk.process_chunks(chunk_directory, output_path)
    end_time = t()
    print_elapsed_time_for(process_name, start_time, end_time)