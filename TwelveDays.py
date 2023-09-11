def main():
    number = input("Please input a number between 1 and 12: ")

    try:
        number = int(number)
        if 1 <= number <= 12:
            print_twelve_days(number)
        else:
            raise ValueError
    except ValueError:
        print("Invalid number!")

def print_twelve_days(n):
    days = [
        "first", "second", "third", "fourth", "fifth", "sixth", 
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]
    
    gifts = [
        "A partridge in a pear tree.",
        "Two turtledoves, and",
        "Three French hens,",
        "Four calling birds,",
        "Five golden rings,",
        "Six geese a-laying,",
        "Seven swans a-swimming,",
        "Eight maids a-milking,",
        "Nine ladies dancing,",
        "Ten lords a-leaping,",
        "Eleven pipers piping,",
        "Twelve drummers drumming,"
    ]

    print(f"On the {days[n-1]} day of Christmas, my true love gave to me:")
    for i in range(n, 0, -1):
        print(gifts[i-1])

if __name__ == "__main__":
    main()

