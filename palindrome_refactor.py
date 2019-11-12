def is_Palindrome(num):
    bin_num_str = str(bin(num)[2:])
    oct_num_str = str(oct(num)[2:])
    is_palindrome_decimal = str(num) == str(num)[::-1]
    is_palindrome_bin     = bin_num_str == bin_num_str[::-1]
    is_palindrome_oct     = oct_num_str == oct_num_str[::-1]
    return is_palindrome_decimal and is_palindrome_bin and is_palindrome_oct 

if __name__ == '__main__':
    n = 10
    while True:
        if is_Palindrome(n):
            break
        n = n + 1
    print(f"最小値は{n}")