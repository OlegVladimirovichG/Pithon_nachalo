original_list = [1, 2, 3, 3, 4, 5, 2, 6, 6]
result_list = []

for item in original_list:
    if item not in result_list:
        result_list.append(item)

print(result_list)
