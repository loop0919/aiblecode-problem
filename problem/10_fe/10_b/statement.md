# 問題文
中島くんは、引数で与えられた整数以下の、全ての素数だけを格納した配列を返す関数を作成している途中です。

$N$ 以下の素数すべてを昇順に出力してください。

ここで、以下のコードテンプレートを利用して書いても構いません。

<details>
<summary>コードテンプレート</summary>
<div>

コードテンプレートは以下の通りです。「空欄 a」と「空欄 b」を埋めてください。

```py
import math

def find_prime_numbers(max_num: int):
    pn_list = [] # 要素数 0 の配列
    for i in range(2, '''空欄 a''' + 1, 1):
        divide_flag = True

        # i の正の平方根の整数部分が 2 未満のときは、繰返し処理を実行しない
        for j in range(2, math.isqrt(i) + 1, 1): # α
            if '''空欄 b''':
                divide_flag = False
                break # α の行から始まる繰返し処理を終了する
        
        if divide_flag == True:
            pn_list.append(i)
    
    return pn_list

if __name__ == "__main__":
    N = int(input())
    print(*find_prime_numbers(N))
```

```java
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static List<Integer> findPrimeNumbers(int maxNum) {
        List<Integer> pnList = new ArrayList<Integer>(); // 要素数 0 の配列
        int i;
        int j;
        boolean divideFlag;

        for (i = 2; i <= /* 空欄 a */; i++) {
            divideFlag = true;

            /* i の正の平方根の整数部分が 2 未満のときは、繰返し処理を実行しない */
            for (j = 2; j <= (int)Math.sqrt(i); j++) { // α
                if (/* 空欄 b */) {
                    divideFlag = false;
                    break; // α の行から始まる繰返し処理を終了する
                }
            }
            if (divideFlag == true) {
                pnList.add(i);
            }
        }
        return pnList;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        List<Integer> pnList = findPrimeNumbers(N);

        for (int pn: pnList) {
            System.out.print(pn);
            System.out.print(" ");
        }
        System.out.println();
    }
}
```

```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> find_prime_numbers(int max_num) {
    vector<int> pn_list; // 要素数 0 の配列
    int i, j;
    bool divide_flag;

    for (i = 2; i <= /* 空欄 a */; i++) {
        divide_flag = true;

        /* i の正の平方根の整数部分が 2 未満のときは、繰返し処理を実行しない */
        for (j = 2; j < (int)sqrt(i); j++) { // α
            if (/* 空欄 b */) {
                divide_flag = false;
                break; // α の行から始まる繰返し処理を終了する
            }
        }
        if (divide_flag == true) {
            pn_list.push_back(i);
        }
    }
    return pn_list;
}

int main() {
    int N;
    cin >> N;
    
    vector<int> pn_list = find_prime_numbers(N);
    
    for (int pn: pnList) {
        cout << pn << " ";
    }
    cout << endl;
}
```

<div>
</details>

出典：令和5年度 基本情報技術者試験 科目B 公開問題 問1

## 制約
- $2 \leqq N \leqq 1000$
- $N$ は整数

## 入力
入力は以下の形式で標準入力から与えられます。

$N$

## 出力
$N$ 以下の素数すべてを昇順に出力してください。

## サンプル 1
### 入力例 1
```
5
```

### 出力例 1
```
2 3 5
```

$5$ 以下の素数は $2, 3, 5$ の $3$ つ存在します。

## サンプル 2
### 入力例 2
```
30
```

### 出力例 2
```
2 3 5 7 11 13 17 19 23 29
```
