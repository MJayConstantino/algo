def selection_sort(string: str):
    string = list(string)
    for i in range(len(string)):
        min_index = i
        for j in range(i + 1, len(string)):
            if string[j] < string[min_index]:
                min_index = j
        string[i], string[min_index] = string[min_index], string[i]
        print("".join(string))
    return "".join(string)

if __name__ == '__main__':
    import sys
    selection_sort(sys.argv[1])
    