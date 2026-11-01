def describe(*numbers, decimals=2, label="Data"):
    if len(numbers) == 0:
        print("label : no values")
        return None
    mean = round(sum(numbers) / len(numbers), decimals)
    print(f"{label}: n={len(numbers)} min={min(numbers)} max={max(numbers)} mean={mean}")

def make_tag(text, **style):
    attrs= ""
    for key, value in style.items():
        attrs += f"{key} = {value}"
    return f"<span{ attrs }>{ text }</span>"

print()
describe(12, 7, 30, 4)
describe(3.14159, 2.71828, decimals=3, label="Constants")
describe()


print(make_tag(" Hello ", color=" red ", size=14))
square = lambda a: a * a
is_adult = lambda age: age >= 18
print(square(9), is_adult(17), is_adult(21))

