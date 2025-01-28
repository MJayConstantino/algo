import time
import math
import sys


class Stopwatch:
    def __init__(self):
        """
        Initializes a new stopwatch.
        """
        self.start = time.time()

    def elapsed_time(self):
        """
        Returns the elapsed CPU time (in seconds) since the stopwatch was created.

        :return: elapsed CPU time (in seconds) since the stopwatch was created
        """
        now = time.time()
        return now - self.start

    @staticmethod
    def main():
        if len(sys.argv) < 2:
            print("Please provide an integer argument.")
            return

        n = int(sys.argv[1])

        # sum of square roots of integers from 1 to n using math.sqrt(x).
        timer1 = Stopwatch()
        sum1 = sum(math.sqrt(i) for i in range(1, n + 1))
        time1 = timer1.elapsed_time()
        print(f"{sum1:e} ({time1:.2f} seconds)")

        # sum of square roots of integers from 1 to n using math.pow(x, 0.5).
        timer2 = Stopwatch()
        sum2 = sum(math.pow(i, 0.5) for i in range(1, n + 1))
        time2 = timer2.elapsed_time()
        print(f"{sum2:e} ({time2:.2f} seconds)")


if __name__ == "__main__":
    Stopwatch.main()
