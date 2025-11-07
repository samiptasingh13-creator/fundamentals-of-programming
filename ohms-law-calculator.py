print(" Ohm's Law Calculator ")
print("Formula: V = I × R")
print("Choose what you want to calculate:")
print("1. Voltage (V)")
print("2. Current (I)")
print("3. Resistance (R)")

choice = input("Enter your choice (1/2/3): ")

if choice == '1':
    current = float(input("Enter current (in Amperes): "))
    resistance = float(input("Enter resistance (in Ohms): "))
    voltage = current * resistance
    print(f"Voltage = {voltage:.2f} Volts")

elif choice == '2':
    voltage = float(input("Enter voltage (in Volts): "))
    resistance = float(input("Enter resistance (in Ohms): "))
    current = voltage / resistance
    print(f"Current = {current:.2f} Amperes")

elif choice == '3':
    voltage = float(input("Enter voltage (in Volts): "))
    current = float(input("Enter current (in Amperes): "))
    resistance = voltage / current
    print(f"Resistance = {resistance:.2f} Ohms")

else:
    print("Invalid choice! Please enter 1, 2, or 3.")
