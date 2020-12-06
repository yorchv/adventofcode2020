def main():
    with open('input.txt') as f:
        lines = f.read().split('\n\n')
        total = 0
        for line in lines:
            total_passangers = len(line.split('\n'))
            all_letters = line.replace('\n', '')
            total_in_all = 0
            for letter in list(set(all_letters)):
                total_in_all += 1 if all_letters.count(letter) == total_passangers else 0
            total += total_in_all
            
        print(total)
        
if __name__ == "__main__":
    main()