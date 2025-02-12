# 問題文
異なる $3$ つの整数 $x, y, z$ が与えられます。
$x, y, z$ の中で最大の値を出力してください。

ここで、以下のコードテンプレートを利用しても構いません。

<details>
<summary>コードテンプレート</summary>
<div>

コードテンプレートは以下の通りです。「空欄」を埋めてください。

```py
def maximum(x, y, z):
    if '''空欄''':
        return x
    elif y > z:
        return y
    else:
        return z

if __name__ == "__main__":
    x, y, z = map(int, input().split())
    max_value = maximum(x, y, z)
    print(max_value)
```

```java
import java.util.Scanner;

public class Main {
    public static int maximum(int x, int y, int z) {
        if (/* 空欄 */) {
            return x;
        } else if (y > z) {
            return y;
        } else {
            return z;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        int z = sc.nextInt();

        int maxValue = maximum(x, y, z);
        System.out.println(maxValue);
    }
}
```

```cpp
#include <bits/stdc++.h>
using namespace std;

int maximum(int x, int y, int z) {
    if (/* 空欄 */) {
        return x;
    } else if (y > z) {
        return y;
    } else {
        return z;
    }
}

int main() {
    int x, y, z;
    cin >> x >> y >> z;
    
    int max_value = maximum(x, y, z);
    cout << max_value << endl;
}
```

<div>
</details>

出典：令和6年度 基本情報技術者試験 科目B 公開問題 問1

## 制約
- $x, y, z$ は整数
- $1 \leqq x \leqq 10^9$
- $1 \leqq y \leqq 10^9$
- $1 \leqq z \leqq 10^9$
- $x, y, z$ は相異なる

## 入力
入力は以下の形式で標準入力から与えられます。

$x$&emsp;$y$&emsp;$z$

## 出力
$x, y, z$ の中で最大の値を標準出力に出力してください。

## サンプル 1
### 入力例 1
```
5 3 2
```

### 出力例 1
```
5
```

$5, 3, 2$ の中で最大の値は $3$ です。

## サンプル 2
### 入力例 2
```
3 1 4
```

### 出力例 2
```
4
```

## サンプル 3
### 入力例 3
```
123 456 78
```

### 出力例 3
```
456
```
