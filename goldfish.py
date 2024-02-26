import numpy as np

## Initialize parameters
deck  =  {'Land': 35, 'Ramp': 11, 'Draw': 11, 'Counter': 10, 'Other': 32}
keep  =  {'Land':  2, 'Ramp':  1, 'Draw':  1, 'Counter':  0, 'Other':  0}
mulls = [{'Land':  3, 'Ramp':  1, 'Draw':  1, 'Counter':  1, 'Other':  0},
         {'Land':  3, 'Ramp':  1, 'Draw':  1, 'Counter':  0, 'Other':  0},
         {'Land':  2, 'Ramp':  1, 'Draw':  1, 'Counter':  0, 'Other':  0}]

sims = 1_000_000
turns = 5

## Initialize results
results = [{x: 0 for x in deck} for _ in range(turns + 1)]
M = 0

## Preprocessing
deck_list = [x for x, y in deck.items() for _ in range(y)]

## Run simulation(s)
for _ in range(sims):

    # Mulligan
    for m in range(len(mulls) + 2):
        np.random.shuffle(deck_list)
        hand = deck_list[0:7]
        if all(hand.count(x) >= keep[x] for x in keep):
            break

    # Discard
    for x in range(m - 1):
        for y in hand:
            if hand.count(y) > mulls[x][y]:
                hand.remove(y)
                break

    # Update results
    M += m
    for x in hand:
        results[0][x] += 1
    for x in range(1, turns + 1):
        hand += [deck_list[6 + x]]
        for y in hand:
            results[x][y] += 1

## Print results
print(f'Mulligans: {M/sims}')
for w, x in enumerate(results):
    print(f'\n---- Turn {w} ----')
    for y, z in x.items():
        print(f'{y}: {z/sims}')