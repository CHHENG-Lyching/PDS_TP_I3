def cel_to_fah(c, round_to=1):
    f = (c * 9/5) + 32
    return round(f, round_to)

def fah_to_cel(f, round_to=1):
    c = (f - 32) * 5/9
    return round(c, round_to)

print("a. Use a for loop with range(0, 101, 20) to print the conversion table below. ")
print("    °C   |   °F\n  -------+-------")
for c in range(0, 101, 20):
    print(f"{c:>5}°C  |  {cel_to_fah(c):.1f}°F")

print("\n\nb. Convert 98.6 °F (normal body temperature) to Celsius. ")
f = 98.6
c = fah_to_cel(f)
print(f"98.6 °F =  {c:.1f}°C")

print("\n\nc. Convert 37 °C (normal body temperature) to Fahrenheit and back again. Do you get 37.0 °F? ")
c = 37
f = cel_to_fah(c)
print(f"37.0 °C =  {f:.1f}°F")
print(f"Back to Celsius: {fah_to_cel(f)}°C (Check: {fah_to_cel(f) == c})")

print("\n\nd. Call one function with round_to=3")
result = fah_to_cel(98, round_to=3)
print("98°F to Celsius:", result)

