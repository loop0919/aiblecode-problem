# 問題文
AIbleCode にはランキングがあり、問題を正解することで取得できるスコアによって順位が決まります。

中島くんは、★の数が $N$ 個の問題に正解しました。  
以下の式で計算される、中島くんが取得したスコアを求めてください。

<br/>

- $10 \times N$

## 制約
- $N$ は整数
- $1 \leqq N \leqq 5$

## 入力
入力は以下の形式で標準入力から与えられます。

$N$

<details>
<summary>入力のサンプルコード</summary>
<div>
与えられる入力を受け取るコードの一例です。

```py
N = int(input())
# ここからコードを入力してください。

```

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        /* ここからコードを入力してください。 */
    }
}
```

```cpp
#include <bits/stdc++.h>

using namespace std;

int main() {
    int N;
    cin >> N;

    /* ここからコードを入力してください。 */
}
```

</div>
</details>

## 出力
中島くんが取得したスコアを求めてください。

<details>
<summary>出力のサンプルコード</summary>
<div>
整数 <code>10</code> を出力するコードの一例です。

```py
print(10)

```

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println(10);
    }
}

```

```cpp
#include <bits/stdc++.h>

using namespace std;

int main() {
    cout << 10 << endl;
}
```
</div>
</details>


## サンプル 1
### 入力例 1
```
1
```

### 出力例 1
```
10
```

★の数が $1$ 個の問題に正解することで、スコア $10$ 点を取得することができます。

## サンプル 2
### 入力例 2
```
3
```

### 出力例 2
```
30
```