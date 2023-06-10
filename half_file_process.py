def process_half_files(file_path, output_path):
    with open(file_path) as f, open(output_path, 'w') as output:
        lines = f.readlines()
        half = len(lines) // 2
        for line1, line2 in zip(lines[:half], lines[half:]):
            total_sum = int(line1.strip()) + int(line2.strip())
            output.write(str(total_sum) + '\n')