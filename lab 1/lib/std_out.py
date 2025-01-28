import sys
import locale

class StdOut:
    CHARSET = "UTF-8"
    LOCALE = locale.getlocale()

    def __init__(self):
        pass

    @staticmethod
    def println(x=""):
        print(x)

    @staticmethod
    def print(x):
        sys.stdout.write(str(x))
        sys.stdout.flush()

    @staticmethod
    def printf(format_string, *args):
        print(format_string % args, end='')

    @staticmethod
    def main():
        # write to stdout
        StdOut.println("Test")
        StdOut.println(17)
        StdOut.println(True)
        StdOut.printf("%.6f\n", 1.0 / 7.0)

if __name__ == "__main__":
    StdOut.main()
