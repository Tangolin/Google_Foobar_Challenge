import math 
import time

def re_solution(n):
    n = int(n)
    if n == 1:
        return 0

    if n%2 == 0:
        return 1 + re_solution(n/2)
    
    else:
        return 1 + min(re_solution(n+1), re_solution(n-1))


def solution(n):
    n = int(n)
    count = 0

    while n != 1:
        if n % 2 == 0:
            n /= 2
        
        else:
            high = 2 ** math.ceil(math.log(n)/math.log(2))
            low = 2 ** math.floor(math.log(n)/math.log(2))
            mid = (high + low) / 2
            if abs(high - n) == 1:
                n = high
            elif abs(low - n) == 1:
                n = low
            elif abs(mid - n) == 1:
                n = mid
            else:
                x = n - 1
                x /= 2
                if x % 2 == 0:
                    n -= 1
                else:
                    n += 1
        
        count += 1
    
    return count


if __name__ == '__main__':
    n = int(input("Enter value: "))
    cur_time = time.time()
    print(solution(n))
    print('iterative time: ', time.time()-cur_time)
    cur_time = time.time()
    print(re_solution(n))
    print('recursive time: ', time.time()-cur_time)
    print(solution(n)==re_solution(n))
