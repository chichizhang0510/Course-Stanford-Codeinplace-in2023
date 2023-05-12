# Mars Weight Calculator
"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

def main():
    # Fill this function out!
    earth_w = float(input("Enter a weight on Earth: ") )
    mars_w = 37.8 / 100 * earth_w
    # print(f"The equivalent weight on Mars: {round(mars_w,2)}")
    # print("The equivalent weight on Mars: ",round(mars_w,2)) # easiest
    # print("The equivalent weight on Mars: "+str(round(mars_w,2)))
    
    print(f"The equivalent weight on Mars: {mars_w:.2f}")
    
    # print(f"string {variables}")

if __name__ == "__main__":
    main()
    
# Planetary Weight Calculator
"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""
FRACTION = {"Mercury":37.6 / 100,"Venus":88.9 / 100,"Mars":37.8 / 100,"Jupiter": 236.0 / 100,"Saturn":108.1 / 100,"Uranus":81.5 / 100,"Neptune":114.0 / 100}

def main():
    # Fill this function out!
    earth_w = float(input("Enter a weight on Earth: "))
    
    loop = True
    while loop:
        name_planet = input("Enter a planet: ")
        name_planet = name_planet.capitalize()
        if name_planet == "Mercury":
            planet_w = FRACTION["Mercury"] * earth_w
            loop = False
        elif name_planet == "Venus":
            planet_w = FRACTION["Venus"] * earth_w
            loop = False
        elif name_planet == "Mars":
            planet_w = FRACTION["Mars"] * earth_w
            loop = False
        elif name_planet == "Jupiter":
            planet_w = FRACTION["Jupiter"] * earth_w
            loop = False
        elif name_planet == "Saturn":
            planet_w = FRACTION["Saturn"] * earth_w
            loop = False
        elif name_planet == "Uranus":
            planet_w = FRACTION["Uranus"] * earth_w
            loop = False
        elif name_planet == "Neptune":
            planet_w = FRACTION["Neptune"] * earth_w
            loop = False
        else :
            print("Your input is invalid. Please try again.")

    print(f"The equivalent weight on {name_planet}: {round(planet_w,2)}")

if __name__ == "__main__":
    main()
