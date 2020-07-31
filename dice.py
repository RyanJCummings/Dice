import secrets

def roll(size, number):
    value = 0
    result = 0
    for i in range(int(number)):
        value = secrets.randbelow(int(size) + 1)
        text = "Roll number {}: {}"
        print(text.format(i + 1, value))
        result += value
    return result

def main():
    which_die = input("Which die? ")
    how_many = input("How many? ")
    text = "Result: " + str(roll(which_die, how_many))
    print(text)

main()
