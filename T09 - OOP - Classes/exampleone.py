# Attributes: features of the house

"""""
size: s,m,l
color: white, red, red
number of room: 2-10
type of flooring: hardwood, carpet or tile

"""
# Methods(Behaviors)

"""
opening doors-open a door in house
turning on lights-this will turn on lights in house
cleaning-clean the house

Methods are...a function that belongs to a class
"""

# Instances(Objects)
""""
The houses built of the blueprint provided
"""


class HousePlan:
    def __init__(self, u_size, u_colour, u_num_rooms, u_floor):  # constructer method
        self.size = u_size
        self.color = u_colour
        self.num_rooms = u_num_rooms
        self.floor = u_floor

    def openDoor(self):
        print("The door has been opened.")

    def lightSwitch(self):
        # NOTE can add contional to ceck light status
        print("Light has been turned on.")

    def RumbClean(self):
        print("House has been cleaned.")


h_size = input("what size housewould you prefer (small, medium, large): ")
h_color = input("what color housewould you prefer (blue, green, red)): ")
h_num = int(input("house_num: "))
h_flooring = input("flooring")

kitt_house = HousePlan(h_size, h_color, h_num, h_flooring)

print(
    f"""
      ......................................................
      Size:{kitt_house.size}
      Colour:{kitt_house.color}
      Number of rooms:{kitt_house.num_rooms}
      Flooring:{kitt_house.floor}
      ........................................................."""
)

kitt_house.openDoor()
kitt_house.lightSwitch()
kitt_house.RumbClean()
