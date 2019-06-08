import itertools
import time


def nextto(h1, h2):
    return abs(h1 - h2) == 1


def imright(h1, h2):
    return h1 - h2 == 1


def zebra_puzzle():
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in c(orderings)
                if imright(green, ivory)
                for (Englishman, Spaniard, Ukranian, Japanse, Norwegian) in c(orderings)
                if Englishman is red
                for (dog, snails, fox, horse, ZEBRA) in c(orderings)
                if Spaniard is dog
                if Norwegian is first
                if nextto(Norwegian, blue)
                for (coffee, tea, milk, oj, WATER) in c(orderings)
                if coffee is green
                if Ukranian is tea
                if milk is middle
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in c(orderings)
                if OldGold is snails
                if Kools is yellow
                if nextto(Chesterfields, fox)
                if nextto(Kools, horse)
                if LuckyStrike is oj
                if Japanse is Parliaments
                )


def timedcall(fn, *args):
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return (t1 - t0, result)


def average(numbers):
    return sum(numbers) / float(len(numbers))


def timedcalls(n, fn, *args):
    if isinstance(n, int):
        times = [timedcall(fn, *args)[0] for _ in range(n)]
    else:
        times = []
        while sum(times) < n:
            times.append(timedcall(fn, *args)[0])
    return (min(times), average(times), max(times))


def instrument_fn(fn, *args):
    c.starts = c.items = 0
    result = fn(*args)
    print('%s got %s with %5d iters over %7d items' % (fn.__name__, result, c.starts, c.items))


def c(sequence):
    c.starts += 1
    for item in sequence:
        c.items += 1
        yield item


instrument_fn(zebra_puzzle)

print(timedcalls(10.0, zebra_puzzle))
