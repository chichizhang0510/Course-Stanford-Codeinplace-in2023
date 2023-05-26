# ------------------ MY SOLUTION ------------------
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
        if name_planet in FRACTION:
            planet_w = FRACTION[name_planet] * earth_w
            loop = False
        else:
            print("Your input is invalid. Please try again.")
#         if name_planet == "Mercury":
#             planet_w = FRACTION["Mercury"] * earth_w
#             loop = False
#         elif name_planet == "Venus":
#             planet_w = FRACTION["Venus"] * earth_w
#             loop = False
#         elif name_planet == "Mars":
#             planet_w = FRACTION["Mars"] * earth_w
#             loop = False
#         elif name_planet == "Jupiter":
#             planet_w = FRACTION["Jupiter"] * earth_w
#             loop = False
#         elif name_planet == "Saturn":
#             planet_w = FRACTION["Saturn"] * earth_w
#             loop = False
#         elif name_planet == "Uranus":
#             planet_w = FRACTION["Uranus"] * earth_w
#             loop = False
#         elif name_planet == "Neptune":
#             planet_w = FRACTION["Neptune"] * earth_w
#             loop = False
#         else :
#             print("Your input is invalid. Please try again.")

    print(f"The equivalent weight on {name_planet}: {round(planet_w,2)}")

if __name__ == "__main__":
    main()

    
    
    
# --------------------- LEADER'S SOLUTION ---------------------------
# Section 3 Solutions
# '''Mars Weight Solution

# There are three key stages to solving this problem:

# Getting the Earthling's weight from them, which we need the input function for. 

# Converting the Earthing's weight from a string to a number so we can do math with it. We use the float function to do this, since the weight isn't necessarily a whole number

# Calculating the weight on Mars, which we do by multiplying the Earth weight by 0.378. To make the program easy to read, we store this number in a constant called MARS_MULTIPLE.

# Check out the solution code to see all of these stages in action!'''

# """
# Prompts the user for a weight on Earth
# and prints the equivalent weight on Mars.
# """

# # We use constants!
# MARS_MULTIPLE = 0.378

# def main():
#     earth_weight_str = input('Enter a weight on Earth: ')

#     # Get the numeric value since input() returns a value in string form
#     earth_weight = float(earth_weight_str)

#     # Having a variable for each piece of information is a good habit
#     mars_weight = earth_weight * MARS_MULTIPLE
#     rounded_mars_weight = round(mars_weight, 2)


#     # Note the string concatenation!
#     print('The equivalent weight on Mars: ' + str(rounded_mars_weight))

# if __name__ == '__main__':
#     main()
    
    
# # Planetary Weights Solution
# '''
# There are two key parts to this solution:

# Everything from the first part of the problem: getting a user's input, converting it to a float to do the calculation, and covering it to a string to print it out.

# Using if statements to check which gravitational constant to use based on the user's input.  '''
# Solution

# """
# Prompts the user for a weight on Earth
# and a planet (in separate inputs). Then 
# prints the equivalent weight on that planet.

# Note that the user should type in a planet with 
# the first letter as uppercase, and you do not need
# to handle the case where a user types in something 
# other than one of the planets (that is not Earth). 
# """

# MERCURY_GRAVITY = 0.376
# VENUS_GRAVITY = 0.889
# MARS_GRAVITY = 0.378
# JUPITER_GRAVITY = 2.36
# SATURN_GRAVITY = 1.081
# URANUS_GRAVITY = 0.815
# NEPTUNE_GRAVITY = 1.14
# EARTH_GRAVITY = 1.0

# def main():
#     # Prompt the user for their weight on Earth
#     earth_weight = float(input("Enter a weight on Earth: "))

#     # Prompt the user for the name of a planet
#     planet = input("Enter a planet: ")

#     # Determine the gravitational constant for the selected planet
#     if planet == "Mercury":
#         gravity_constant = MERCURY_GRAVITY
#     elif planet == "Venus":
#         gravity_constant = VENUS_GRAVITY
#     elif planet == "Mars":
#         gravity_constant = MARS_GRAVITY
#     elif planet == "Jupiter":
#         gravity_constant = JUPITER_GRAVITY
#     elif planet == "Saturn":
#         gravity_constant = SATURN_GRAVITY
#     elif planet == "Uranus":
#         gravity_constant = URANUS_GRAVITY
#     else:
#         # can assume user types in one of these planets, so this can be an else instead of elif
#         gravity_constant = NEPTUNE_GRAVITY

#     # Calculate the equivalent weight on the selected planet
#     planetary_weight = earth_weight * gravity_constant
#     rounded_planetary_weight = round(planetary_weight, 2)

#     # Print the result
#     print("The equivalent weight on " + planet + ":  " + str(rounded_planetary_weight))

# if __name__ == "__main__":
#     main()
