def temperature_converter():
    print("Temperature Converter")
    temp = float(input("Enter temperature: "))
    
    print("Convert to: ")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Fahrenheit")
    print("5. Kelvin to Celsius")
    print("6. Fahrenheit to Kelvin")
    
    choice = input("Enter choice (1/2/3/4/5/6): ")
    
    if choice == '1':
        converted = (temp * 9/5) + 32
        print(f"Temperature in Fahrenheit: {converted:.2f}°F")
    elif choice == '2':
        converted = (temp - 32) * 5/9
        print(f"Temperature in Celsius: {converted:.2f}°C")
    elif choice == '3':
        converted = temp + 273.15
        print(f"Temperature in Kelvin: {converted:.2f}K")
    elif choice == '4':
        converted = (temp - 273.15) * 9/5 + 32
        print(f"Temperature in Fahrenheit: {converted:.2f}°F")
    elif choice == '5':
        converted = temp - 273.15
        print(f"Temperature in Celsius: {converted:.2f}°C")
    elif choice == '6':
        converted = (temp - 32) * 5/9 + 273.15
        print(f"Temperature in Kelvin: {converted:.2f}K")
    else:
        print("Invalid choice. Please enter a valid option.")


temperature_converter()

