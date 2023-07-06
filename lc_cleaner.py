final_arr = []

with open("lc.txt", "r", encoding='utf-8') as file:
    for line1 in file:
        final_arr.append(line1)  # No modification made to remove trailing spaces

final_arr = list(set(final_arr))

def remove_pattern(arr, pattern):
    new_arr = []
    for line2 in arr:
        if pattern not in line2:
            new_arr.append(line2)
        else:
            pass

    return new_arr

final_arr = remove_pattern(final_arr, "/solution")

print(len(final_arr))

with open("lc_problems.txt", "a", encoding='utf-8') as file:
    for line in final_arr:
        file.write(line)
