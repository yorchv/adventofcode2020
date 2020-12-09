
def processLine(index, inst, total):
    operation = inst[:3]
    argument = int(inst.split(' ')[1])

    print('processing', inst, index)
    if "nop" in operation:
        return (index + 1, total)
    
    if "acc" in operation:
        return (index + 1, total + argument)
    
    if "jmp" in operation:
        return (index + argument, total)

def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        last_index = len(lines)
        lines_processed = []

        index = 0
        total = 0
        while True:
            (new_index, new_total) = processLine(index, lines[index], total)
            if new_index in lines_processed:
                break

            if new_index is last_index:
                total = new_total
                print('FINAL')
                break
            else:
                index = new_index
                lines_processed.append(new_index)
                total = new_total

        print(total)
if __name__ == "__main__":
    main()