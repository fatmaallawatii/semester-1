# Week 1.2, Session 2: Task 6



# Get user inputs
temperature = int(input("Enter temperature (°C): "))
pressure = int(input("Enter pressure (PSI): "))
status = int(input("Enter machine status (1 = operating, 0 = stopped): "))

# Check temperature
if temperature > 80:
    print("Temperature too high! Shut down the machine.")
elif temperature >= 50:
    print("Temperature is within safe limits.")
else:
    print("Temperature is low. No action needed.")

# Check pressure
if pressure > 100:
    print("High pressure detected! Maintenance needed.")
elif pressure >= 70:
    print("Pressure is stable.")
else:
    print("Pressure is low. System operating normally.")

# Check machine status
if status == 1:
    if temperature > 80 or pressure > 100:
        print("Machine is running in unsafe conditions! Shut it down.")
    else:
        print("Machine is running normally.")
else:
    print("Machine is stopped. No immediate action needed.")
