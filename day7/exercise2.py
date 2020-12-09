def find_by_bag_type(bag_type):
    with open('input.txt') as f:
        lines = f.read().splitlines()
        subtotal = 1
        print('checking: ', bag_type.replace(' ', '#'))
        
        def find_bag_inst(line):
            return line.startswith(bag_type)
        line = list(filter(find_bag_inst, lines))[0]

        parts = line.split(' contain ')
        content = parts[1].split(', ')
        for child_bag in content:
            print('content', content)
            if 'no other bags' in child_bag:
                subtotal = 1
            else:
                num_bags = int(child_bag[:1])
                child_bag_name = child_bag[2:].replace('.', '').replace(' bags','').replace(' bag', '')
                subtotal += num_bags * find_by_bag_type(child_bag_name)
        print('subtotal bags in: ', bag_type, subtotal)
        return subtotal

def main():
    total = find_by_bag_type('shiny gold')
    print(total - 1)

if __name__ == "__main__":
    main()