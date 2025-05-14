from __future__ import annotations


class Board:
    """
    Class that models an n-by-n sliding puzzle board.
    """

    def __init__(self, tiles: list[list[int]]):
        """
        Initializes the board from a given n-by-n list of lists.
        Each element is an integer in the range 0 to n^2 - 1, where 0 represents the blank space.
        """
        self._tiles = [row[:] for row in tiles]
        self._n = len(tiles)
        
        self._blank_row, self._blank_col = self._find_blank()
        
        self._manhattan_dist = self._calculate_manhattan()
        self._hamming_dist = self._calculate_hamming()
    
    def _find_blank(self) -> tuple[int, int]:
        """
        Helper method to find the position of the blank tile.
        """
        for i in range(self._n):
            for j in range(self._n):
                if self._tiles[i][j] == 0:
                    return i, j
        return -1, -1
    
    def dimension(self) -> int:
        """
        Returns the board dimension n.
        """
        return self._n
    
    def _calculate_hamming(self) -> int:
        """
        Calculate the Hamming distance to the goal board.
        """
        distance = 0
        for i in range(self._n):
            for j in range(self._n):
                tile = self._tiles[i][j]
                if tile != 0 and tile != i * self._n + j + 1:
                    distance += 1
        return distance
    
    def hamming(self) -> int:
        """
        Returns the number of tiles that are not in their goal position.
        Do not count the blank (0) in the Hamming score.
        """
        return self._hamming_dist
    
    def _calculate_manhattan(self) -> int:
        """
        Calculate the Manhattan distance to the goal board.
        """
        distance = 0
        for i in range(self._n):
            for j in range(self._n):
                tile = self._tiles[i][j]
                if tile != 0:
                    goal_row = (tile - 1) // self._n
                    goal_col = (tile - 1) % self._n
                    
                    distance += abs(goal_row - i) + abs(goal_col - j)
        return distance
    
    def manhattan(self) -> int:
        """
        Returns the sum of the Manhattan distances (vertical + horizontal)
        from the tiles to their goal positions.
        """
        return self._manhattan_dist
    
    def is_goal(self) -> bool:
        """
        Returns True if the board is the goal board.
        """
        # For the goal board, each tile should be i*n + j + 1, except the last position should be 0
        for i in range(self._n):
            for j in range(self._n):
                expected = i * self._n + j + 1
                # Last position should be 0
                if i == self._n - 1 and j == self._n - 1:
                    expected = 0
                if self._tiles[i][j] != expected:
                    return False
        return True
    
    def __eq__(self, other) -> bool:
        """
        Returns True if this board equals the other board.
        Two boards are equal if they have the same size and their corresponding tiles are equal.
        """
        if not isinstance(other, Board):
            return False
        
        if self._n != other._n:
            return False
        
        for i in range(self._n):
            for j in range(self._n):
                if self._tiles[i][j] != other._tiles[i][j]:
                    return False
        
        return True
    
    def __str__(self) -> str:
        """
        Returns a string representation of the board.
        First line contains the dimension n, followed by the n-by-n grid.
        """
        result = [str(self._n)]
        for row in self._tiles:
            result.append(' '.join(str(tile) for tile in row))
        return '\n'.join(result)
    
    def neighbors(self) -> list[Board]:
        """
        Returns an iterable (e.g., generator) of all neighboring boards.
        A neighbor is a board obtained by sliding a tile into the empty space.
        Depending on the position of the blank, there will be 2, 3, or 4 neighbors.
        """
        neighbors_list = []
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for d_row, d_col in directions:
            new_row, new_col = self._blank_row + d_row, self._blank_col + d_col
            
            if not (0 <= new_row < self._n and 0 <= new_col < self._n):
                continue
            
            new_tiles = [row[:] for row in self._tiles]
            new_tiles[self._blank_row][self._blank_col] = new_tiles[new_row][new_col]
            new_tiles[new_row][new_col] = 0
            
            neighbors_list.append(Board(new_tiles))
        
        return neighbors_list
        
    def twin(self) -> Board:
        """
        Returns a board that is a twin of the current board — obtained by swapping any pair
        of tiles (the blank should not be swapped).
        This is useful for detecting unsolvable puzzles.
        """
        twin_tiles = [row[:] for row in self._tiles]
        
        first_row, first_col = -1, -1
        second_row, second_col = -1, -1
        
        for i in range(self._n):
            for j in range(self._n):
                if twin_tiles[i][j] != 0:
                    first_row, first_col = i, j
                    break
            if first_row != -1:
                break
        
        for i in range(self._n):
            for j in range(self._n):
                if twin_tiles[i][j] != 0 and (i != first_row or j != first_col):
                    second_row, second_col = i, j
                    break
            if second_row != -1:
                break
    
        twin_tiles[first_row][first_col], twin_tiles[second_row][second_col] = \
            twin_tiles[second_row][second_col], twin_tiles[first_row][first_col]
        
        return Board(twin_tiles)


if __name__ == '__main__':
    # Add some basic tests to verify your Board methods.
    # For example, read a board from an input, print it, and check distances.

    test_tiles = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 8, 5]
    ]
    
    board = Board(test_tiles)
    print("Board:")
    print(board)
    print("Dimension:", board.dimension())
    print("Hamming distance:", board.hamming())
    print("Manhattan distance:", board.manhattan())
    print("Is goal?", board.is_goal())
    
    print("\nNeighbors:")
    for i, neighbor in enumerate(board.neighbors()):
        print(f"Neighbor {i+1}:")
        print(neighbor)
    
    print("\nTwin:")
    print(board.twin())