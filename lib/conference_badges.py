def badge_maker(name): 
    return (f"Hello, my name is {name}.") 

print(badge_maker("Bob"))

names = ["Arel", "Carol"]

def batch_badge_creator(names):
     return [(f"Hello, my name is {name}.") for name in names]

    # name_badges = []
    # for name in names:
    #     name_badges.append(f"Hello, my name is {name}.")
    # return name_badges
#above 4 lines work and pass tests, but the list comprehension is best solution 

print(batch_badge_creator(names))

def assign_rooms(names):
    room_assignments = []
    for index, name in enumerate(names):
            room_assignments.append(f"Hello, {name}! You'll be assigned to room {index+1}!")
            index += 1
    return room_assignments

print(assign_rooms(names))

def printer(names):
    [print(badge) for badge in batch_badge_creator(names)]
    [print(room) for room in assign_rooms(names)]

    # for badge in batch_badge_creator(names): 
        # print(badge)
    # for room in assign_rooms(names):
        # print(room)
    # 4 lines above work properly and pass tests, though top two list comprehensions are most succinct

    # print(batch_badge_creator(names)) creates list; doesnt iterate through
    # print(assign_rooms(names)) creates list; doesnt iterate through

printer(names)
