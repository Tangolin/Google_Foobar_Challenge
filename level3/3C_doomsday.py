from fractions import Fraction, gcd


def matmul(a, b):
    c = []
    # multiply row by column
    for i in range(len(b[0])):
        sum = Fraction(0, 1)
        for j in range(len(a)):
            sum += a[j] * b[j][i]

        c.append(sum)

    return c


def change(a, b):
    sum = 0
    for i in range(len(a)):
        sum += abs(a[i]-b[i])

    return sum


def lcm(a):
    k = 1
    for i in a:
        k = k*i // gcd(k, i)
    
    return k


def solution(m):
    markov = []
    terminal_state = []

    for i, row in enumerate(m):
        denom = sum(row)

        # check for terminal state
        if denom == 0: 
            row[i] = 1
            denom = 1
            terminal_state.append(i)

        new_row = [Fraction(a, denom) for a in row]
        markov.append(new_row)

    steady_state = [Fraction(0, 1)] * len(m)
    steady_state[0] = Fraction(1, 1)
    new_steady_state = [Fraction(0, 1)] * len(m)
    old_steady_state = steady_state

    while(change(new_steady_state , old_steady_state) >= 0.00001):
        old_steady_state = steady_state
        new_steady_state = matmul(steady_state, markov)
        steady_state = new_steady_state

    for i in range(len(new_steady_state)):
        new_steady_state[i] = new_steady_state[i].limit_denominator(100)

    denoms = []
    numers = []

    for idx in terminal_state:
        denoms.append(new_steady_state[idx].denominator)
        numers.append(new_steady_state[idx].numerator)
    
    common_mul = lcm(denoms)
    for i in range(len(numers)):
        if denoms[i] != common_mul:
            numers[i] *= (common_mul/denoms[i])
    
    numers.append(common_mul)

    return list(map(int, numers))
