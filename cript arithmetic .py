from itertools import permutations

def solve_cryptarithmetic():
    letters = 'SENDMORY'
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))

        # Skip if leading letters are zero
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue

        send = 1000 * mapping['S'] + 100 * mapping['E'] + 2 * mapping['N'] + mapping['D']
        more = 1000 * mapping['M'] + 100 * mapping['O'] + 2 * mapping['R'] + mapping['E']
        money = 10000 * mapping['M'] + 1000 * mapping['O'] + 100 * mapping['N'] + 10 * mapping['E'] + mapping['Y']

        if send + more == money:
            print(f"SEND: {send}, MORE: {more}, MONEY: {money}")
            print("Mapping:", mapping)
            return

solve_cryptarithmetic()
