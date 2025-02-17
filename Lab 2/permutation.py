# client code for permutation
import random
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python permutation.py <number of strings to be called>")
        return
    
    k = int(sys.argv[1])
    
    try:
        with open("IVOS.txt", "r") as string_file:
            lines = [line.strip() for line in string_file.readlines()]
            
            if k > len(lines):
                print("Error: k is greater than the number of available strings.")
                return
            
            selected_strings = random.sample(lines, k)
            
            for string in selected_strings:
                print(string)
    except FileNotFoundError:
        print("Error: strings.txt file not found.")
    except ValueError:
        print("Error: Invalid value in strings.txt.")

if __name__ == "__main__":
    main()