def selection_sort(string: str):
    string = list(string)
    result = []
    for i in range(len(string)):
        min_index = i
        for j in range(i + 1, len(string)):
            if string[j] < string[min_index]:
                min_index = j
        string[i], string[min_index] = string[min_index], string[i]
        result.append(f"{i:<2} {min_index:<2} {' '.join(string)}")
    return "\n".join(result)

if __name__ == '__main__':
    import sys
    print(selection_sort(sys.argv[1]))