import glob
import concurrent.futures

def process_chunk(file_path):
    output_path = f"total_{file_path}.txt"

    with open(file_path) as f, open(output_path, 'w') as output:
        lines = f.readlines()

        for line in lines:
            total_sum = sum(map(int, line.split()))
            output.write(str(total_sum) + '\n')

def run_parallel_processes(file_paths):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_chunk, file_paths)

file_paths = glob.glob("chunk_*.txt")
run_parallel_processes(file_paths)