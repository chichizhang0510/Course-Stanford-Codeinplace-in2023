# Mars Weight Calculator
"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

def main():
    # Fill this function out!
    earth_w = int(input("Enter a weight on Earth: ") )
    mars_w = 37.8 / 100 * earth_w
    print(f"The equivalent weight on Mars: {round(mars_w,2)}")

if __name__ == "__main__":
    main()
    
# Planetary Weight Calculator
'''
Mercury: 37.6%
Venus: 88.9%
Mars: 37.8%
Jupiter: 236.0%
Saturn: 108.1%
Uranus: 81.5%
Neptune: 114.0%
'''
"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""

def main():
    # Fill this function out!
    earth_w = int(input("Enter a weight on Earth: "))
    # name_planet = capitalize(input("Enter a planet: "))
    name_planet = input(("Enter a planet: "))
    
    loop = True
    while loop:
        if name_planet == "Mercury":
            planet_w = 37.6 / 100 * earth_w
            loop = False
        elif name_planet == "Venus":
            planet_w = 88.9 / 100 * earth_w
            loop = False
        elif name_planet == "Mars":
            planet_w = 37.8 / 100 * earth_w
            loop = False
        elif name_planet == "Jupiter":
            planet_w = 236.0 / 100 * earth_w
            loop = False
        elif name_planet == "Saturn":
            planet_w = 108.1 / 100 * earth_w
            loop = False
        elif name_planet == "Uranus":
            planet_w = 81.5 / 100 * earth_w
            loop = False
        elif name_planet == "Neptune":
            planet_w = 114.0 / 100 * earth_w
            loop = False
        else :
            print("Your input is invalid. Please try again.")

    print(f"The equivalent weight on {name_planet}: {round(planet_w,2)}")

if __name__ == "__main__":
    main()

