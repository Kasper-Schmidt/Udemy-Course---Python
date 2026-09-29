sample_list = [21, 55, 18, 33, 24, 22, 68, 35, 79]

chunk_size = 3
chunks = [sample_list[i:i + chunk_size] for i in range(0, len(sample_list), chunk_size)]

for chunk in chunks:
    print(chunk)