import math

def find_prime_numbers(max_num: int):
    pn_list = [] # 要素数 0 の配列
    for i in range(2, max_num + 1, 1):
        divide_flag = True

        # i の正の平方根の整数部分が 2 未満のときは、繰返し処理を実行しない
        for j in range(2, math.isqrt(i) + 1, 1): # α
            if i % j == 0:
                divide_flag = False
                break # α の行から始まる繰返し処理を終了する
        
        if divide_flag == True:
            pn_list.append(i)
    
    return pn_list

if __name__ == "__main__":
    N = int(input())
    print(*find_prime_numbers(N))