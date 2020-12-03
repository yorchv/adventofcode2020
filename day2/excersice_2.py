def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        total = 0
        ## Line Format
        ## 3-7 g: gggbggsgg
        for l in lines:
            splited_line = l.split(':')
            pwd = splited_line[1][1:]
            rule = splited_line[0]
            letter = rule.split()[1]
            values = rule.split()[0].split('-')
            index_1 = int(values[0])
            index_2 = int(values[1])
            
            if pwd[index_1 - 1] == letter and pwd[index_2 - 1] != letter:
                total += 1
            if pwd[index_1 - 1] != letter and pwd[index_2 - 1] == letter:
                total += 1

        print(total)

if __name__ == "__main__":
    main()