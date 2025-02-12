# 問題文
コサイン類似度は、$2$ つのベクトルの向きの類似性を測る尺度です。

中島くんは、$2$ つの配列を受け取り、それらのコサイン類似度を返す関数を作成している途中です。

ここで、$\bm{v_1} = (a_1, a_2, \cdots, a_n), ~ \bm{v_2} = (b_1, b_2, \cdots, b_n)$ であったとき、$\bm{v_1}, \bm{v_2}$ のコサイン類似度は以下の式で計算することができます。

$$
\frac{a_1 b_1 + a_2 b_2 + \cdots + a_n b_n}{\sqrt{{a_1}^2 + {a_2}^2 + \cdots + {a_n}^2} \sqrt{{b_1}^2 + {b_2}^2 + \cdots + {b_n}^2}}
$$

$2$ つの $N$ 次元ベクトル $A = (A_1, A_2, \cdots, A_N), ~ B = (B_1, B_2, \cdots, B_N)$ のコサイン類似度を求めてください。

ここで、以下のコードテンプレートを利用しても構いません。

<details>
<summary>コードテンプレート</summary>
<div>

コードテンプレートは以下の通りです。「空欄 a」と「空欄 b」を埋めてください。

```py
import math

def calc_cosine_similarity(vector1, vector2):
    temp = 0
    numerator = 0

    for i in range(len(vector1)):
        numerator = numerator + '''空欄 a'''
    
    for i in range(len(vector1)):
        temp = temp + vector1[i]**2
    denominator = math.sqrt(temp)

    temp = 0
    for i in range(len(vector2)):
        temp = temp + vector2[i]**2
    denominator = '''空欄 b'''

    similarity = numerator / denominator
    return similarity


if __name__ == "__main__":
    N = int(input())
    A = list(map(float, input().split()))
    B = list(map(float, input().split()))
    print(calc_cosine_similarity(A, B))
```

```java
import java.util.Scanner;

public class Main {
    public static double calcCosineSimilarity(double[] vector1, double[] vector2) {
        double similarity;
        double numerator;
        double denominator;
        double temp = 0;
        int i;
        numerator = 0;

        for (i = 0; i < vector1.length; i++) {
            numerator = numerator + /* 空欄 a */;
        }

        for (i = 0; i < vector1.length; i++) {
            temp = temp + (vector1[i] * vector1[i]);
        }
        denominator = Math.sqrt(temp);

        temp = 0;
        for (i = 0; i < vector2.length; i++) {
            temp = temp + (vector2[i] * vector2[i]);
        }
        denominator = /* 空欄 b */;

        similarity = numerator / denominator;
        return similarity;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        double[] A = new double[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextDouble();
        }

        double[] B = new double[N];
        for (int i = 0; i < N; i++) {
            B[i] = sc.nextDouble();
        }

        double similarity = calcCosineSimilarity(A, B);
        System.out.println(similarity);
    }
}
```

```cpp
#include <bits/stdc++.h>
using namespace std;

double calc_cosine_similarity(vector<double> vector1, vector<double> vector2) {
    double similarity, numerator, denominator, temp;
    temp = 0;
    int i;
    numerator = 0;

    for (i = 0; i < vector1.size(); i++) {
        numerator = numerator + /* 空欄 a */;
    }

    for (i = 0; i < vector1.size(); i++) {
        temp = temp + (vector1[i] * vector1[i]);
    }
    denominator = sqrt(temp);

    temp = 0;
    for (i = 0; i < vector2.size(); i++) {
        temp = temp + (vector2[i] * vector2[i]);
    }
    denominator = /* 空欄 b */;

    similarity = numerator / denominator;
    return similarity;
}

int main() {
    int N;
    cin >> N;
    
    vector<double> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    vector<double> B(N);
    for (int i = 0; i < N; i++) {
        cin >> B[i];
    }

    double similarity = calc_cosine_similarity(A, B);
    cout << similarity << endl;
}
```

<div>
</details>

出典：令和5年度 基本情報技術者試験 科目B 公開問題 問5

## 制約
- $N$ は整数
- $1 \leqq N \leqq 100$
- $A_i, B_i$ は小数で、小数第 $2$ 位まで与えられる。
- $-100.00 \leqq A_i \leqq 100.00$
- $-100.00 \leqq B_i \leqq 100.00$
- $A_1, A_2, \cdots, A_N$ のうち少なくとも $1$ つは $0.00$ でない
- $B_1, B_2, \cdots, B_N$ のうち少なくとも $1$ つは $0.00$ でない

## 入力
入力は以下の形式で標準入力から与えられます。

$N$  
$A_1$&emsp;$A_2$&emsp;$\ldots$&emsp;$A_N$  
$B_1$&emsp;$B_2$&emsp;$\ldots$&emsp;$B_N$  

## 出力
$A, B$ のコサイン類似度を標準出力に出力してください。

ただし、真の値との相対誤差または絶対誤差が $0.001$ 以下であったとき、正解と判定されます。

## サンプル 1
### 入力例 1
```
2
1.00 3.14
-2.71 0.00
```

### 出力例 1
```
-0.30345415304293577
```

$A = (1.00, 3.14), ~ B = (-2.71, 0.00)$ です。  
これらのコサイン類似度を計算すると、$-0.3034\cdots$ となります。

`-0.3034` などでも、真の値との誤差が十分誤差が小さいため正解と判定されます。

## サンプル 2
### 入力例 2
```
1
0.01
100.00
```

### 出力例 2
```
1.0
```

## サンプル 3
### 入力例 3
```
5
-6.65 74.46 -2.11 -16.56 96.90
-4.60 -37.51 63.44 56.04 98.63
```

### 出力例 3
```
0.34290259795407035
```
