import rt_processing

def main():
    # ------- Change Me -----------
    n = 5000
    # -----------------------------
    
    file_1 = "nums.txt"
    file_2 = "nums_2.txt"
    file_3 = "nums_3.txt"
    file_4 = "nums_4.txt"
    file_5 = "nums_5.txt"

    print("Beginning exercise 1: standard run...")
    print("Generating", file_1,"with", n,"rows..")
    rt_processing.write_num_to_file(file_1, n)
    time_elapsed_1 = rt_processing.standard_run(file_1)
    
    print("Beginning exercise 2: split into 10 file chunks...")
    print("Generating", file_2,"with", n,"rows..")
    rt_processing.write_num_to_file(file_2, n)
    exercise_num = "2"
    chunks = 10
    time_elapsed_2 = rt_processing.split_by_chunk_size(file_2, chunks, exercise_num)

    print("Beginning exercise 3: split into 10 file chunks...")
    print("Generating", file_3,"with", n,"rows..")
    rt_processing.write_num_to_file(file_3, n)
    exercise_num = "3"
    chunks = 2
    time_elapsed_3 = rt_processing.split_by_chunk_size(file_3, chunks, exercise_num)

    print("Beginning exercise 4: split into 10 file chunks...")
    print("Generating", file_4,"with", n,"rows..")
    rt_processing.write_num_to_file(file_4, n)
    exercise_num = "4"
    chunks = 5
    time_elapsed_4 = rt_processing.split_by_chunk_size(file_4, chunks, exercise_num)

    print("Beginning exercise 5: split into 10 file chunks...")
    print("Generating", file_5,"with", n,"rows..")
    rt_processing.write_num_to_file(file_5, n)
    exercise_num = "5"
    chunks = 20
    time_elapsed_5 = rt_processing.split_by_chunk_size(file_5, chunks, exercise_num)

    fastest_time = min(time_elapsed_1, time_elapsed_2, time_elapsed_3, time_elapsed_4, time_elapsed_5)
    print("Of the 5 exercises, the fastest time was", fastest_time, "second(s)")

if __name__ == '__main__':
    main()    