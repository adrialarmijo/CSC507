# This python module mimics processing data within the OS into static and heap memory.
# Using the bin-packing problem, both the best-fit and first-fit algorithms are tested.
# In most cases, the first-fit algorithm performs better, with a worst-case time complexity
# of O(n^2). Best-fit has its uses, but is currently not optimal for this project.

# More on the bin-packing problem can be found in the ACM Journal:
# Goemans, M. X., & Rothvoss, T. (2020). Polynomiality for Bin Packing with a Constant Number of Item Types. 
# Journal of the ACM, 67(6), 1–21. https://doi.org/10.1145/3421750

import os

# Best-Fit Algorithm
def best_fit(items, bin_cap):
    bins = []
    for item in items:
        current_best = None
        best_remain = bin_cap

        for bin in bins:
            remain = bin_cap - sum(bin)
            if remain >= item and remain < best_remain:
                current_best = bin
                best_remain = remain
        
        if current_best is not None:
            current_best.append(item)
        else:
            bins.append([item])
    return bins

# First-Fit Algorithm
def first_fit(items, bin_cap):
    # print("items:", items, "bin_cap:", bin_cap) # debug
    bins = []
    for item in items:
        isPlaced = False
        for bin in bins:
            if sum(bin) + item <= bin_cap:
                bin.append(item)
                isPlaced = True
                break
        if not isPlaced:
            bins.append([item])
    return bins

def get_data_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        if len(lines) > 0:
            bin_cap_str = lines[0].strip()
            if bin_cap_str.isdigit():
                bin_cap = int(bin_cap_str)
            else:
                # print("Invalid bin capacity: not a valid integer") # bug-catcher
                return None, None
            items = [int(line.strip()) for line in lines[1:]]
        else:
            print("File is empty")
            return None, None
    if bin_cap is None or len(items) == 0:
        print("Invalid bin capacity or no items found in the file")
        return None, None
    return items, bin_cap
    

# Write the chunk to a file
def chunkify_me_capn(chunk_size, file_size, base_name, fin):
    # print("chunk size:", chunk_size) # debug
    
    for i in range(chunk_size):
        starting_i = i * chunk_size
        next_end_i = (i + 1) * chunk_size
        end_i = next_end_i if next_end_i < file_size else file_size
        chunk = fin[starting_i:end_i]
        name = base_name + "_chunk_"+ str(i) + ".txt"     
        with open(name, 'w') as o:
            o.write(chunk)   
    
    
def prepare_chunks(filename, chunk_size):
    # print("Preparing", filename, "for chunkification...") # debug
    with open(filename, 'r') as f:
        base_name = os.path.splitext(filename)[0]
        fin = f.read()
        file_size = len(fin)
        # print("File size:", file_size) # debug
        # print("Chunk size:", chunk_size) # debug
        chunkify_me_capn(chunk_size, file_size, base_name, fin)
    

def process_data(filename):
    items, bin_cap = get_data_from_file(filename)
    first_fit(items, bin_cap)

def process_chunky_data(filename, chunk_size):
    prepare_chunks(filename, chunk_size)
    base_name = os.path.splitext(filename)[0]
    all_items = []
    all_bin_cap = None
    for i in range(chunk_size):
        chunk_file_name = base_name + "_chunk_"+ str(i) + ".txt"
        items, bin_cap = get_data_from_file(chunk_file_name)
        print("Chunk file:", chunk_file_name) # debug
        print("Items:", items) # debug
        print("Bin Capacity:", bin_cap) # debug
        if items is not None and bin_cap is not None:
            all_items.extend(items)
            all_bin_cap = bin_cap
    if all_bin_cap is not None:
        first_fit(all_items, all_bin_cap)

def print_first(calc_first_fit): # debug
    print("Printing First-Fit results:")
    for i, bin in enumerate(calc_first_fit, start=1):
        print(f"Bin {i}: {bin}")


def print_best(calc_best_fit): # debug
    print("Printing First-Fit results:")
    for i, bin in enumerate(calc_best_fit, start=1):
        print(f"Bin {i}: {bin}")