import art

print(art.logo)
bids = {}
input_next = "yes"
name = ""
bid = 0
max_bid = 0
winner = ""
# TODO-1: Ask the user for input
while input_next != "no":
    name = input("Please type your name: ")
    bid = float(input("Please type your bid $: "))
    input_next = input("Is there someone else to bid? Type: yes or no ")

    if input_next == "yes":
        print("\n" * 100)

    bids[name] = bid
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

for bid_value in bids:
    current = bids[bid_value]
    if current > max_bid:
        max_bid = current
        winner = bid_value


print(f"The winner of the bid is {winner} with offer: {max_bid}")