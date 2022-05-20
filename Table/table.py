def table(num):
    with open(f"{num}", "a") as file:
        file.write(f"********* {num} Table ***********\n")
        for i in range(1, 11):
            file.write(f"{num} X {i} = {num * i}\n")
        file.write("********************************")


if __name__ == '__main__':
    number = int(input("Enter the number: "))
    table(number)
    print("Successfully!!!!")
