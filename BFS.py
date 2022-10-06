# BFS implementation based on number of islands leetcode #200

def no_islands(grid):
  if not grid:
      return 0

  dirs = [[0,1], [1,0], [0,-1], [-1,0]]
  num_islands = 0
  visited = set()

  def dfs(grid,r,c):
      if r<0 or c<0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
          return

      # grid[r][c] = "0"
      for x,y in dirs:
          if (r+x,c+y) not in visited:
              visited.add((r+x,c+y))
              dfs(grid, r+x, c+y)

  for r in range(len(grid)):
      for c in range(len(grid[0])):
              if grid[r][c] == "1":
                  if (r,c) not in visited:
                      visited.add((r,c))
                      num_islands += 1
                      dfs(grid, r,c)

  return num_islands
