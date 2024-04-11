from time import perf_counter, sleep


def brewCoffee():
    print('Start brewCoffee()')
    sleep(3)
    print('  Stop brewCoffee()')
    return '\tCoffee done!'


def toastBread():
    print('Start toastBread()')
    sleep(2)
    print('  Stop toastBread()')
    return '\tBread done!'


def fryEggsAndHam():
    print('Start fryEggsAndHam()')
    sleep(4)
    print('  Stop fryEggsAndHam()')
    return '\tEggs and Ham done!'


def main():
    t1 = perf_counter()
    coffee_result = brewCoffee()
    print(coffee_result)
    bread_result = toastBread()
    print(bread_result)
    eggs_ham_result = fryEggsAndHam()
    print(eggs_ham_result)
    t2 = perf_counter()
    print(f'It took {t2 - t1:.2f} seconds!')


if __name__ == '__main__':
    main()
