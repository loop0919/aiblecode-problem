# 問題文
数字、文字 <code>x</code> 、括弧 <code>(</code>, <code>)</code> 、記号 <code>|</code>, <code>^</code>, <code>&</code>, <code>=</code> からなる $x$ についての方程式が文字列 $S$ として与えられます。

ここで**方程式**は、以下の BNF によって定義される <code>\<Equation\></code> です。

```
<Equation> ::= <Expression> "=" <Number>
<Expression> ::= <OrTerm>

<OrTerm> ::= <XorTerm> | <OrTerm> "|" <XorTerm>
<XorTerm> ::= <AndTerm> | <XorTerm> "^" <AndTerm> 
<AndTerm> ::= <Value> | <AndTerm> "&" <Value>

<Value> ::= <Number> | "x" | "(" <Expression> ")"
<Number> ::= 0 以上 2の30乗 未満の整数
```

文字と記号はそれぞれ以下のように説明されます。

- <code>x</code> : 変数 $x$ 。ただし、$x$ は $0$ 以上の整数である。
- <code>|</code> : ビットごとの論理和 $\mathrm{or}$ 。
- <code>^</code> : ビットごとの排他的論理和 $\mathrm{xor}$ 。ただし、$\mathrm{or}$ よりも先に計算される。
- <code>&</code> : ビットごとの論理積 $\mathrm{and}$ 。ただし、$\mathrm{or}, ~\mathrm{xor}$ よりも先に計算される。
- <code>=</code> : 等号 $=$ 。

$x$ についての方程式の解の**最小値**を求めてください。ただし、解が存在しない場合、<code>-1</code> を出力してください。

**$T$ 個のテストケースが与えられるので、それぞれについて答えてください。**

<details>
<summary>ビットごとの論理和とは</summary>
<div>

$0$ 以上の整数 $a, b$ について、ビットごとの論理和 $a ~ \mathrm{or} ~ b$ は以下のように定義されます。

- $a ~\mathrm{or}~ b$ を $2$ 進数表記にしたときの $2^i$ の位 $(i = 0, 1, 2, \cdots)$ は、
  - $a, b$ を $2$ 進数表記したときの $2^i$ の位の少なくとも一方が $1$ のとき $1$ 。
  - そうでないとき $0$ 。

例えば、$9, 3$ を $2$ 進数表記にすると <code>1001</code>, <code>0011</code> となるので、$9 ~ \mathrm{or} ~ 3 = 11$ となります。（ $11$ を $2$ 進数表記にすると <code>1011</code> となります。）

</div>
</details>

<details>
<summary>ビットごとの排他的論理和とは</summary>
<div>

$0$ 以上の整数 $a, b$ について、ビットごとの論理和 $a ~ \mathrm{xor} ~ b$ は以下のように定義されます。

- $a ~\mathrm{xor}~ b$ を $2$ 進数表記にしたときの $2^i$ の位 $(i = 0, 1, 2, \cdots)$ は、
  - $a, b$ を $2$ 進数表記したときの $2^i$ の位の一方が $1$ 、他方が $0$ のとき $1$ 。
  - そうでないとき $0$ 。

例えば、$9, 3$ を $2$ 進数表記にすると <code>1001</code>, <code>0011</code> となるので、$9 ~ \mathrm{xor} ~ 3 = 10$ となります。（ $10$ を $2$ 進数表記にすると <code>1010</code> となります。）

</div>
</details>

<details>
<summary>ビットごとの論理積とは</summary>
<div>

$0$ 以上の整数 $a, b$ について、ビットごとの論理積 $a ~ \mathrm{and} ~ b$ は以下のように定義されます。

- $a ~\mathrm{and}~ b$ を $2$ 進数表記にしたときの $2^i$ の位 $(i = 0, 1, 2, \cdots)$ は、
  - $a, b$ を $2$ 進数表記したときの $2^i$ の位の両方が $1$ のとき $1$ 。
  - そうでないとき $0$ 。

例えば、$9, 3$ を $2$ 進数表記にすると <code>1001</code>, <code>0011</code> となるので、$9 ~ \mathrm{and} ~ 3 = 1$ となります。（ $1$ を $2$ 進数表記にすると <code>0001</code> となります。）

</div>
</details>
<details>
<summary>入力される方程式の例</summary>
<div>

例えば、以下の例は <code>\<Equation\></code> になり得ます。
- <code>4|1^3&x=7</code> ： $4 ~ \mathrm{or} ~ 1 ~ \mathrm{xor} ~ 3 ~ \mathrm{and} ~ x = 7$ , 計算順序は $4 ~\mathrm{or}~ (3 ~ \mathrm{xor} ~ (1 ~\mathrm{and}~ x))$ であることに注意。

- <code>(x|1)&((3^x)&15)=1073741823</code> ： $(x ~\mathrm{or}~ 1) ~\mathrm{and}~ ((3 ~\mathrm{xor}~ x) ~\mathrm{and}~ 15) = 1073741823$

- <code>(((x)))=314</code> ： $(((x))) = 314$

- <code>1=2</code> ： $1 = 2$

ただし、以下の例は <code>\<Equation\></code> になり得ません。
- <code>x=-1</code>
- <code>x=9999999999</code>
- <code>2x=4</code>
- <code>123=x</code>
- <code>x=3=3</code>

</div>
</details>

## 制約
- $T$ は $1 \leqq T \leqq 100$ を満たす整数
- $S$ は問題文中の BNF で定義された <code>\<Equation\></code> である
- $1 \leqq |S| \leqq 2000$ （ $|S|$ は $S$ の文字数）

## 入力
入力は以下の形式で標準入力から与えられます。ここで、$\mathrm{case}_i$ は $i$ 番目のテストケースです。

$T$  
$\mathrm{case}_1$  
$\mathrm{case}_2$  
$\vdots$  
$\mathrm{case}_T$

各テストケースは以下の形式で与えられます。

$S$

## 出力
$T$ 行出力し、$i$ 行目には $i$ 番目のテストケースについての答えを出力してください。

各テストケースについて、$x$ についての方程式の解の最小値を出力してください。ただし、解が存在しない場合、<code>-1</code> を出力してください。

## サンプル 1
### 入力例 1
```
5
4|1^3&x=7
4&(3|x)=6
x^x|x&x=100
1=2
x|(x&(x|(x^1234)^5678)|9012)=13301
```

### 出力例 1
```
2
-1
100
-1
4289
```

この入力では $5$ 個のテストケースが与えられています。$1, 2, 3, 4$ 番目のテストケースについて、以下のことが言えます。

- $4 ~\mathrm{or}~ 1 ~ \mathrm{xor} ~ 3 ~ \mathrm{and} ~ x = 7$ の解のうち最小のものは $x = 2$ です。

- $4 ~\mathrm{and}~ (3 ~\mathrm{or}~ x) = 6$ を満たす $x$ は存在しません。この場合、<code>-1</code> を出力してください。

- $x ~ \mathrm{xor} ~ x ~\mathrm{or}~ x ~\mathrm{and}~ x = 100$ の解は $x = 100$ です。方程式の中に $x$ が複数個含まれている場合もあります。

- $1 = 2$ を満たす $x$ は存在しません。方程式の中に $x$ が含まれない場合もあります。
