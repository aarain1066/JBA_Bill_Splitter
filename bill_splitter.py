# Asim Arain
# JBA Bill Splitter Part 3

#--------------------------

import random
party = []

print("Enter the number of friends joining (including you):")
party_size = int(input())

if party_size <= 0:
    print("\nNo one is joining for the party")
else:
    print("\nEnter the name of every friend (including you), each on a new line:")
    while len(party) < party_size:
        party.append(input())
    print("Enter the total bill value:")
    bill_value = float(input())
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    enable_lucky = input()
    if enable_lucky == 'Yes':
        party_dict = dict.fromkeys(party)
        lucky_split_value = round(bill_value / (party_size - 1), 2)
        lucky_one = random.choice(list(party_dict))
        print(f"{lucky_one} is the lucky one!\n")
        for party_member in party_dict:
            if party_member != lucky_one:
                party_dict[str(party_member)] = lucky_split_value
            elif party_member == lucky_one:
                party_dict[str(party_member)] = 0
        print("\n", party_dict)
    elif enable_lucky == 'No':
        split_value = round(bill_value / party_size, 2)
        party_dict = dict.fromkeys(party, split_value)
        print("No one is going to be lucky")
        print("\n", party_dict)
        
        
