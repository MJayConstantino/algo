# client code for permutation
import random
import sys

def main():
    # Check command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python permutation.py <filename> <number_of_strings>")
        return

    filename = sys.argv[1]

    try:
        k = int(sys.argv[2])
        if k <= 0:
            print("Error: Number of strings (k) must be a positive integer.")
            return
    except ValueError:
        print("Error: <number_of_strings> must be an integer.")
        return

    try:
        with open(filename, "r") as file:
            lines = [line.strip() for line in file if line.strip()]  # Remove empty lines

            if not lines:
                print("Error: The file is empty.")
                return

            if k > len(lines):
                print(f"Error: k ({k}) is greater than the number of available strings ({len(lines)}).")
                return

            selected_strings = random.sample(lines, k)  # Select k unique strings

            print("\nSelected strings:")
            for string in selected_strings:
                print(string)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
