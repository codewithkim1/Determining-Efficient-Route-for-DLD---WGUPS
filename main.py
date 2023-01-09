# Mail me: codewithkim1@gmail.com
from excel_reader import get_hash_map
from packages import total_distance
import datetime
class Main:
    print('------------------------------')
    print('Western Governors University Parcel Service')
    print('------------------------------\n')
    print(f'Route finished in {total_distance():.2f} miles.\n')

    user_input = input(""" SELECT or TYPE 'cancel' to stop:
    1. Get info for all packages at a particular time
    2. Get info for a single package at a particular time


    >>: """)

    while user_input != 'cancel':
        if user_input == '1':
            try:
                input_time = input('Enter a time (HH:MM:SS): ')
                (hrs, mins, secs) = input_time.split(':')
                convert_user_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                for count in range(1,41):
                    try:
                        first_time = get_hash_map().get_value(str(count))[9]
                        second_time = get_hash_map().get_value(str(count))[10]
                        (hrs, mins, secs) = first_time.split(':')
                        convert_first_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                        (hrs, mins, secs) = second_time.split(':')
                        convert_second_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                    except ValueError:
                        pass
                    if convert_first_time >= convert_user_time:
                        get_hash_map().get_value(str(count))[10] = 'At Hub'
                        get_hash_map().get_value(str(count))[9] = 'Leaves at ' + first_time
                        print(
                            f'Package ID: {get_hash_map().get_value(str(count))[0]}, '
                            f'Delivery status: {get_hash_map().get_value(str(count))[10]}'
                        )
                    elif convert_first_time <= convert_user_time:
                        if convert_user_time < convert_second_time:
                            get_hash_map().get_value(str(count))[10] = 'In transit'
                            get_hash_map().get_value(str(count))[9] = 'Left at ' + first_time

                            # Print package's current info
                            print(
                                f'Package ID: {get_hash_map().get_value(str(count))[0]}, '
                                f'Delivery status: {get_hash_map().get_value(str(count))[10]}'
                            )

                        # Determine which packages have already been delivered
                        else:
                            get_hash_map().get_value(str(count))[10] = 'Delivered at ' + second_time
                            get_hash_map().get_value(str(count))[9] = 'Left at ' + first_time

                            # Print package's current info
                            print(
                                f'Package ID: {get_hash_map().get_value(str(count))[0]}, '
                                f'Delivery status: {get_hash_map().get_value(str(count))[10]}'
                            )
            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print('Invalid entry!')
                exit()
        elif user_input == '2':
            try:
                count = input('Enter Package ID: ')
                first_time = get_hash_map().get_value(str(count))[9]
                second_time = get_hash_map().get_value(str(count))[10]
                input_time = input('Enter a time (HH:MM:SS): ')
                (hrs, mins, secs) = input_time.split(':')
                convert_user_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                (hrs, mins, secs) = first_time.split(':')
                convert_first_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                (hrs, mins, secs) = second_time.split(':')
                convert_second_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                if convert_first_time >= convert_user_time:

                    get_hash_map().get_value(str(count))[10] = 'At Hub'
                    get_hash_map().get_value(str(count))[9] = 'Leaves at ' + first_time
                    print(
                        f'Package ID: {get_hash_map().get_value(str(count))[0]}\n'
                        f'Street address: {get_hash_map().get_value(str(count))[2]}\n'
                        f'Required delivery time: {get_hash_map().get_value(str(count))[6]}\n'
                        f'Package weight: {get_hash_map().get_value(str(count))[7]}\n'
                        f'Truck status: {get_hash_map().get_value(str(count))[9]}\n'
                        f'Delivery status: {get_hash_map().get_value(str(count))[10]}\n'
                    )
                elif convert_first_time <= convert_user_time:
                    if convert_user_time < convert_second_time:
                        get_hash_map().get_value(str(count))[10] = 'In transit'
                        get_hash_map().get_value(str(count))[9] = 'Left at ' + first_time
                        print(
                            f'Package ID: {get_hash_map().get_value(str(count))[0]}\n'
                            f'Street address: {get_hash_map().get_value(str(count))[2]}\n'
                            f'Required delivery time: {get_hash_map().get_value(str(count))[6]}\n'
                            f'Package weight: {get_hash_map().get_value(str(count))[7]}\n'
                            f'Truck status: {get_hash_map().get_value(str(count))[9]}\n'
                            f'Delivery status: {get_hash_map().get_value(str(count))[10]}\n'
                        )
                    else:
                        get_hash_map().get_value(str(count))[10] = 'Delivered at ' + second_time
                        get_hash_map().get_value(str(count))[9] = 'Left at ' + first_time

                        # Print package's current info
                        print(
                            f'Package ID: {get_hash_map().get_value(str(count))[0]}\n'
                            f'Street address: {get_hash_map().get_value(str(count))[2]}\n'
                            f'Required delivery time: {get_hash_map().get_value(str(count))[6]}\n'
                            f'Package weight: {get_hash_map().get_value(str(count))[7]}\n'
                            f'Truck status: {get_hash_map().get_value(str(count))[9]}\n'
                            f'Delivery status: {get_hash_map().get_value(str(count))[10]}\n'
                        )
            except ValueError:
                print('Invalid entry')
                exit()
        elif user_input == 'cancel':
            exit()
        else:
            print('Invalid entry!')
            exit()