# 問題文
プログラミング学習でよく練習問題として出題される **FizzBuzz 問題** を解いてみましょう。

整数 $N, A, B$ が与えられます。$i = 1, 2, \cdots, N$ の順に以下の指示に従い出力してください。

- $i$ が $A$ と $B$ の両方の倍数のとき、 <code>FizzBuzz</code> を出力する
- 上記を満たさず、$i$ が $A$ の倍数であるとき、 <code>Fizz</code> を出力する
- 上記を満たさず、$i$ が $B$ の倍数であるとき、 <code>Buzz</code> を出力する
- 上記のいずれも満たさないとき、 整数 $i$ を出力する

## 制約
- $N, A, B$ は整数
- $1 \leqq N \leqq 100$
- $1 \leqq A \leqq 100$
- $1 \leqq B \leqq 100$

## 入力
入力は以下の形式で標準入力から与えられます。

$N$&emsp;$A$&emsp;$B$

<details>
<summary>入力のサンプルコード</summary>
<div>
与えられる入力を受け取るコードの一例です。

```py
N, A, B = map(int, input().split())
# ここからコードを入力してください。

```

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int A = sc.nextInt();
        int B = sc.nextInt();

        /* ここからコードを入力してください。 */
    }
}
```

```cpp
#include <bits/stdc++.h>

using namespace std;

int main() {
    int N, A, B;
    cin >> N >> A >> B;

    /* ここからコードを入力してください。 */
}
```
</div>
</details>

## 出力
問題文の指示に従い、$N$ 行出力してください。  
$k$ 行目には $i = k$ のときの指示に従って出力してください。

<details>
<summary>出力のサンプルコード</summary>
<div>

以下のように出力するコードの一例です。

```
Fizz
Buzz
1
```

```py
print("Fizz")
print("Buzz")
print(1)

```

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("Fizz");
        System.out.println("Buzz");
        System.out.println(1);
    }
}
```

```cpp
#include <bits/stdc++.h>

using namespace std;

int main() {
    cout << "Fizz" << endl;
    cout << "Buzz" << endl;
    cout << 1 << endl;
}
```
</div>
</details>

## サンプル 1
### 入力例 1
```
10 2 3
```

### 出力例 1
```
1
Fizz
Buzz
Fizz
5
FizzBuzz
7
Fizz
Buzz
Fizz
```

例えば、$i = 4$ のとき、$4$ は $2$ の倍数ですが、$3$ の倍数ではありません。  
よって、$4$ 行目には <code>Fizz</code> を出力します。

## サンプル 2
### 入力例 2
```
6 2 2
```

### 出力例 2
```
1
FizzBuzz
3
FizzBuzz
5
FizzBuzz
```
