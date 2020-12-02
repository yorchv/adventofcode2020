def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        numbers = [int(n) for n in lines]
        numbers.sort()
        lowest_number = numbers[0]
        probable_numbers = list(filter(lambda x: x < (2020 - lowest_number), numbers))
        bellow_middle = filter(lambda x: x <= 1010, list(probable_numbers))
        after_middle = filter(lambda x: x > 1010, list(probable_numbers))
        bellow_list = list(bellow_middle)
        after_list = list(after_middle)
        first_number = 0
        second_number = 0
        for first in bellow_list:
            for _second in after_list:
                if first + _second == 2020:
                    first_number = first
                    second_number = _second
        print(first_number, second_number, first_number * second_number)

        

if __name__ == "__main__":
    main()