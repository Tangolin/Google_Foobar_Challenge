def solution(total_lambs):
    # most generous case is basically log2
    f_sum = 0
    n_0 = 0
    n_1 = 1
    num_generous = 0
    while (f_sum+n_1 <= total_lambs):
        f_sum += n_1
        n_1, n_0 = n_1*2, n_1
        num_generous += 1
    
    # least generous is basically fibonacci
    f_sum = 0
    n_0 = 0
    n_1 = 1
    num_stingy = 0
    while (f_sum+n_1 <= total_lambs):
        f_sum += n_1
        n_1, n_0 = n_1+n_0, n_1
        num_stingy += 1

    return num_stingy - num_generous
