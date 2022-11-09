# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


# Opdracht 1 klaar


def greet(name, greeting_template='Hello, <name>!'):
    x = greeting_template.replace("<name>", name)
    return x


print(greet("Bob"))
print(greet("Dre", "Waaazzzuppp <name>"))


# opdracht 2 klaar


def force(mass, body="earth"):
    planets = {
        "earth": 9.798,
        "sun": 274,
        "jupiter": 24.92,
        "neptune": 11.15,
        "saturn": 10.44,
        "uranus": 8.87,
        "venus": 8.87,
        "mars": 3.71,
        "mercury": 3.7,
        "moon": 1.62,
        "pluto": 0.58,
    }
    return (mass * round(planets[body], 1))


print(force(float(500), str("sun")))


# opdracht 3

def pull(m1, m2, d):
    return ((6.674*10**-11) * ((float(m1) * float(m2)) / (float(d**2))))


print(pull(800, 1500, 3))
