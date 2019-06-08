import itertools

def best_hand(hand):
    return max(itertools.combinations(hand, 5), key=hand_rank)


def best_wild_hand(hand):
    hands = set(best_hand(h)
                for h in itertools.product(*map(replacements, hand)))
    return max(hands, key=hand_rank)


redcards = [r + k for r in '23456789TJQKA' for k in 'DH']
blackcards = [r + k for r in '23456789TJQKA' for k in 'CS']
def replacements(card):
    if card == '?B': return blackcards
    elif card == '?R': return redcards
    else: return [card]

def best_wild_hand2(hand):
    return max(
        itertools.chain.from_iterable(
            replace_joker(hand) for hand in itertools.combinations(hand, 5)
        ), key=hand_rank)


def replace_joker(hand):
    jokers = [(r, s) for (r, s) in hand if r == '?']
    if len(jokers) == 0:
        yield hand
        raise StopIteration

    hand_without_jokers = tuple([c for c in hand if c[0] != '?'])
    joker_replacements = [redcards if s == 'R' else blackcards for (_, s) in jokers]
    for replacements in itertools.product(*joker_replacements):
        if any(c in hand_without_jokers for c in replacements):
            continue
        yield hand_without_jokers + replacements


def poker(hands):
    return allmax(hands, key=hand_rank)


def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    max_rank = max(map(key, iterable))
    return [hand for hand in iterable if key(hand) == max_rank]


def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, ranks)


CARD_NUMBERS = list(map(str, range(10))) + ['T', 'J', 'Q', 'K', 'A']
def card_ranks(cards):
    ranks = [CARD_NUMBERS.index(r) for (r, s) in cards]
    ranks.sort(reverse=True)
    return range(5, 0, -1) if ranks == [14, 5, 4, 3, 2] else ranks

def straight(ranks):
    return ranks == list(range(ranks[0], ranks[0] - 5, -1))

def flush(hand):
    return len(set([s for (r, s) in hand])) == 1

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    # pair = kind(2, ranks)
    # lowpair = kind(2, list(reversed(ranks)))
    # if pair and lowpair != pair:
    #     return (pair, lowpair)
    # return None
    pairs = [r for r in set(ranks) if ranks.count(r) == 2]
    if len(pairs) == 2:
        return tuple(sorted(pairs, reverse=True))

    return None

def test():
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    tp = "5S 5D 9H 9C 6S".split()
    al = "AC 2D 4H 3D 5S".split() # Ace-Low Straight

    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)

    assert(kind(4, fkranks) == 9)
    assert(kind(3, fkranks) == None)
    assert(kind(2, fkranks) == None)
    assert(kind(1, fkranks) == 7)

    assert(straight(card_ranks(al)) == True)

    assert(card_ranks(sf) == [10, 9, 8, 7, 6])
    assert(card_ranks(fk) == [9, 9, 9, 9, 7])
    assert(card_ranks(fh) == [10, 10, 10, 7, 7])

    assert(straight([9, 8, 7, 6, 5]) == True)
    assert(straight([9, 8, 8, 6, 5]) == False)
    assert(flush(sf) == True)
    assert(flush(fk) == False)

    assert(hand_rank(sf) == (8, 10))
    assert(hand_rank(fk) == (7, 9, 7))
    assert(hand_rank(fh) == (6, 10, 7))

    assert(poker([sf, fk, fh]) == [sf])
    assert(poker([fk, fh]) == [fk])
    assert(poker([fh, fh]) == [fh, fh])
    assert(poker([fh]) == [fh])
    assert(poker([sf] + 99 * [fh]) == [sf])

    sf1 = "6C 7C 8C 9C TC".split() # Straight Flush
    sf2 = "6D 7D 8D 9D TD".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    assert poker([sf1, sf2, fk, fh]) == [sf1, sf2]

    return "Tests pass"


def test_best_hand():
    assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split()))
            == ['6C', '7C', '8C', '9C', 'TC'])
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
            == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert (sorted(best_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_hand passes'


def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])

    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_wild_hand passes'


print(test())

print(test_best_hand())

print(test_best_wild_hand())
