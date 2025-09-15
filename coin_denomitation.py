amt = 0
number_of_coins = 0
coins = []
amt_left = 0
coins_used = []
while True:
  amt = input("Enter amount: ")
  if amt.isdigit():
    amt = int(amt)
    amt_left = amt
    break
  
  else:
    print("Please, enter valid number")


while True:
  number_of_coins = input("Enter number of coins: ")
  if number_of_coins.isdigit():
    number_of_coins = int(number_of_coins)
    break
  
  else:
    print("Please, enter valid number")

for i in range(0, number_of_coins):
  while True:
    coin = input(f"Enter coin {i} value: ")
    if coin.isdigit():
      coin = int(coin)
      coins.append(coin)
      break
  
    else:
      print("Please, enter valid coin value")

coins.sort(reverse=True)

for i in coins:
  while True:
    if amt_left >= i:
      amt_left -= i
      coins_used.append(i)

    else:
      break

for i in coins_used:
  print(i)
