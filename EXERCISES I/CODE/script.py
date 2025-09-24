import array
room_counts = [12, 18, 25, 9, 30, 22]
total_occupancy = sum(room_counts)
average_occupancy = total_occupancy / len(room_counts)
min_occupancy = min(room_counts)
max_occupancy = max(room_counts)
report = (
    f"Room Occupancy Report:\n"
    f"Total Occupancy: {total_occupancy}\n"
    f"Average Occupancy: {average_occupancy:.2f}\n"
    f"Minimum Occupancy: {min_occupancy}\n"
    f"Maximum Occupancy: {max_occupancy}\n"
)
print(report)
threshold = 20
if average_occupancy > threshold and max_occupancy > 25:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")
room_names = ["Room A", "Room B", "Room C", "Room D", "Room E"]
print("Original Room List:", room_names)

room_names.append("Room F")
room_names = [room for room in room_names if "C" not in room]
room_names.sort()
print("Updated Room List:", room_names)
room_array = array.array('i', room_counts[:4])
array_sum = sum(room_array)
list_sum = sum(room_counts[:4])
print(f"Array Sum: {array_sum}, List Sum: {list_sum}")

room_data = [
    {"id": 1, "name": "Room A", "value": 12},
    {"id": 2, "name": "Room B", "value": 18},
    {"id": 3, "name": "Room C", "value": 25},
    {"id": 4, "name": "Room D", "value": 9},
]
for room in room_data:
    if room["name"] == "Room B":
        room["value"] = 20
room_data = [room for room in room_data if room["name"] != "Room C"]
total_value = sum(room["value"] for room in room_data)
print(f"Total Occupancy from Dictionary Records: {total_value}")