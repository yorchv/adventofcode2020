def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        total = 0
        ## Line Format
        ## 3-7 g: gggbggsgg
        for l in lines:
            splited_line = l.split(':')
            pwd = splited_line[1]
            rule = splited_line[0]
            letter = rule.split()[1]
            values = rule.split()[0].split('-')
            min_value = int(values[0])
            max_value = int(values[1])
            recurrences = pwd.count(letter)
            if recurrences >= min_value and recurrences <= max_value:
                total += 1

        print(total)

if __name__ == "__main__":
    main()