size = 0
arr = []
first_largest = 0
second_largest = 0

while True:
  size = input("Enter Size: ")

  if size.isdigit():
    size  = int(size)
    break

  else:
    print("Error, please input number")

for i in range(0, size):
  num = input(f"Enter number {i+1}: ")
  while True:
    if num.isdigit():
      arr.append(int(num))
      break

    else:
      print("Error, please input number")

for i in arr:
  if i > first_largest:
    first_largest = i
  
  elif i > second_largest and i != first_largest:
    second_largest = i

print(first_largest, second_largest)
