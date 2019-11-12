def is_Palindrome(num):
    dec_num_str = str(num)
    bin_num_str = str(bin(num)[2:])
    oct_num_str = str(oct(num)[2:])
    is_palindrome_decimal = dec_num_str == dec_num_str[::-1]
    is_palindrome_bin     = bin_num_str == bin_num_str[::-1]
    is_palindrome_oct     = oct_num_str == oct_num_str[::-1]
    return is_palindrome_decimal and is_palindrome_bin and is_palindrome_oct 

if __name__ == '__main__':
    N = 1000
    for i in range(10,N):
        if is_Palindrome(i):
            print(i)
            break