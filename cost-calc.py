# Ask the user for their name
name = input("Enter your name: ")

# Ask the user for the file they want to open
file_name = input("Enter the name of the file you want to open: ")

# Open the input file for reading
with open(file_name, 'r') as file:
    # Rest of the code...
    item_totals = {}
    # Variable to store the overall total
    overall_total = 0

    # Read each line in the file
    for line in file:
        # Split the line into item and price
        item, price = line.strip().split()

        # Convert the price to a float
        price = float(price)

        # Add the price to the total for the item
        if item in item_totals:
            item_totals[item] += price
        else:
            item_totals[item] = price

        # Add the price to the overall total
        overall_total += price
# Ask the user for the file they want to write to
output_file = input("Enter the name of the file you want to write to: ")

# Open the output file for writing
with open(output_file, 'w') as file:

    # Write the user's name to the output file
    file.write(f'{name} expense report\n')

    # Write the totals to the output file
    for item, total in item_totals.items():
        file.write(f'{item}: {total}\n')

    # Write the overall total to the output file
    file.write(f'Overall Total: {overall_total}\n')
