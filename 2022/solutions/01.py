def main():
    with open('/Users/tomaskvapil/git/AoC/AoC/2022/inputs/01', 'r') as f:
        food_list = f.read().split('\n\n')

    meals = []
    for food in food_list:
        calories = sum(map(int, food.split('\n')))
        meals.append(calories)
        
    part1 = max(meals)
    print(f'Most calories carried by elf: {part1}')

    part2 = sum(sorted(meals)[-3:])
    print(f'Total calories carried by the top three elves: {part2}')

if __name__ == '__main__':
    main()