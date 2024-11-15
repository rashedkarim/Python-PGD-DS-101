sum = 0
while True:
    num = input("Enter a number: ")
    if num == "quit":
        break
    if num.isnumeric():
        sum += int(num)

    # try:
    #     num = int(num)
    # except:
    #     print("Enter a valid number please")
    #     continue


print(sum)