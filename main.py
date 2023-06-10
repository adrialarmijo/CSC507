# CSC507 - Portfolio Project
# Adrial Armijo
# ------- Prompt ------------------------------------------------------------------------------------------
# Create a program, using a programming language of your choice, to produce a new file: totalfile.txt, 
# by taking the numbers from each line of hugefile1.txt and hugefile2.txt and adding them. 
# So, each line in totalfile.txt is the sum of the corresponding line in hugefile1.txt and hugefile2.txt.
# Create two programs, where one program reads the first half of the files, and another 
# program reads the second half. Use the OS to launch both programs simultaneously.
# Lastly, break up hugefile1.txt and hugefile2.txt into 10 files each, and run your process on all 10 sets
# in parallel. How do the run times compare to the original process?
# ----------------------------------------------------------------------------------------------------------

# import rt_processing
import big_data

def main():
    # ------- Change Me -----------
    in_files = ["hugefile1.txt", "hugefile2.txt"]
    out_files = ["totalfile1.txt", "totalfile2.txt"]
    # -----------------------------

    fastest_time = float('inf')

    for file, output_file in zip(in_files, out_files):
        big_data.run_simultaneously(file, output_file)
        big_data.run_in_parallel(file)


if __name__ == '__main__':
    main()    


