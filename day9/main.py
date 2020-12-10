def main():
    preamble = 25
    previous_list_length = 25
    with open('input.txt') as f:
        lines = f.read().splitlines()
        lines = [int(n) for n in lines]
        passcode = lines[preamble:]
        
        
        def is_invalid(value, index):
            previous = lines[index : index + previous_list_length]
            invalid = True
            for p in previous:
                for p2 in previous:
                    if p != p2:
                        if p + p2 == value:
                          invalid = False  
                    else:
                        continue
            return invalid
        
        initial = 0
        craked = []
        for value in passcode:
            craked.append(value) if is_invalid(value, initial) else None
            initial += 1

        print(craked)


if __name__ == "__main__":
    main()