    
def calculate_slope(right, down):
    with open('input.txt') as f:
        lines = list(f.read().splitlines())
        current_position = right
        max_position = len(lines[0]) - 1
        total_trees = 0
        offset = right - 1
        i = down

        while i < len(lines):
            print(i)
            if i % down == 0:
                print('internal', i)
                line = lines[i]
                if (line[current_position] == '#'):
                    total_trees += 1
                
                if current_position < (max_position - offset):
                    current_position += right
                else:
                    current_position = (current_position + offset) - max_position
            i += 1
        return total_trees

def main():
    slope_1 = calculate_slope(1, 1)
    slope_2 = calculate_slope(3, 1)
    slope_3 = calculate_slope(5, 1)
    slope_4 = calculate_slope(7, 1)
    slope_5 = calculate_slope(1, 2)
    print(slope_1 , slope_2 , slope_3 , slope_4 , slope_5)
    print(slope_1 * slope_2 * slope_3 * slope_4 * slope_5)

if __name__ == "__main__":
    main()