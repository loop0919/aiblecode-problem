# 問題文
八木山ベニーランドでは、年齢が $6$ 歳以上かつ身長が $120.0$ cm 以上の人のみが乗れるジェットコースターがあります。  

中島くんの年齢 $A$ 歳と身長 $H$ cm が与えられるので、中島くんがジェットコースターに乗れるか判定してください。

## 制約
- $A$ は整数
- $0 \leqq A \leqq 100$
- $H$ は小数であり、小数第 $1$ 位まで与えられる
- $100.0 \leqq H \leqq 200.0$

## 入力
入力は以下の形式で標準入力から与えられます。

$A$&emsp;$H$

<details>
<summary>入力のサンプルコード</summary>
<div>
与えられる入力を受け取るコードの一例です。

```py
A, H = input().split()
A = int(A)
H = float(H)
# ここからコードを入力してください。

```

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        float H = sc.nextFloat();

        /* ここからコードを入力してください。 */
    }
}
```

```cpp
#include <bits/stdc++.h>

using namespace std;

int main() {
    int A;
    float H;
    cin >> A >> H;

    /* ここからコードを入力してください。 */
}
```

</div>
</details>

## 出力
中島くんがジェットコースターに乗れるならば <code>Yes</code> 、乗れないならば <code>No</code> を標準出力から出力してください。

<details>
<summary>出力のサンプルコード</summary>
<div>
文字列 <code>Yes</code> を出力するコードの一例です。

```py
print("Yes")

```

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("Yes");
    }
}
```

```cpp
#include <bits/stdc++.h>

using namespace std;

int main() {
    cout << "Yes" << endl;
}
```
</div>
</details>

## サンプル 1
### 入力例 1
```
7 120.5
```

### 出力例 1
```
Yes
```

中島くんの年齢は $7$ 歳で身長は $120.5$ cm です。これはジェットコースターに乗れる条件を満たすため <code>Yes</code> と出力します。


## サンプル 2
### 入力例 2
```
5 130.0
```

### 出力例 2
```
No
```

身長は条件を満たしていますが、年齢は満たしていません。<code>No</code> と出力します。


## サンプル 3
### 入力例 3
```
0 100.0
```

### 出力例 3
```
No
```

## サンプル 4
### 入力例 4
```
23 177.1
```

### 出力例 4
```
Yes
```
