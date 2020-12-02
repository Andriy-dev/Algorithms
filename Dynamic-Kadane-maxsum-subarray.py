'''
Find the maximum sum of the subarray in array

Using Kadane algorithm (https://youtu.be/86CQq3pKSUw)
https://en.wikipedia.org/wiki/Maximum_subarray_problem

1. Backward-looking
2. Forward looking

'''

def max_sum_subrarray_backward(l):
    if len(l) == 0:
        return None
    
    max_subarray = l[0]
    max_subarray_representation = [l[0]]
    previous_subarray = l[0]
    previous_subarray_representation = [l[0]]


    for idx in range(1,len(l)):
        #print(f'idx={idx} Comparing {previous_subarray} and {l[idx]} + {previous_subarray} = {l[idx] + previous_subarray} , max_subarray = {max_subarray}')
        if l[idx] > l[idx] + previous_subarray:
            previous_subarray = l[idx]
            previous_subarray_representation = [l[idx]]
        else:
            previous_subarray+= l[idx]
            previous_subarray_representation+= [l[idx]]
        if previous_subarray > max_subarray:
            max_subarray = previous_subarray
            max_subarray_representation = previous_subarray_representation[:]

    return(max_subarray,max_subarray_representation)

def max_sum_subrarray_forward(l):
    if len(l) == 0:
        return None
    
    max_subarray = l[-1]
    next_subarray = l[-1]

    for idx in range(len(l) - 2,-1,-1):
        #print(f'idx={idx} Comparing {next_subarray} and {l[idx]} + {next_subarray} = {l[idx] + next_subarray} , max_subarray = {max_subarray}')
        next_subarray = max(l[idx],l[idx] + next_subarray)
        max_subarray = max(next_subarray,max_subarray)

    return(max_subarray)

if __name__ == '__main__':
    print(max_sum_subrarray_backward([-1,1,2,-10,-20,30,-100,29,1,1]))
    print(max_sum_subrarray_forward([-1,1,2,-10,-20,30,-100,29,1,1]))

    print(max_sum_subrarray_backward([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(max_sum_subrarray_forward([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   

