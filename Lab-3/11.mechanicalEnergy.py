from scipy.constants import g
m = float(input("Enter the mass: "))
h = float(input("Enter the height: "))

v = float(input("Enter the velocity: "))

e = m*g*h + 0.5 * m * v**2

print(f"The energy generted by mass: {m} at height: {h} and velocity: {v} is {e}")