from collections import defaultdict

def main():
    with open('/Users/tomaskvapil/git/AoC/AoC/2022/inputs/03', 'r') as f:
        rucksacks = f.read().splitlines()

    item_to_priority = {}
    for i, ordinal in enumerate(range(ord('a'), ord('z')+1), start=1):
        item_to_priority[chr(ordinal)] = i
    for i, ordinal in enumerate(range(ord('A'), ord('Z')+1), start=27):
        item_to_priority[chr(ordinal)] = i
      
    priorities = []
    for rucksack in rucksacks:
        rucksack_len = int(len(rucksack)/2)
        c1 = set(rucksack[:rucksack_len])
        c2 =set(rucksack[rucksack_len:])
        duplicates = c1.intersection(c2)

        for item in duplicates:
            priorities.append(item_to_priority[item])
    part1 = sum(priorities)
    print(f'Sum of the priorities of duplicated items: {part1}')  

    groups = defaultdict(list)
    group = 1
    for i, rucksack in enumerate(rucksacks):
        if i > 0 and i % 3 == 0:
            group += 1
        groups[group] += [rucksack]
    
    priorities2 = []
    for values in groups.values():
        sets = [set(x) for x in values]
        shared = set.intersection(*sets)
        for item in shared:
            priorities2.append(item_to_priority[item])
    
    part2 = sum(priorities2)
    print(f'Sum of the priorities of duplicated items: {part2}')

if __name__ == '__main__':
    main()