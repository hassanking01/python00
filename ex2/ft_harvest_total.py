def ft_harvest_total():
    i = 1
    total = 0
    while i <= 3:
        total = total + int(input(f"Day {i} harvest: "))
        i = i + 1
    print("Total harvest:", total)
