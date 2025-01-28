from lib.weighted_quick_union_uf import WeightedQuickUnionUF


class Percolation:
    # creates an n-by-n grid, with all sites initially blocked
    def __init__(self, n: int):
        if n <= 0:
            raise ValueError("n must be greater than 0")

        self.n = n
        self.grid_size = n * n
        self.opens = [False] * (self.grid_size + 2)
        self.uf = WeightedQuickUnionUF(self.grid_size + 2)
        self.virtual_top = 0
        self.virtual_bottom = self.grid_size + 1

        for col in range(n):
            self.uf.union(self.virtual_top, self._xy_to_1d(1, col))
            self.uf.union(self.virtual_bottom, self._xy_to_1d(n, col))

    # opens the site (row, col) if it is not open already
    def open(self, row: int, col: int) -> None:
        self.validate(row, col)
        if not self.is_open(row, col):
            site = self._xy_to_1d(row, col)
            self.opens[site] = True

            neighbors = [
                (row - 1, col), # up
                (row + 1, col), # down
                (row, col - 1), # left
                (row, col + 1), # right
            ]
            for r, c in neighbors:
                if self.is_valid(r, c) and self.is_open(r, c):
                    neighbor_site = self._xy_to_1d(r, c)
                    self.uf.union(site, neighbor_site)

    # is the site (row, col) open?
    def is_open(self, row: int, col: int) -> bool:
        self.validate(row, col)
        return self.opens[self._xy_to_1d(row, col)]

    # is the site (row, col) full?
    def is_full(self, row: int, col: int) -> bool:
        self.validate(row, col)
        site = self._xy_to_1d(row, col)
        return self.uf.connected(self.virtual_top, site)

    # returns the number of open sites
    def number_of_open_sites(self) -> int:
        return sum(self.opens)

    # does the system percolate?
    def percolates(self) -> bool:
        return self.uf.connected(self.virtual_top, self.virtual_bottom)

    # utils
    def validate(self, row: int, col: int) -> None:
        if row < 1 or row > self.n or col < 1 or col > self.n:
            raise ValueError("row and col must be between 1 and n")
        
    def is_valid(self, row: int, col: int) -> bool:
        return 1 <= row <= self.n and 1 <= col <= self.n
        
    def _xy_to_1d(self, row: int, col: int) -> int:
        return (row - 1) * self.n + col
    
    # test client (optional)
    @staticmethod
    def main():
        #test case 1
        test1 = Percolation(7)
        test1.open(1, 1)
        test1.open(1, 2)
        test1.open(1, 3)
        test1.open(1, 4)
        test1.open(1, 5)
        test1.open(1, 6)
        test1.open(1, 7)
        print(test1.is_open(1, 1))
        print(test1.is_open(2, 1))
        print(test1.is_full(1, 1)) 
        print(test1.is_full(2, 1)) 
        print(test1.number_of_open_sites())  
        print(test1.percolates())

if __name__ == "__main__":
    Percolation.main()
