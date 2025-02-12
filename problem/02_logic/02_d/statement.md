# 問題文
<strong>
本問題の強化版として フィボナッチ数列（★4 Edition） があります。<br/>  
フィボナッチ数列（★4 Edition） との相違点は <font color="yellow">黄色</font> で記述しています。
</strong>

<br/>

<font color="yellow">本問題の</font> $\color{yellow} N$ <font color="yellow">の値は、</font> $\color{yellow} N = 2$ <font color="yellow">に固定されています。</font>

正整数 $N, M$ と、長さ $N$ の数列 $A = (A_1, A_2, \cdots, A_N)$ が与えられます。  

数列 $X$ を以下のように定義します。

- $1 \leqq i \leqq N$ ならば、 $X_i = A_i$
- $i \geqq N + 1$ ならば、 $\displaystyle X_i = X_{i - 1} + X_{i - 2} + \cdots + X_{i - N}$

$X_{M}$ を求めてください。<font color="yellow">制約により、答えが</font> $\color{yellow}2^{63}$ <font color="yellow">未満であることが保証されます。</font>

**$T$ 個のテストケースが与えられるので、それぞれについて答えてください。**

## 制約
- $1 \leqq T \leqq 100$
- $\color{yellow} N = 2$
- $1 \leqq M \leqq \color{yellow} 80$
- $0 \leqq A_i \leqq \color{yellow} 100$
- 入力はすべて整数

## 入力
入力は以下の形式で標準入力から与えられます。ここで、$\mathrm{case}_i ~ (i = 1, 2, \cdots, T)$ は $i$ 番目のテストケースです。

$T$  
$\mathrm{case}_1$  
$\mathrm{case}_2$  
$\vdots$  
$\mathrm{case}_T$

各テストケースは以下の形式で与えられます。

$N$&emsp;$M$  
$A_1$&emsp;$A_2$&emsp;$\ldots$&emsp;$A_N$

<details>
<summary>入力のサンプルコード</summary>
<div>
与えられる入力を受け取るコードの一例です。

```py
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # ここからコードを入力してください。
```

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        for (int i = 0; i < T; i++) {
            int N = sc.nextInt();
            int M = sc.nextInt();

            long[] A = new long[N];
            for (int k = 0; j < N; j++) {
                A[k] = sc.nextLong();
            }

            /* ここからコードを入力してください。 */
        }
    }
}
```

```cpp
#include <bits/stdc++.h>

using namespace std;

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int N, M;
        cin >> N >> M;

        vector<long long> A(N);
        for (int k = 0; k < N; k++) {
            cin >> A[k];
        }

        /* ここからコードを入力してください。 */
    }
}
```
</div>
</details>


## 出力
標準出力に $T$ 行出力してください。$i$ 行目 $(i = 1, 2, \cdots, T)$ には $i$ 番目のテストケースについての答えを出力してください。

各テストケースについて、$\color{yellow} X_M$ を出力してください。

<details>
<summary>出力のサンプルコード</summary>
<div>
整数 <code>10000000000</code> を出力するコードの一例です。

```py
print(10000000000)

```

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println(10000000000L);
    }
}

```

```cpp
#include <bits/stdc++.h>

using namespace std;

int main() {
    cout << 10000000000LL << endl;
}
```
</div>
</details>


## サンプル
### 入力例
```
4
2 7
1 1
2 1
0 0
2 15
2 3
2 80
100 100
```

### 出力例
```
13
0
1597
2341672834846768500
```

この入力では、$4$ 個のテストケースが与えられています。$1, 2, 4$ 番目のテストケースについて、以下のことが言えます。

- $1$ 番目のテストケースについて、 数列 $X$ は $(1, 1, 2, 3, 5, 8, 13, \cdots)$ です。 $7$ 項目は $1$ です。

- $2$ 番目のテストケースについて、 数列 $X$ の各要素はすべて $0$ です。

- $4$ 番目のテストケースについて、$32$-bit 整数型の範囲を超える可能性があることに注意してください。
