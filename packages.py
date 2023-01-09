#import libraries
import datetime
import distance
import excel_reader
# initializing empty lists
first_delivery = []
second_delivery = []
third_delivery = []
first_truck_distances = []
second_truck_distances = []
third_truck_distances = []
#set time for trucks to leave
first_leave_times = ['8:00:00']
second_leave_times = ['9:10:00']
third_leave_times = ['11:00:00']
for index, value in enumerate(excel_reader.get_first_delivery()):
    excel_reader.get_first_delivery()[index][9] = first_leave_times[0]
    first_delivery.append(excel_reader.get_first_delivery()[index])
for index, outer in enumerate(first_delivery):
    for inner in distance.get_address():
        if outer[2] == inner[2]:
            first_truck_distances.append(outer[0])
            first_delivery[index][1] = inner[0]

# Call algorithm to sort packages for first truck
distance.get_shortest_route(first_delivery, 1, 0)
total_distance_1 = 0
for index in range(len(distance.first_truck_index())):
    try:
        total_distance_1 = distance.get_distance(int(distance.first_truck_index()[index]), int(distance.first_truck_index()[index + 1]), total_distance_1)
        
        deliver_package = distance.get_time(distance.get_current_distance(int(distance.first_truck_index()[index]), int(distance.first_truck_index()[index + 1])), first_leave_times)
        distance.first_truck_list()[index][10] = (str(deliver_package))
        excel_reader.get_hash_map().update(int(distance.first_truck_list()[index][0]), first_delivery)
    except IndexError:
        pass
for index, value in enumerate(excel_reader.get_second_delivery()):
    excel_reader.get_second_delivery()[index][9] = second_leave_times[0]
    second_delivery.append(excel_reader.get_second_delivery()[index])
for index, outer in enumerate(second_delivery):
    for inner in distance.get_address():
        if outer[2] == inner[2]:
            second_truck_distances.append(outer[0])
            second_delivery[index][1] = inner[0]

distance.get_shortest_route(second_delivery, 2, 0)
total_distance_2 = 0
for index in range(len(distance.second_truck_index())):
    try:
        total_distance_2 = distance.get_distance(int(distance.second_truck_index()[index]), int(distance.second_truck_index()[index + 1]), total_distance_2)
        
        deliver_package = distance.get_time(distance.get_current_distance(int(distance.second_truck_index()[index]), int(distance.second_truck_index()[index + 1])), second_leave_times)
        distance.second_truck_list()[index][10] = (str(deliver_package))
        excel_reader.get_hash_map().update(int(distance.second_truck_list()[index][0]), second_delivery)
    except IndexError:
        pass
for index, value in enumerate(excel_reader.get_final_delivery()):
    excel_reader.get_final_delivery()[index][9] = third_leave_times[0]
    third_delivery.append(excel_reader.get_final_delivery()[index])
for index, outer in enumerate(third_delivery):
    for inner in distance.get_address():
        if outer[2] == inner[2]:
            third_truck_distances.append(outer[0])
            third_delivery[index][1] = inner[0]
distance.get_shortest_route(third_delivery, 3, 0)
total_distance_3 = 0
for index in range(len(distance.third_truck_index())):
    try:
        total_distance_3 = distance.get_distance(int(distance.third_truck_index()[index]), int(distance.third_truck_index()[index + 1]), total_distance_3) 
        deliver_package = distance.get_time(distance.get_current_distance(int(distance.third_truck_index()[index]), int(distance.third_truck_index()[index + 1])), third_leave_times)
        distance.third_truck_list()[index][10] = (str(deliver_package))
        excel_reader.get_hash_map().update(int(distance.third_truck_list()[index][0]), third_delivery)
    except IndexError:
        pass
def total_distance():
    return total_distance_1 + total_distance_2 + total_distance_3