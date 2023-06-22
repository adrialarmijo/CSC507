"""
Chunkify Module
===============

This module provides functions to split large files into smaller chunks for parallel processing.

Functions:
----------
- write(chunks, chunk_directory): Write the chunks to individual chunk files in the specified chunk directory.
- get_chunks(lines, chunk_size): Split the lines into chunks of the specified size.
- split_file(file_paths, chunk_directory, chunk_size): Split the input files into chunks and write them to the chunk directory.
- pair_chunks(chunk_files): Pair the chunk files for further processing.
- process_result(lines, output_file): Process the lines using parallel execution and write the result to the output file.
- process_chunk_file(chunk_file, output_file): Process a single chunk file.
- process_chunk_pairs(chunk_pairs, chunk_directory): Process the chunk pairs and write the results to the output file.
- process_chunks(chunk_directory, output_file): Process the chunks in the specified directory and write the results to the output file.

Usage:
------
The functions in this module can be imported and used in other Python scripts to assist in creating
chunks of data from a specified file.

"""

import sys
import os
import logging
import traceback
import sum_calculator

def write(chunks, chunk_directory):
    for i, chunk in enumerate(chunks):
            chunk_file_path = os.path.join(chunk_directory, f"chunk_{i}.txt")
            with open(chunk_file_path, 'w') as chunk_file:
                chunk_file.writelines(chunk)

def get_chunks(lines, chunk_size):
    return [lines[i:i+chunk_size] for i in range(0, len(lines), chunk_size)]

def split_file(file_paths_str, chunk_directory, chunk_size):
    file_paths = file_paths_str.split(',') # use a delimiter to assist in serialization
    total_files = len(file_paths)
    current_file = 0
    try:
        for path in file_paths:
            current_file += 1
            print(f"Splitting file {current_file}/{total_files}: {path} into chunks...")
            with open(path, 'r') as original_file:
                lines = original_file.readlines()
                os.makedirs(chunk_directory, exist_ok=True) # create the directory for chunked files
                chunks = get_chunks(lines, chunk_size)
                write(chunks, chunk_directory)
                print(f"Chunks created for file {current_file}/{total_files}: {path}")
    except FileNotFoundError:
        print(f"File not found: {path}")
    except IOError:
        print(f"Error reading file: {path}")

def pair_chunks(chunk_files):
    try:
        sorted_chunk_files = sorted(chunk_files) # files must be sorted to keep their pairing
        even_i = range(0, len(sorted_chunk_files), 2) # contains the even indecies of chunked_pairs
        odd_i = range(1, len(sorted_chunk_files), 2) # contains the odds
        chunk_pairs = [
            (sorted_chunk_files[i], sorted_chunk_files[j]) for i, j in zip(even_i, odd_i)
        ]
    except IndexError:
        print("Error: Odd number of chunk files. Pairs cannot be created.")
    return chunk_pairs

def process_result(lines, output_file):
    logging.basicConfig(filename='error.log', level=logging.ERROR)
    try:
        with open(output_file, 'a') as output:
            for line in lines:
                try:
                    result = sum_calculator.calculate(line)
                    output.write(str(result) + '\n')
                except ValueError as e:
                    logging.error(f"Invalid literal for int() with base 10: {line.strip()}")
                    logging.error(traceback.format_exc())
                    sys.exit(1)
    except Exception as e:
        logging.error(f"Error processing file: {output_file}")
        logging.error(traceback.format_exc())
        sys.exit(1)

def process_chunk_file(chunk_file, output_file):
    try:
        with open(chunk_file) as f:
            lines = f.readlines()
        process_result(lines, output_file)
    except FileNotFoundError:
        print(f"Chunk file not found: {chunk_file}")
    except IOError:
        print(f"Error reading chunk file: {chunk_file}")

def process_chunk_pairs(chunk_pairs, chunk_directory, output_file):
    for pair in chunk_pairs:
        for file in pair:
            process_chunk_file(os.path.join(chunk_directory, file), output_file)

def delete_chunk_files(chunk_directory):
    try:
        chunk_files = os.listdir(chunk_directory)
        for file in chunk_files:
            file_path = os.path.join(chunk_directory, file)
            try:
                os.remove(file_path)
            except FileNotFoundError:
                print(f"Error deleting chunk file: {file_path}. File not found.")
            except IOError as e:
                print(f"Error deleting chunk file: {file_path}. {str(e)}")
    except FileNotFoundError:
        print(f"Error accessing chunk directory: {chunk_directory}. Directory not found.")
    except IOError as e:
        print(f"Error accessing chunk directory: {chunk_directory}. {str(e)}")

def process_chunks(chunk_directory, output_file):
    chunk_files = os.listdir(chunk_directory)
    chunk_pairs = pair_chunks(chunk_files)
    if chunk_pairs is not None:
        process_chunk_pairs(chunk_pairs, chunk_directory, output_file)
        delete_chunk_files(chunk_directory)
    else:
        print("Error processing chunks. Aborting")