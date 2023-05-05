from karel.stanfordkarel import *

# # Here is a place to program your Section problem


# ------------------my codes--------------------
def main():
    while front_is_clear():
        if beepers_present() :
            build()
        else:
            move()

def build():
    turn_left()
    mo_pu()
    mo_pu()
    turn_right()
    mo_pu()
    turn_right()
    mo_pu()
    mo_pu()
    turn_left()
    if front_is_blocked():
        facing_east()
    else:
        move()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def mo_pu():
    move()
    put_beeper()

if __name__ == '__main__':
    main()


# ------------------martin's codes--------------------


# Here is a place to program your Section problem

# def main():
#     """
#     Have Karel go to each beeper and build a hospital.
#     """
#     build_and_move()

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def build_column():
#     for i in range(2):
#         move()
#         put_beeper()

# def build_hospital():
#     turn_left()
#     build_column()
#     turn_right()
#     move()
#     turn_right()
#     put_beeper()
#     build_column()
#     turn_left()
#     if front_is_blocked():
#         facing_east()
#     else:
#         move()
    

# # def build_and_move():
# #     while no_beepers_present():
# #         move()
# #     build_hospital()
# #     if front_is_blocked():
# #         facing_east()
# #     else:
# #         move()
        
# def build_and_move():
#     while front_is_clear():
#         if beepers_present() :
#             build_hospital()
#         else:
#             move()

# if __name__ == '__main__':
#     main()

if __name__ == '__main__':
    main()
