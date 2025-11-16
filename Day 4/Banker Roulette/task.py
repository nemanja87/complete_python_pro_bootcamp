import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_name_code = random.randint(0, len(friends) - 1)

print(f"Person who will pay the bill is: {friends[random_name_code]}")