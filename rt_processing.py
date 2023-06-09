# The goal of this script is to process large data files of a given input
# There are 5 exercises used in this script: standard_run, and various chunk sizes. 
# Each exercise intends to demonstrate different processing times.
#
# bin_packing.py is imported to mimic processing static heap data.
# For scheduling events in real-time, the python module 'threading' will be used.
# It should be noted that 'threading' does not execute in true parallelism due to
# the Global Interpreter Lock (GIL).
# More about the GIL can be found at https://realpython.com/python-gil/
#

import random
import time
import bin_packing
import os
import threading
import math

def write_num_to_file(file_name, n, chunk_sizes):
    items = [random.randint(0, 32767) for _ in range(n)]
    bin_cap = calculate_bin_capacity(items)

    for i, chunk_size in enumerate(chunk_sizes):
        chunk_items = items[:chunk_size]
        items = items[chunk_size:]
        chunk_file_name = f'{file_name}_chunk_{i + 1}.txt'

        with open(chunk_file_name, 'w') as f:
            f.write(str(bin_cap) + '\n')
            f.write('\n'.join(map(str, chunk_items)))

def calculate_bin_capacity(items):
    total_size = sum(items)
    num_bins = math.ceil(total_size / len(items))  # Round up to ensure all items fit
    bin_cap = total_size / num_bins
    return bin_cap

def call_bin_packing(file_name):
    if not os.path.isfile(file_name):
        print("File does not exist or there is an error with the file provided.")
    bin_packing.process_data(file_name)

def schedule_tasks(file_name, chunk_size):
    threads = []
    for i in range(chunk_size):
        thread_target = bin_packing.process_chunky_data
        t = threading.Thread(target=thread_target, args=(file_name, chunk_size))
        threads.append(t)
        t.start()
    for t in threads:
        t.join() # begin thread scheduling

def combine_files(file_name, chunks, exercise_num):
    output = ""
    base_name = os.path.splitext(file_name)[0]
    for i in range(chunks):
        with open((base_name + f'_chunk_{i}.txt'), 'r') as f:
            chunk_out = f.read()
            output += chunk_out
    with open(f'combined_output_{exercise_num}.txt', 'w') as o:
        o.write(output)

# standard_run runs a static process, calling the next-fit algorithm from the
# imported bin_packing module. 
def standard_run(file_name):
    start = time.time()
    if not os.path.isfile(file_name):
        print("File does not exist or there is an error with the file provided.")   
    call_bin_packing(file_name) # process the file
    finish = time.time()
    time_elapsed = finish - start
    print("Exercise 1 complete. Time elapsed is ", time_elapsed, "second(s)")
    return time_elapsed

# This function splits the file contents into n chunk_size(s) and then proceeds
# to schedule and process the data within the file. Afterwards, the contents are
# combined and written to one output file.
def split_by_chunk_size(file_name, chunks, exercise_num):
    start_time = time.time()
    schedule_tasks(file_name, chunks)
    combine_files(file_name, chunks, exercise_num)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Exercise " + exercise_num + " complete. Time elapsed is", elapsed_time, "second(s)") 
    return elapsed_time
      
    