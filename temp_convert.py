#!/usr/bin/env python3
# Created by: Shem
# Created on: 2025/12/2
# This program converts a temperature from Celsius to Fahrenheit.

def fahrenheit():
    # Get temperature in Celsius (negative numbers allowed)
    celsius = float(input("Enter temperature in Celsius: "))

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
