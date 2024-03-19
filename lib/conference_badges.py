def badge_maker(name): 
    return (f"Hello, my name is {name}.") 

# print(badge_maker("Bob"))

names = ["Arel", "Carol"]

def batch_badge_creator(names):
    name_badges = []
    for name in names:
        name_badges.append(f"Hello, my name is {name}.")
    return name_badges

# print(batch_badge_creator(names))

def assign_rooms(names):
    room_assignments = []
    for index, name in enumerate(names):
            room_assignments.append(f"Hello, {name}! You'll be assigned to room {index+1}!")
            index += 1
    return room_assignments

# print(assign_rooms(names))

def printer(names):
    # print(batch_badge_creator(names))
    for badge in batch_badge_creator(names):
        print(badge)
    # print(assign_rooms(names))
    for room in assign_rooms(names):
        print(room)
    # return None

printer(names)
