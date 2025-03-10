def insertion_sort(string: str):
    list_of_string = list(string)
    n = len(list_of_string)
    
    width = len(str(n - 1))
    
    print(f"{0:<{width}}  {0:<{width}}  {" ".join(list_of_string)}")
    
    for i in range(1, n):
        key = list_of_string[i]
        j = i - 1
        
        # Move elements that are greater than key one position ahead to make space.
        while j >= 0 and list_of_string[j] > key:
            list_of_string[j + 1] = list_of_string[j]
            j -= 1
        
        # Insert the key at its correct position.
        list_of_string[j + 1] = key
        
        print(f"{i:<{width}}  {j + 1:<{width}}  {" ".join(list_of_string)}")
    
    return "".join(list_of_string)


if __name__ == "__main__":
  # Test the function with your example string.
  input_string = "KIMLYJOHNVERGARA"
  sorted_string = insertion_sort(input_string)
  print("\nSorted string:", sorted_string)
