from lib.weighted_quick_union_uf import WeightedQuickUnionUF


class Percolation:
    # creates an n-by-n grid, with all sites initially blocked
    def __init__(self, n: int):
        if n <= 0:
            raise ValueError("n must be greater than 0")

        self.n = n
        self.grid_size = n * n
        self.opens = [False] * (self.grid_size + 2)
        self.virtual_top = 0
        self.virtual_bottom = self.grid_size + 1
        self.uf = WeightedQuickUnionUF(self.grid_size + 2)
        
        for col in range(self.n+1):
            self.uf.union(self.virtual_top, col)

        for col in range(self.grid_size - self.n, self.grid_size + 1):
            self.uf.union(self.virtual_bottom, col)

    # opens the site (row, col) if it is not open already
    def open(self, row: int, col: int) -> None:
        self.validate(row, col)
        if not self.is_open(row, col):
            site = self.matrix_to_array(row, col)
            self.opens[site] = True

            neighbors = [
                (row - 1, col), # up
                (row + 1, col), # down
                (row, col - 1), # left
                (row, col + 1), # right
            ]
            for neighbor_row, neighbor_col in neighbors:
                if self.is_valid(neighbor_row, neighbor_col) and self.is_open(neighbor_row, neighbor_col):
                    neighbor_site = self.matrix_to_array(neighbor_row, neighbor_col)
                    self.uf.union(site, neighbor_site)


    # is the site (row, col) open?
    def is_open(self, row: int, col: int) -> bool:
        self.validate(row, col)
        site = self.matrix_to_array(row, col)
        return self.opens[site]
    

    # is the site (row, col) full?
    def is_full(self, row: int, col: int) -> bool:
        self.validate(row, col)
        site = self.matrix_to_array(row, col)
        if self.is_open(row, col):
            return self.uf.connected(self.virtual_top, site)
        else:
            return False

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
        
    def matrix_to_array(self, row: int, col: int) -> int:
        return (row - 1) * self.n + col
    
    # test client (optional)
    @staticmethod
    def main():
        pass

if __name__ == "__main__":
    Percolation.main()
