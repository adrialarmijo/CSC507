# This script is called by main.py to manipulate hugefile1.txt and hugefile2.txt
# which each contain 1 billion lines of randomized numbers. This program will process the files by
# adding the corresponding rows of each file together and placing the result into a new file.

import subprocess
import time

def split_file_into_chunks(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        chunk_size = len(lines) // 10
        for i in range(10):
            start = i * chunk_size
            end = start + chunk_size
            chunk_lines = lines[start:end]
            with open(f"chunk_{i}.txt", 'w') as chunk_file:
                chunk_file.writelines(chunk_lines)

# Create two programs, where one program reads the first half of the files, and another 
# program reads the second half. Use the OS to launch both programs simultaneously.
# The subprocess module is called to run each program as a separate process.
def run_simultaneously(file_path, output_path):
    start_time = time.time()
    subprocess.run(["python", "half_file_process.py", file_path, output_path])
    end_time = time.time()
    print("Elapsed time:", end_time - start_time)

# Break up hugefile1.txt and hugefile2.txt into 10 files each, and run your process on all 10 sets
# in parallel. 
def run_in_parallel(file_path):
    start_time = time.time()
    split_file_into_chunks(file_path)
    subprocess.run(["python", "parallel_file_process.py"])
    end_time = time.time()
    print("Elapsed time:", end_time - start_time)