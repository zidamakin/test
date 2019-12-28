def squares_needed(grains):
    count = 0
    grains_in_square = int()
    for  num in range(0, 65):
        grains_in_square += 2 ** num
        count += 1
        if grains == 0:
            return 0
        if grains <= grains_in_square:
            return count
