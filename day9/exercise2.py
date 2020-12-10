def main():
    value_to_find = 3199139634
    with open('input.txt') as f:
        lines = f.read().splitlines()
        lines = [int(n) for n in lines]
        final_list = []

        for first_index in range(0, len(lines)):
            values = []
            second_index = 0
            for i in range(second_index, len(lines)):
                values.append(lines[i + first_index])
                second_index += 1
                if sum(values) == value_to_find:
                    final_list = values
                    break
                if sum(values) > value_to_find:
                    break
            if final_list:
                break

        final_list.sort()
        print(sum([final_list[0], final_list[-1]]))


if __name__ == "__main__":
    main()