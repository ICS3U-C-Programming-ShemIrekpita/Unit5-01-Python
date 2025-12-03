#!/usr/bin/env python3
# Created by: Shem
# Created on: 2025/12/2
# This program converts a temperature from Celsius to Fahrenheit.

def fahrenheit():
    # Keep asking until a valid non-negative decimal number is entered
    while True:
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            if celsius < 0:
                print("Error: Temperature cannot be negative.\n")
            else:
                break
        except ValueError:
            print("Error: Please enter a valid decimal number.\n")
    # Convert Celsius to Fahrenheit
    fahrenheit = (9 / 5) * celsius + 32
    # Display the result
    print("Temperature in Fahrenheit:", fahrenheit)
    # Thank you message
    print("Thank you for using the program")
    print(" /\\_/\\  ")
    print("( ^_^ )")
    print(" > ^ < ")
def main():
    fahrenheit()

if __name__ == "__main__":
    main()
