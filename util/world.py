from api.models import Room
import random


class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0

    def generate_rooms(self, size_x, size_y, num_rooms):

        # Initialize the grid's height
        self.grid = [None] * size_y
        self.width = size_x
        self.height = size_y

        # fill the row up with an array of None
        for i in range(len(self.grid)):
            self.grid[i] = [None] * size_x

        # Start from lower-left corner (0,0)
        x = -1  # (this will become 0 on the first step)
        y = 0
        # set to 1 so id can begin at 1
        room_count = 1

        # Start generating rooms to the east
        direction = 1  # 1: east, -1: west

        # While there are rooms to be created...
        previous_room = None

        # use to reverse the direction of the room
        reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e", "err": "err"}

        # will be used to create chasm
        break_choices = [False, True, False, False, False]

        while room_count <= num_rooms:

            # Calculate the direction of the room to be created
            if direction > 0 and x < size_x - 1:
                room_direction = "e"
                x += 1
            elif direction < 0 and x > 0:
                room_direction = "w"
                x -= 1
            else:
                # REMOVED THE NORTH SOUTH MAPPING AT THE ENDS OF THE MAP
                # # If we hit a wall, turn north and reverse direction
                # set the direction to something useless
                room_direction = "err"
                y += 1
                direction *= -1

            # THIS CREATES A CHASM IN THE EAST-WEST CONNECTION AT RANDOM POINTS
            # if 1 < y < (size_y - 3)
            if 1 < y < (size_y - 3):
                # randomize break_choices
                choice = random.choice(break_choices)
                # if true break the connection by setting the room direction to err
                if choice:
                    room_direction = "err"

            # Create a room in the given direction
            room = Room(id=room_count, title="A Generic Room",
                        description="This is a generic room.", x=x, y=y)
            # Note that in Django, you'll need to save the room after you create it
            room.save()

            # Save the room in the World grid
            self.grid[y][x] = room

            # Connect the new room to the previous room
            if previous_room is not None:
                previous_room.connectRooms(room, room_direction)
                room.connectRooms(previous_room, reverse_dirs[room_direction])

            # Update iteration variables
            previous_room = room
            room_count += 1

        # THIS STEP DOWNWARD WILL CREATE NORTH-SOUTH CONNECTIONS AT RANDOM POINTS IN THE MAP
        # set room_count to zero again
        room_count = 0
        # set x and y to zero
        x = 0
        y = 0
        # set another variable index to zero
        # create an array range to hold choices
        choices = [False, True, False, False, True]
        # loop while room_count is less than num_rooms
        while room_count < num_rooms:
            # if y is less than size_y
            if y < size_y - 1:
                # randomize choices
                # if true set a northward position
                if random.choice(choices):
                    # connect with the room to the north
                    self.grid[y][x].connectRooms(self.grid[y + 1][x], "n")
                    self.grid[y + 1][x].connectRooms(self.grid[y][x], "s")

            # increment x
            x += 1
            # increment room_count
            room_count += 1

            # if x is at the last position increment y and reset x
            if x == size_x:
                x = 0
                y += 1

    def print_rooms(self):

        # Add top border
        str = "# " * ((3 + self.width * 5) // 2) + "\n"

        # The console prints top to bottom but our array is arranged
        # bottom to top.
        #
        # We reverse it so it draws in the right direction.
        reverse_grid = list(self.grid)  # make a copy of the list
        reverse_grid.reverse()
        for row in reverse_grid:
            # PRINT NORTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.n_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
            # PRINT ROOM ROW
            str += "#"
            for room in row:
                if room is not None and room.w_to is not None:
                    str += "-"
                else:
                    str += " "
                if room is not None:
                    str += f"{room.id}".zfill(3)
                else:
                    str += "   "
                if room is not None and room.e_to is not None:
                    str += "-"
                else:
                    str += " "
            str += "#\n"
            # PRINT SOUTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.s_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"

        # Add bottom border
        str += "# " * ((3 + self.width * 5) // 2) + "\n"

        # Print string
        print(str)
