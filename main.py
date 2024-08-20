def flatten(lst):
    """
    Flatten a nested list of integers into a single list.
    """
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(flatten(item))  # Recursively flatten and extend the result
        else:
            flattened.append(item)  # Append the integer directly
    return flattened

def flatten_and_sort(lst):
    """
    Flatten a nested list of integers and sort the resulting list in ascending order.
    """
    # Flatten the list
    flat_list = flatten(lst)
    # Sort the flattened list
    return sorted(flat_list)

# Example usage:
nested_array = [3, [1, [4, 2]], [5, [6]]]
result = flatten_and_sort(nested_array)
print(result)  # Output should be [1, 2, 3, 4, 5, 6]



class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
    
    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def flame_jet(self, other_pod):
        if isinstance(other_pod, Podracer):
            other_pod.condition = "trashed"

# Example usage:
# Create instances of each Podracer type
pod1 = Podracer(max_speed=300, condition="perfect", price=100000)
anakins_pod = AnakinsPod(max_speed=350, condition="perfect", price=150000)
sebubas_pod = SebulbasPod(max_speed=400, condition="perfect", price=200000)

# Repair a Podracer
print(f"Before repair: {pod1.condition}")  # Output: perfect
pod1.repair()
print(f"After repair: {pod1.condition}")  # Output: repaired

# Boost AnakinsPod
print(f"Before boost: {anakins_pod.max_speed}")  # Output: 350
anakins_pod.boost()
print(f"After boost: {anakins_pod.max_speed}")  # Output: 700

# Use SebulbasPod to trash another Podracer
print(f"Before flame_jet: {pod1.condition}")  # Output: repaired
sebubas_pod.flame_jet(pod1)
print(f"After flame_jet: {pod1.condition}")  # Output: trashed
