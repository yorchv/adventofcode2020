def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        numbers = [int(n) for n in lines]
        numbers.sort()
        lowest_number = numbers[0]
        probable_numbers = list(filter(lambda x: x < (2020 - lowest_number), numbers))
        
        first_number = 0
        second_number = 0
        third_number = 0
        for first in probable_numbers:
            for second in probable_numbers:
                for third in probable_numbers:
                    if first + second + third == 2020:
                        first_number = first
                        second_number = second
                        third_number = third
                        break
        print(first_number, second_number, third_number, first_number * second_number * third_number)

        

if __name__ == "__main__":
    main()