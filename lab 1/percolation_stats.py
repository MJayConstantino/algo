import random
from lib.std_stats import StdStats
from percolation import Percolation

class PercolationStats:
    # perform independent trials on an n-by-n grid
    def __init__(self, n: int, trials: int):
        if n <= 0 or trials <= 0:
            raise ValueError("Both n and trials must be greater than 0")

        self.n = n
        self.trials = trials
        self.T = []

        for i in range(trials):
            perc = Percolation(n)
            open_sites = 0

            # Monte Carlo simulation
            while not perc.percolates():
                row = random.randint(1, n)
                col = random.randint(1, n)

                if not perc.is_open(row, col):
                    perc.open(row, col)
                    open_sites += 1

            self.T.append(open_sites / (n * n))

    # sample mean of percolation threshold
    def mean(self) -> float:
        return StdStats.mean(self.T)

    # sample standard deviation of percolation threshold
    def stddev(self) -> float:
        return StdStats.stddev(self.T)

    # low endpoint of 95% confidence interval
    def confidence_lo(self) -> float:
        mean = self.mean()
        margin = 1.96 * self.stddev() / (len(self.T))**0.5
        return mean - margin

    # high endpoint of 95% confidence interval
    def confidence_hi(self) -> float:
        mean = self.mean()
        margin = 1.96 * self.stddev() / (len(self.T))**0.5
        return mean + margin

    # test client (see below)
    @staticmethod
    def main():
        import sys
        if len(sys.argv) != 3:
            print("Usage: python percolation_stats.py <grid size> <number of trials>")
            return

        n = int(sys.argv[1])
        trials = int(sys.argv[2])

        stats = PercolationStats(n, trials)
        print(f"mean                    = {stats.mean()}")
        print(f"stddev                  = {stats.stddev()}")
        print(f"95% confidence interval = [{stats.confidence_lo()}, {stats.confidence_hi()}]")


if __name__ == "__main__":
    PercolationStats.main()
