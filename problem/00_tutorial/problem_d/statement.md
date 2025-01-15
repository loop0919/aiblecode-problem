# 問題文
$N$ 個の商品が棚に横 $1$ 列に並んでいます。  
左から $i$ 番目 $(i = 1, 2, \cdots, N)$ にある商品の在庫数は $A_i$ です。

また、ロボットがあります。はじめ、ロボットは左から $1$ 番目にある商品の目の前に立っています。

ロボットに対してこれから $Q$ 個の指示が与えられます。  
$k$ 番目 $(k = 1, 2, \cdots, Q)$ の指示は文字列 $S_k$ で表され、それぞれの意味は以下の通りです。  
<br>
- $S_k =$ <code>left</code> ： ロボットを、現在いる場所から $1$ 個**左**にある商品の目の前に移動する。
- $S_k =$ <code>right</code> ： ロボットを、現在いる場所から $1$ 個**右**にある商品の目の前に移動する。
- $S_k =$ <code>answer</code> ： 現在ロボットの目の前にある、商品の在庫数を出力する。

<br>
ただし、移動しようとした場所に商品がない場合、何も行わないこととします。

各指示について、$k = 1, 2, \cdots, Q$ の順に処理してください。

## 制約
- $N, Q, A_i$ は整数
- $1 \leqq N \leqq 100$
- $1 \leqq Q \leqq 10000$
- $0 \leqq A_i \leqq 10^9$
- $S_k$ は <code>left</code> , <code>right</code> , <code>answer</code> のいずれかの文字列


 ## 入力
入力は以下の形式で標準入力から与えられます。

$N$&emsp;$Q$  
$A_1$&emsp;$A_2$&emsp;$\ldots$&emsp;$A_N$  
$S_1$  
$S_2$  
$\vdots$  
$S_Q$  

<details>
<summary>入力のサンプルコード</summary>
<div>
与えられる入力を受け取るコードの一例です。

```py
N, Q = map(int, input().split())
A = list(map(int, input().split()))
for i in range(Q):
    S = input() # S_1, S_2, ... がそれぞれ入力されます。

    # ここからコードを入力してください。

```

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int Q = sc.nextInt();

        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }

        for (int k = 0; k < Q; k++) {
            String S = sc.next(); // S_1, S_2, ... がそれぞれ入力されます。
            
            /* # ここからコードを入力してください。 */
        }
    }
}

```
</div>
</details>

 ## 出力
$S_k =$ <code>answer</code> の指示の個数を $q$ 個として、標準出力から $q$ 行出力してください。  
問題文の指示に従い、$S_k =$ <code>answer</code> のクエリについての答えを順番に改行区切りで出力してください。

<details>
<summary>出力のサンプルコード</summary>
<div>
整数 <code>100</code> を出力するコードの一例です。

```py
print(100)

```

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println(100);
    }
}

```
</div>
</details>


## サンプル 1
### 入力例 1
```
5 6
3 1 4 1 5
answer
right
answer
left
left
answer
```

### 出力例 1
```
3
1
3
```

各指示を以下の流れで処理すれば良いです。

- 現在ロボットは左から $1$ 番目のロボットの前にいる。その商品の在庫数 $3$ を出力する。
- $1$ 個右にある商品の目の前に移動する。
- 現在ロボットは左から $2$ 番目のロボットの前にいる。その商品の在庫数 $1$ を出力する。
- $1$ 個左にある商品の目の前に移動する。
- 左にある商品がないため、何も行わない。
- 現在ロボットは左から $1$ 番目のロボットの前にいる。その商品の在庫数 $3$ を出力する。

## サンプル 2
### 入力例 2
```
6 14
2 3 5 7 11 13
left
right
right
right
answer
left
answer
answer
right
right
right
right
right
answer
```

### 出力例 2
```
7
5
5
13
```
