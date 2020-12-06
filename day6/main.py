def main():
    with open('input.txt') as f:
        total = sum([len(list(set(line.replace('\n', '')))) for line in f.read().split('\n\n')])
        print(total)
        
if __name__ == "__main__":
    main()