# This is the implementation of a hash map data structure in Python
class HashMap:
    # The constructor for the HashMap class
    # It takes in a parameter 'capacity' which represents the number of slots in the hash map
    # It initializes an empty list called 'map' and appends 'capacity' number of empty lists to it
    def __init__(self, capacity=10):
        self.map = []
        for _ in range(capacity):
            self.map.append([])

    # This method takes in a key and returns the index at which it should be stored in the 'map' list
    # using a hash function
    def create_hash_key(self, key):
        return int(key) % len(self.map)

    # This method takes in a key and a value and adds them to the hash map as a key-value pair
    def insert(self, key, value):
        # Calculate the index at which the key should be stored
        key_hash = self.create_hash_key(key)
        key_value = [key, value]  # Store the key-value pair as a list

        # If the slot at the calculated index is empty, add the key-value pair to that slot
        if self.map[key_hash] == None:
            self.map[key_hash] = list([key_value])
            return True
        # If the slot is not empty, check if the key already exists in the slot
        else:
            for pair in self.map[key_hash]:
                # If the key exists, update the value associated with that key
                if pair[0] == key:
                    pair[1] = key_value
                    return True
            # If the key does not exist in the slot, append the key-value pair to the end of the list
            self.map[key_hash].append(key_value)
            return True
        # This method takes in a key and a value and updates the value associated with that key in the hash map
    def update(self, key, value):
        # Calculate the index at which the key should be stored
        key_hash = self.create_hash_key(key)
        # If the slot at the calculated index is not empty, check if the key exists in the slot
        if self.map[key_hash] != None:
            for pair in self.map[key_hash]:
                # If the key exists, update the value associated with that key
                if pair[0] == key:
                    pair[1] = value
                    print(pair[1])  # Print the updated value
                    return True
        # If the key does not exist or the slot is empty, print an error message
        else:
            print('There was an error with updating on key: ' + key)

    # This method takes in a key and returns the value associated with that key in the hash map
    def get_value(self, key):
        # Calculate the index at which the key should be stored
        key_hash = self.create_hash_key(key)
        # If the slot at the calculated index is not empty, check if the key exists in the slot
        if self.map[key_hash] != None:
            for pair in self.map[key_hash]:
                # If the key exists, return the value associated with that key
                if pair[0] == key:
                    return pair[1]
        # If the key does not exist or the slot is empty, return None
        return None

    # This method takes in a key and removes the key-value pair associated with that key from the hash map
    def delete(self, key):
        # Calculate the index at which the key should be stored
        key_hash = self.create_hash_key(key)

        # If the slot at the calculated index is empty, return False
        if self.map[key_hash] == None:
            return False
        # If the slot is not empty, check if the key exists in the slot
        for i in range(0, len(self.map[key_hash])):
            # If the key exists, remove the key-value pair from the slot and return True
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        # If the key does not exist in the slot, return False
        return False

# This is a class that represents a single entry in the hash map
class HashTableEntry:
    def __init__(self, key, item):
        self.key = key
        self.item = item
