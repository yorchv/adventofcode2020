def calculate(instructions, length):
    origin = list(range(length))
    for i in range(len(instructions)):
        letter = instructions[i]
        start = 0 if letter is 'F' or letter is 'L' else length / 2
        end = length / 2 if letter is 'F' or letter is 'L' else length
        origin = origin[start:end]
        length = length / 2
    return origin[0]

def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        
        seatIds = []

        for line in lines:
            rowInstruction = line[:7]
            columnInstruction = line[-3:]
            rowValue = calculate(rowInstruction, 128)
            columnValue = calculate(columnInstruction, 8)
            total = rowValue * 8 + columnValue
            seatIds.append(total)
    
    seatIds.sort()

    for seat in seatIds:
    print(seatIds)
        
if __name__ == "__main__":
    main()