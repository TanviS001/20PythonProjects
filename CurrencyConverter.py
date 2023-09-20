def main():
    print("This program converts US dollars to Indian Rupees")
    print()

    dollars = eval(input("Enter amount in Dollars: "))

    inr = convert_to_inr(dollars)

    print("That is", inr, "Indian Rupees.")


convert_to_inr = lambda dollars: dollars * 82.72

main()
