# 問題文
<strong>
本問題は フィボナッチ数列（★3 Edition） の強化版です。<br/>  
フィボナッチ数列（★3 Edition） との相違点は <font color="yellow">黄色</font> で記述しています。
</strong>

<br/>

正整数 $N, M$ と長さ $N$ の数列 $A = (A_1, A_2, \cdots, A_N)$ が与えられます。  

数列 $X$ を以下のように定義します。

- $1 \leqq i \leqq N$ ならば、 $X_i = A_i$
- $i \geqq N + 1$ ならば、 $\displaystyle X_i = X_{i - 1} + X_{i - 2} + \cdots + X_{i - N}$

$X_{M}$ を求めてください。<font color="yellow">答えが非常に大きくなる場合があるため、素数</font> $\color{yellow} 10^9 + 7$ <font color="yellow">で割った余りを出力してください。</font>

**$T$ 個のテストケースが与えられるので、それぞれについて答えてください。**

## 制約
- $1 \leqq T \leqq 100$
- $\color{yellow} 1 \leqq N \leqq 10$
- $1 \leqq M \leqq \color{yellow} 10^{18}$
- $0 \leqq A_i \leqq \color{yellow}  10^9 + 6$
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

## 出力
標準出力に $T$ 行出力してください。$i$ 行目 $(i = 1, 2, \cdots, T)$ には $i$ 番目のテストケースについての答えを出力してください。

各テストケースについて、$\color{yellow} X_M$ <font color="yellow">を素数</font> $\color{yellow} 10^9 + 7$ <font color="yellow">で割った余り</font>を出力してください。

## サンプル
### 入力例
```
4
2 7
1 1
1 99999
0
9 10000000007
9 9 8 2 4 4 3 5 3
10 1000000000000000000
1 2 4 8 16 32 64 128 256 512
```

### 出力例
```
13
0
104102534
502299872
```

この入力では、$4$ 個のテストケースが与えられています。$1, 2, 3$ 番目のテストケースについて、以下のことが言えます。

- $1$ 番目のテストケースについて、数列 $X = (1, 1, 2, 3, 5, 8, 13, \cdots)$ です。これの $7$ 項目は $13$ です。

- $2$ 番目のテストケースについて、数列 $X$ の各要素はすべて $0$ です。

- $3$ 番目のテストケースについて、$10^9 + 7$ で割った余りを求めることと、計算過程で $32$-bit 整数型の範囲を超える可能性があることに注意してください。
