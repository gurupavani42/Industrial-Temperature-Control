# Industrial-Temperature-Control
## Industrial Temperature Control — Simple Python Program

This program simulates an industrial temperature controller. If the temperature is too high, the **cooling system turns ON**; if it is too low, the **heater turns ON**.

```
temperature = float(input("Enter current temperature: "))

set_temperature = 25

if temperature > set_temperature:
    print("Temperature is HIGH")
    print("Cooling system: ON")

elif temperature < set_temperature:
    print("Temperature is LOW")
    print("Heater: ON")

else:
    print("Temperature is NORMAL")
    print("Heater: OFF")
    print("Cooling system: OFF")
```

### Example Output

```
Enter current temperature: 32
Temperature is HIGH
Cooling system: ON
```

### Another example

```
Enter current temperature: 20
Temperature is LOW
Heater: ON
```

**Project name:** Industrial Temperature Control System **Concepts used:** Temperature sensing, set point, heater control, cooling control, `if-elif-else` in Python.
