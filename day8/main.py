
def process_line(index, inst, total, switch_index):
    operation = inst[:3]
    argument = int(inst.split(' ')[1])
    is_switch = index == switch_index
    
    if is_switch:
        print('switch index', switch_index)
        print('processing', inst, index)
        if "jmp" in operation:
            print('jmp to nop')
            return (index + 1, total)
        
        if "nop" in operation:
            print('nop to jmp')
            return (index + argument, total)

    if "nop" in operation:
        return (index + 1, total)
    
    if "acc" in operation:
        return (index + 1, total + argument)
    
    if "jmp" in operation:
        return (index + argument, total)

def process_lines(lines, switch_index):
    last_index = len(lines)
    lines_processed = []

    index = 0
    total = 0
    while True:
        if index >= last_index:
            print('index is too large', index)
            return False
        (new_index, new_total) = process_line(index, lines[index], total, switch_index)
        if new_index in lines_processed:
            print(lines_processed)
            print('Repeated index', new_index)
            return False

        if new_index is last_index:
            total = new_total
            return total
        else:
            index = new_index
            lines_processed.append(new_index)
            total = new_total


def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()

        switch_indexes = []
        index = 0
        for line in lines:
            if "nop" in line or "jmp" in line:
                switch_indexes.append(index)
            index += 1

        for s in switch_indexes:
            print("+++++++++++++++")
            print("testing index", s)
            print("+++++++++++++++")
            result = process_lines(lines, s)
            print("+++++++++++++++")
            if result:
                print(result)
                break

if __name__ == "__main__":
    main()