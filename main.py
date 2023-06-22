"""
-------------------------------------------------------------------------------------------------
CSC507 - Portfolio Project, by Adrial Armijo
-------------------------------------------------------------------------------------------------
Main Module
===========

This module serves as the entry point to the application.

Usage:
    python main.py

Description:
    The `main.py` script is responsible for processing big data files using the `process_big_data` module.
    It performs the following steps:
    1. Defines the input file paths and output file paths.
    2. Calls the relevant functions from the `process_big_data` module to process the files.
    3. Prints relevant messages to track the progress of file processing.

    Make sure to update the following variables in the code section marked 'Change Me' according to your requirements:
    - `in_files`: A list of input file paths, specifically the very large files.
    - `out_file1`: Path to the output file for the first processing step.
    - `out_file2`: Path to the output file for the second processing step.

    Please ensure that the input file paths and output file paths are correctly specified before running the script.

"""
import process_big_data

def main():
    # ------- Change Me -----------
    huge_in_files = ["hugefile1.txt", "hugefile2.txt"]
    small_in_files = ["small_file.txt", "smallfile2.txt"] # debug / troubleshoot
    out_file1 = "totalfile1.txt"
    out_file2 = "totalfile2.txt"
    # -----------------------------
    
    print("Begin processing files...")
    file_paths_str = ",".join(huge_in_files) # set delimiter for argument serialization
    process_big_data.run_simultaneously(file_paths_str, out_file1)
    #process_big_data.run_in_parallel(file_paths_str, out_file2)
     

if __name__ == '__main__':
    main()    


