from test_framework import generic_test

# 5.2
def plus_one(A):
    A[-1] += 1 #increment last digit by 1
    
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break # leave if no carry
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0) # add zero to last digit
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
