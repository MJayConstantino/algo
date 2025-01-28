import sys
import re
import locale


class StdIn:
    CHARSET_NAME = "UTF-8"
    LOCALE = locale.localeconv()

    def __init__(self):
        pass

    @staticmethod
    def is_empty():
        return sys.stdin.isatty()

    @staticmethod
    def has_next_line():
        line = sys.stdin.readline()
        if line:
            sys.stdin = open(0)
            sys.stdin.write(line)
            sys.stdin.seek(0)
            return True
        return False

    @staticmethod
    def has_next_char():
        char = sys.stdin.read(1)
        if char:
            sys.stdin = open(0)
            sys.stdin.write(char)
            sys.stdin.seek(0)
            return True
        return False

    @staticmethod
    def read_line():
        try:
            line = sys.stdin.readline().strip()
            return line
        except EOFError:
            return None

    @staticmethod
    def read_char():
        try:
            char = sys.stdin.read(1)
            if len(char) != 1:
                raise AssertionError(
                    "Internal (Std)In.readChar() error! Please contact the authors.")
            return char
        except EOFError:
            raise EOFError(
                "attempts to read a 'char' value from standard input, but no more tokens are available")

    @staticmethod
    def read_all():
        if StdIn.is_empty():
            return ""
        return sys.stdin.read()

    @staticmethod
    def read_string():
        try:
            string = sys.stdin.read().strip()
            return string
        except EOFError:
            raise EOFError(
                "attempts to read a 'String' value from standard input, but no more tokens are available")

    @staticmethod
    def read_int():
        try:
            return int(sys.stdin.read().strip())
        except ValueError as e:
            raise ValueError(
                f"attempts to read an 'int' value from standard input, but the next token is invalid")
        except EOFError:
            raise EOFError(
                "attempts to read an 'int' value from standard input, but no more tokens are available")

    @staticmethod
    def read_double():
        try:
            return float(sys.stdin.read().strip())
        except ValueError as e:
            raise ValueError(
                f"attempts to read a 'double' value from standard input, but the next token is invalid")
        except EOFError:
            raise EOFError(
                "attempts to read a 'double' value from standard input, but no more tokens are available")

    @staticmethod
    def read_float():
        try:
            return float(sys.stdin.read().strip())
        except ValueError as e:
            raise ValueError(
                f"attempts to read a 'float' value from standard input, but the next token is invalid")
        except EOFError:
            raise EOFError(
                "attempts to read a 'float' value from standard input, but no more tokens are available")

    @staticmethod
    def read_long():
        try:
            return int(sys.stdin.read().strip())
        except ValueError as e:
            raise ValueError(
                f"attempts to read a 'long' value from standard input, but the next token is invalid")
        except EOFError:
            raise EOFError(
                "attempts to read a 'long' value from standard input, but no more tokens are available")

    @staticmethod
    def read_short():
        try:
            return int(sys.stdin.read().strip())
        except ValueError as e:
            raise ValueError(
                f"attempts to read a 'short' value from standard input, but the next token is invalid")
        except EOFError:
            raise EOFError(
                "attempts to read a 'short' value from standard input, but no more tokens are available")

    @staticmethod
    def read_byte():
        try:
            return int(sys.stdin.read().strip())
        except ValueError as e:
            raise ValueError(
                f"attempts to read a 'byte' value from standard input, but the next token is invalid")
        except EOFError:
            raise EOFError(
                "attempts to read a 'byte' value from standard input, but no more tokens are available")

    @staticmethod
    def read_boolean():
        try:
            token = StdIn.read_string().lower()
            if token in ["true", "1"]:
                return True
            elif token in ["false", "0"]:
                return False
            else:
                raise ValueError(
                    f"attempts to read a 'boolean' value from standard input, but the next token is \"{token}\"")
        except EOFError:
            raise EOFError(
                "attempts to read a 'boolean' value from standard input, but no more tokens are available")

    @staticmethod
    def read_all_strings():
        return re.split(r'\s+', StdIn.read_all().strip())

    @staticmethod
    def read_all_lines():
        return StdIn.read_all().splitlines()

    @staticmethod
    def read_all_ints():
        return [int(x) for x in StdIn.read_all_strings()]

    @staticmethod
    def read_all_longs():
        return [int(x) for x in StdIn.read_all_strings()]

    @staticmethod
    def read_all_doubles():
        return [float(x) for x in StdIn.read_all_strings()]

    @staticmethod
    def main():
        print("Type a string: ", end='')
        s = StdIn.read_string()
        print(f"Your string was: {s}\n")

        print("Type an int: ", end='')
        a = StdIn.read_int()
        print(f"Your int was: {a}\n")

        print("Type a boolean: ", end='')
        b = StdIn.read_boolean()
        print(f"Your boolean was: {b}\n")

        print("Type a double: ", end='')
        c = StdIn.read_double()
        print(f"Your double was: {c}\n")


if __name__ == "__main__":
    StdIn.main()
