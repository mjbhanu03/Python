arr = []
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of cols: "))

for i in range(0, rows):
  row = []
  for j in range(0, cols):
    row.append(int(input(f"Enter value for Row {i+1}, Col {j+1}: ")))
  arr.append(row)

for i in range(rows):
  for j in range(i+1, cols):
    temp = arr[i][j]
    arr[i][j] = arr[j][i]
    arr[j][i] = temp

for i in range(rows):
    start = 0
    end = cols - 1
    while start < end:
        temp = arr[i][start]
        arr[i][start] = arr[i][end]
        arr[i][end] = temp
        start += 1
        end -= 1
        
for i in arr: 
  print(i)