def selection_trace(string: str):

    string = list(string)
    length = len(string)
    result = []

    for i in range(length):
        min_index = i
        
        for j in range(i + 1, length):
            if string[j] < string[min_index]:
                min_index = j
        
        # Create formatted string BEFORE the swap
        formatted_chars = []
        for idx, char in enumerate(string):
            if idx == min_index:
                # Red text for the element to be swapped
                formatted_chars.append(f"\033[91m{char}\033[0m")
            elif idx < i:
                # Gray text for already sorted elements
                formatted_chars.append(f"\033[90m{char}\033[0m")
            else:
                # Normal text for unsorted elements
                formatted_chars.append(char)
        
        # Add this iteration to results (before swap)
        result.append(f"{i:<2} {min_index:<2} {' '.join(formatted_chars)}")
        
        # Swap the found minimum element with the element at position i
        string[i], string[min_index] = string[min_index], string[i]
    
    # Add final sorted string in bold - using the bold ANSI code for the entire string
    bold_chars = [f"\033[1m{char}\033[0m" for char in string]
    result.append(' ' * 2 + '**' + ' '.join(bold_chars) + '**')
    
    return '\n'.join(result)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        print(selection_trace(sys.argv[1]))
    else:
        print("Usage: python selection_trace.py <string>")