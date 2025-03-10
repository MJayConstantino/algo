def insertion_sort(string: str):
    # ANSI escape codes for colors.
    RED = "\033[31m"
    GRAY = "\033[90m"
    WHITE = "\033[97m"
    RESET = "\033[0m"

    # Convert the string into a list for in-place modifications.
    list_of_string = list(string)
    n = len(list_of_string)
    
    # Calculate the field width for proper alignment.
    width = len(str(n - 1))
    
    colored_letters = [f"{GRAY}{char}{RESET}" for char in list_of_string]
    print(f"{0:<{width}}  {WHITE}{0:<{width}}{RESET}  {' '.join(colored_letters)}")
    
    # Save the initial state for comparison in subsequent iterations.
    prev_state = list_of_string.copy()
    
    # Insertion sort: start from index 1 (since index 0 is trivially sorted).
    for i in range(1, n):
        key = list_of_string[i]
        j = i - 1
        
        # Shift elements that are greater than key to the right.
        while j >= 0 and list_of_string[j] > key:
            list_of_string[j + 1] = list_of_string[j]
            j -= 1
        
        # The correct insertion position is j + 1.
        insertion_index = j + 1
        list_of_string[insertion_index] = key
        
        # Build the colored output for the current state.
        colored_letters = []
        for idx, char in enumerate(list_of_string):
            if idx == insertion_index:
                # The inserted letter is highlighted in red.
                colored_letters.append(f"{RED}{char}{RESET}")
            else:
                # If the letter is in the same position as the previous state, print in gray.
                # Otherwise, if it has shifted, print in white.
                if idx < len(prev_state) and char == prev_state[idx]:
                    colored_letters.append(f"{GRAY}{char}{RESET}")
                else:
                    colored_letters.append(f"{WHITE}{char}{RESET}")
        
        print(f"{i:<{width}}  {WHITE}{insertion_index:<{width}}{RESET}  {' '.join(colored_letters)}")
        
        # Update the previous state for the next iteration.
        prev_state = list_of_string.copy()
    
    return "".join(list_of_string)


if __name__ == "__main__":
    # Test the function with your example string.
    input_string = "KIMLYJOHNVERGARA"
    sorted_string = insertion_sort(input_string)
    print("\nSorted string:", sorted_string)
