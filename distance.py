#import libraries
import csv
import datetime

# Open the distance data CSV file and store the contents in a list
with open('./data/WGUPS_distance_data.csv') as csvfile_1:
    distance_csv = list(csv.reader(csvfile_1, delimiter=','))
# Open the distance name data CSV file and store the contents in a list
with open('./data/WGUPS_distance_name_data.csv') as csvfile_2:
    WGUPS_distance_name_csv = list(csv.reader(csvfile_2, delimiter=','))
# Define a function to return the list of addresses
    def get_address():
        return WGUPS_distance_name_csv
# Define a function to calculate the total distance between two locations
    def get_distance(row, col, total):
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[col][row]
    # Retrieve the distance from the distance data list
        return total + float(distance)
# Define a function to retrieve the current distance between two locations
    def get_current_distance(row, col):
        distance = distance_csv[row][col]
    # If the distance is not available, retrieve it from the other direction
        if distance == '':
            distance = distance_csv[col][row]
    # If the distance is not available, retrieve it from the other direction
        return float(distance)
    # Retrieve the distance from the distance data list
    def get_time(distance, truck_list):
        new_time = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(
            *divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        truck_list.append(final_time)
# Initialize a variable to store the total time
        total = datetime.timedelta()
# Iterate through the list of times and add them up

        for i in truck_list:
            (hrs, mins, secs) = i.split(':')
            total += datetime.timedelta(hours=int(hrs),
                                        minutes=int(mins), seconds=int(secs))
        return total

    first_truck = []
    first_truck_indices = []
    second_truck = []
    second_truck_indices = []
    third_truck = []
    third_truck_indices = []

# Define a function to calculate the time it takes to travel a certain distance
    def get_shortest_route(_list, num, curr_location):
        if not len(_list):
            return _list

        lowest_value = 50.0
        location = 0

        for i in _list:
            value = int(i[1])
            if get_current_distance(curr_location, value) <= lowest_value:
                lowest_value = get_current_distance(
                    curr_location, value)
                location = value

        for i in _list:
            if get_current_distance(curr_location, int(i[1])) == lowest_value:
                if num == 1:
                    first_truck.append(i)
                    first_truck_indices.append(i[1])
                    _list.pop(_list.index(i))
                    curr_location = location
                    get_shortest_route(_list, 1, curr_location)
                elif num == 2:
                    second_truck.append(i)
                    second_truck_indices.append(i[1])
                    _list.pop(_list.index(i))
                    curr_location = location
                    get_shortest_route(_list, 2, curr_location)
                elif num == 3:
                    third_truck.append(i)
                    third_truck_indices.append(i[1])
                    _list.pop(_list.index(i))
                    curr_location = location
                    get_shortest_route(_list, 3, curr_location)

    first_truck_indices.insert(0, '0')
    second_truck_indices.insert(0, '0')
    third_truck_indices.insert(0, '0')

    def first_truck_index():
        return first_truck_indices

    def first_truck_list():
        return first_truck

    def second_truck_index():
        return second_truck_indices

    def second_truck_list():
        return second_truck

    def third_truck_index():
        return third_truck_indices

    def third_truck_list():
        return third_truck
