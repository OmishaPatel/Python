from collections import deque

def shortest_path(board, start, end):
    seen = set()
    queue = deque([(start,0)])
    while queue:
        #enque 
        coordinate,count = queue.popleft()

        if coordinate == end:
            return count
        seen.add(coordinate)

        neighbors = get_valid_neighbors(board, coordinate[0], coordinate[1])
        queue.extend((neighbor, count+1)for neighbor in neighbors if neighbor not in seen)
    
def get_valid_neighbors(board, row, col):
    return [(r,c) for r,c in [
        #up
        (row - 1, col),
        #down
        (row + 1 , col),
        #left
        (row, col - 1),
        #right
        (row, col + 1)
    ] if is_valid(board, r,c)]
    


def is_valid(board, row,col):
    return (row >= 0) and (row < len(board)) and (col >= 0) and (col < len(board[0]))
    
mat = [ ['0', '1', '0', '1'],
          [ '1', '0', '1', '1'],
          [ '0', '1', '1', '1'],
          [ '1', '1', '1', '0']]
print(shortest_path(mat,(0,3),(3,0)))