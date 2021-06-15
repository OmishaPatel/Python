def minimum_rooms(intervals):
    starting_time = [i[0] for i in intervals]
    ending_time = [i[1] for i in intervals]

    starting_time.sort()
    ending_time.sort()

    starting_index = ending_index = 0
    max_rooms = current_room = 0

    while starting_index < len(starting_time) and ending_index < len(ending_time):
        if starting_index >= len(starting_time):
            break

        if starting_time[starting_index] < ending_time[ending_index]:
            current_room +=1
            starting_index +=1

        else:
            current_room -= 1
            ending_index += 1
    max_rooms = max(max_rooms, current_room)
    return max_rooms



print(minimum_rooms([(30, 75), (0, 50), (60, 150)]))
print(minimum_rooms([(5, 7), (0, 9), (5, 9)]))
print(minimum_rooms([]))