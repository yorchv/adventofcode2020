def find_by_bag_type(bag_type, bag_types, total):
    with open('test.txt') as f:
        lines = f.read().splitlines()
        subtotal = 0
        for line in lines:
            parts = line.split(' contain ')
            bag_name = parts[0][0:-5]
            content = parts[1].split(', ')
            for bag in content:
                if bag_type in bag:
                    bag_types.add(bag_name)
                    (subtypes, subtypes_total) = find_by_bag_type(bag_name, bag_types, subtotal)
                    subtotal += subtypes_total
                    bag_types.union(subtypes)

    return (bag_types, subtotal + total)

def main():
    bag_types = set()
    (types, total) = find_by_bag_type('shiny gold', bag_types, 0)
    result = len(list(types))
    print(result)
    print(total)

if __name__ == "__main__":
    main()