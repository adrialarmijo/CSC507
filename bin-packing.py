import time

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
        bin_cap = int(lines[0].strip())
        items = [int(line.strip()) for line in lines[1:]]
    return bin_cap, items 

def print_first(calc_first_fit): # debug
    print("Printing First-Fit results:")
    for i, bin in enumerate(calc_first_fit, start=1):
        print(f"Bin {i}: {bin}")


def print_best(calc_best_fit): # debug
    print("Printing First-Fit results:")
    for i, bin in enumerate(calc_best_fit, start=1):
        print(f"Bin {i}: {bin}")


def main():
    filename = 'text2.txt'
    bin_cap, items = get_data_from_file(filename)
    
    time_elapsed_first_fit = 0
    time_elapsed_best_fit = 0

    start_time = time.time()
    #print("Starting timer at:", start_time) # debug
    
    calc_first_fit = first_fit(items, bin_cap)
    #print("time is", time.time(),"-", start_time) # debug
    time_elapsed_first_fit = (time.time() - start_time)
    
    current_time = time.time()
    calc_best_fit = best_fit(items, bin_cap)
    #print("time is", time.time(),"-", current_time) # debug
    time_elapsed_best_fit = (time.time() - current_time)
    
    print("First-Fit runtime:", time_elapsed_first_fit, "seconds")
    print("Best-Fit runtime:", time_elapsed_best_fit, "seconds")
    

if __name__ == '__main__':
    main()        