def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def recursive_count(i: int):
        if i > 0:
            recursive_count(i - 1)
            print("Day", i)
    recursive_count(days)
    print("Harvest time!")
