import rt_processing

def main():
    # ------- Change Me -----------
    n = 10000000
    files = ["nums.txt", "nums_2.txt", "nums_3.txt", "nums_4.txt", "nums_5.txt"]
    chunk_sizes = [1, 10, 2, 5, 20]
    # -----------------------------

    fastest_time = float('inf')
    fastest_exercise = None

    for i in range(len(files)):
        print(f"Beginning exercise {i+1}: split into {chunk_sizes[i]} file chunks...")
        print(f"Generating {files[i]} with {n} rows..")
        exercise_num = str(i+1)

        if i == 0:
            rt_processing.write_num_to_file(files[i], n, chunk_sizes[i])
            time_elapsed = rt_processing.standard_run(files[i])
        else:
            rt_processing.write_num_to_file(files[i], n, chunk_sizes[i])
            time_elapsed = rt_processing.split_by_chunk_size(files[i], chunk_sizes[i], exercise_num)

        if time_elapsed < fastest_time:
            fastest_time = time_elapsed
            fastest_exercise = i + 1

    print("Of the 5 exercises, the fastest time was exercise", fastest_exercise, "at", fastest_time, "second(s)")

if __name__ == '__main__':
    main()    