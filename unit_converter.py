print("1. Celsius to Farenheit")
print("2. Fahrenheit to Celsius")
choice = input("Choose an option: ")
if choice == "1":
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is {fahrenheit}°F")
elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is {celsius}°C")
else:
    print("Invalid choice.")
