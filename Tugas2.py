data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

filtered_data = []
for entry in data:
    numbers = list(filter(str.isdigit, entry.split()))
    filtered_data.append(numbers)

for numbers in filtered_data:
    print(numbers)
