
def powerRecursive(base, power):
    if power == 0:
        return 1
    else:
        return base * powerRecursive(base, power-1)


if __name__ == '__main__':
    base = 3
    power = 2
    print(powerRecursive(base, power))
