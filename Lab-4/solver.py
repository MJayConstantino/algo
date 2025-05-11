from __future__ import annotations
import heapq
import sys
from board import Board


class SearchNode:
    """Helper class to represent a search node in the A* algorithm."""
    
    def __init__(self, board: Board, moves: int, previous: SearchNode = None):
        self.board = board
        self.moves = moves
        self.previous = previous
        self.manhattan = board.manhattan()
        self.priority = self.manhattan + moves
    
    def __lt__(self, other):
        """Comparison method for the priority queue."""
        return self.priority < other.priority


class Solver:
    """
    Class that solves the n-by-n sliding puzzle using the A* search algorithm.
    """
    
    def __init__(self, initial: Board):
        """
        Find the solution to the initial board using the A* algorithm.
        If the initial board is None, raise a ValueError.
        """
        if initial is None:
            raise ValueError("Initial board cannot be None")
        
        self._initial = initial
        self._solution_path = None
        self._moves_count = -1
        self._solvable = False
        
        # Solve the puzzle
        self._solve()
    
    def _solve(self):
        """
        Implements the A* search algorithm to solve the puzzle.
        Uses the Manhattan distance as the heuristic.
        """
        # Create a priority queue for the main search
        pq = []
        initial_node = SearchNode(self._initial, 0)
        heapq.heappush(pq, initial_node)
        
        # Create a priority queue for the twin search
        twin_pq = []
        twin_initial_node = SearchNode(self._initial.twin(), 0)
        heapq.heappush(twin_pq, twin_initial_node)
        
        # Use dictionaries to keep track of visited boards
        visited = {}
        twin_visited = {}
        
        # Main search loop
        while pq and twin_pq:
            # Process a node from the main search
            node = heapq.heappop(pq)
            
            # If we've reached the goal, reconstruct the path
            if node.board.is_goal():
                self._solvable = True
                self._moves_count = node.moves
                self._reconstruct_path(node)
                return
            
            # Add current board to visited
            visited[str(node.board)] = True
            
            # Process neighbors
            for neighbor_board in node.board.neighbors():
                neighbor_str = str(neighbor_board)
                # Skip if we've already visited this board or if it's the same as the previous board
                if (neighbor_str in visited or 
                    (node.previous is not None and neighbor_board == node.previous.board)):
                    continue
                
                # Add neighbor to the priority queue
                neighbor_node = SearchNode(neighbor_board, node.moves + 1, node)
                heapq.heappush(pq, neighbor_node)
            
            # Process a node from the twin search
            twin_node = heapq.heappop(twin_pq)
            
            # If the twin search reaches the goal, then the original board is unsolvable
            if twin_node.board.is_goal():
                self._solvable = False
                self._moves_count = -1
                self._solution_path = None
                return
            
            # Add current twin board to visited
            twin_visited[str(twin_node.board)] = True
            
            # Process twin neighbors
            for twin_neighbor_board in twin_node.board.neighbors():
                twin_neighbor_str = str(twin_neighbor_board)
                # Skip if we've already visited this board or if it's the same as the previous board
                if (twin_neighbor_str in twin_visited or 
                    (twin_node.previous is not None and twin_neighbor_board == twin_node.previous.board)):
                    continue
                
                # Add twin neighbor to the priority queue
                twin_neighbor_node = SearchNode(twin_neighbor_board, twin_node.moves + 1, twin_node)
                heapq.heappush(twin_pq, twin_neighbor_node)
    
    def _reconstruct_path(self, goal_node: SearchNode):
        """Reconstructs the solution path from the goal node."""
        path = []
        current = goal_node
        
        # Traverse backwards from the goal node to the initial node
        while current is not None:
            path.append(current.board)
            current = current.previous
        
        # Reverse the path to get from initial to goal
        self._solution_path = list(reversed(path))
    
    def is_solvable(self) -> bool:
        """
        Returns True if the initial board is solvable.
        """
        return self._solvable
    
    def moves(self) -> int:
        """
        Returns the minimum number of moves required to solve the puzzle,
        or -1 if the puzzle is unsolvable.
        """
        return self._moves_count
    
    def solution(self) -> list[Board]:
        """
        Returns a list of Board objects representing the sequence of moves from the
        initial board to the goal board, if the puzzle is solvable. Otherwise, return None.
        """
        return self._solution_path if self._solvable else None


def main():
    """Test client for the Solver class."""
    if len(sys.argv) != 2:
        print("Usage: python solver.py [input_file]")
        return
    
    try:
        with open(sys.argv[1], 'r') as f:
            # The first integer is the board dimension n
            n = int(f.readline().strip())
            tiles = []
            for _ in range(n):
                row = list(map(int, f.readline().split()))
                tiles.append(row)
            
            initial_board = Board(tiles)
            solver = Solver(initial_board)
            
            if not solver.is_solvable():
                print("No solution possible")
            else:
                print("Minimum number of moves =", solver.moves())
                for board in solver.solution():
                    print(board)
                    print()  # Add an extra newline for readability
    except FileNotFoundError:
        print(f"Error: File {sys.argv[1]} not found.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()