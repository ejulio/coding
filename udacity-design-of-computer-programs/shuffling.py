import random
from collections import defaultdict

def shuffle(deck):
    "Knuth's Algorithm P."
    N = len(deck)
    for i in range(N - 1):
        swap(deck, i, random.randrange(i, N))


def shuffle1(deck):
    "Teacher's algorithm."
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i = random.randrange(N)
        j = random.randrange(N)
        swapped[i] = swapped[j] = True
        swap(deck, i, j)


def shuffle2(deck):
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i = random.randrange(N)
        j = random.randrange(N)
        swapped[i] = True
        swap(deck, i, j)


def shuffle3(deck):
    N = len(deck)
    for i in range(N):
        swap(deck, i, random.randrange(N))


def swap(deck, i, j):
    "Swap elements i and j of a collection"
    deck[i], deck[j] = deck[j], deck[i]


# A correct shuffling should give the same probability
# for all possible permutations
def test_shuffler(shuffler, deck='abcd', n=10000):
    counts = defaultdict(int)
    for _ in range(n):
        input = list(deck)
        shuffler(input)
        counts[''.join(input)] += 1

    e = n * 1.0 / factorial(len(deck))
    ok = all((0.9 <= counts[item] / e  <= 1.1) for item in counts)
    name = shuffler.__name__
    print('')
    print('%s(%s) %s' % (name, deck, 'ok' if ok else '** BAD **'))
    for (item, count) in sorted(counts.items()):
        print('%s: %4.1f' % (item, count * 100.0 / n))


def factorial(n):
    return 1 if (n <= 1) else n * factorial(n - 1)


print('Shuffling a deck.')
deck = [r + k for r in '23456789TJQKA' for k in 'CDHS']
print(deck)
shuffle(deck)
print(deck)


print('Testing shufflers.')
test_shuffler(shuffle)
test_shuffler(shuffle1)
test_shuffler(shuffle2)
test_shuffler(shuffle3)
