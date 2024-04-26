items_file = open("items.txt", "r")
expense_file = open("expense_report.txt", "w")

items = {}

for line in items_file:
    item = line.split()[0]
    price = int(line.split()[1])

    if item in items.keys():
        old_total = items.get(item)
        new_total = old_total + price
        items.update({item:new_total})
    else:
        items[item] = price

total = sum(items.values())

for key, value in items.items():
    expense_file.write("%s: %d\n" % (key, value))

expense_file.write("total: %d" % total)

items_file.close()
expense_file.close()

    