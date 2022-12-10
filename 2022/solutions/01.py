from pathlib import Path

PATH = '/2022/inputs/01'

def main():
    with open(PATH, 'r') as f:
        elf_meals = f.read().split('\n\n')

    elf_cals = []    
    for elf in elf_meals:
        calories = sum(map(int, elf.splitlines()))
        elf_cals.append(calories)
    print(f'task 1: {max(elf_cals)}')    

    print(f'task 2: {sum(sorted(elf_cals)[-3:])}')

if __name__ == '__main__':
    main()