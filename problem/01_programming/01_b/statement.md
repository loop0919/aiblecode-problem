# 問題文
整数 $a, b$ が与えられます。  
短軸 $a$ 、長軸 $b$ の楕円の面積を小数で求めてください。

__ここで、楕円の面積は $\pi \times a \times b$ （$\pi$ は円周率 $3.141592\cdots$）で計算することができます。__

![楕円](data:image/png;base64,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)

## ヒント
ヒントを閲覧したいときは、以下をクリックしてください。
<details>
<summary>ヒント</summary>
<div>

円周率 $\pi$ を宣言するためには、数学ライブラリを利用すると良いです。  
円周率 $\pi$ を出力するサンプルコードは以下の通りです。

```py
import math

print(math.pi) # math.pi : 円周率π
```

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(Math.PI); // Math.PI : 円周率π
    }
}
```

```cpp
#include <bits/stdc++.h>

using namespace std;

int main() {
    cout << M_PI << endl; // M_PI : 円周率π
}
```

その後、$\pi$ と $a$ と $b$ を <code>*<code> 演算子でかけ算すると良いです。

<div>
</details>


## 制約
- $a, b$ は整数
- $1 \leqq a \leqq b \leqq 100$

## 入力
入力は以下の形式で標準入力から与えられます。

$a$&emsp;$b$

<details>
<summary>入力のサンプルコード</summary>
<div>
与えられる入力を受け取るコードの一例です。

```py
a, b = map(int, input().split())
# ここからコードを入力してください。

```

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();

        /* ここからコードを入力してください。 */
    }
}
```

```cpp
#include <bits/stdc++.h>

using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    /* ここからコードを入力してください。 */
}
```

</div>
</details>

## 出力
問題文中の楕円の面積を小数で標準出力に出力してください。  
ただし、真の値からの相対誤差または絶対誤差が $0.01$ 以下のとき、正解と判定されます。

<details>
<summary>出力のサンプルコード</summary>
<div>
小数 <code>3.14</code> を出力するコードの一例です。

```py
print(3.14)

```

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println(3.14);
    }
}

```

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    cout << 3.14 << endl;
}
```

</div>
</details>

## サンプル 1
### 入力例 1
```
2 3
```

### 出力例 1
```
18.84955592153876
```

短軸 $2$ 、長軸 $3$ の楕円の面積は、$2 \times 3 \times \pi = 18.84955\cdots$ です。

<code>18.84</code> や <code>18.849552000000003</code> などと出力しても、真の値との誤差が十分小さいため正解と判定されます。

## サンプル 2
### 入力例 2
```
100 100
```

### 出力例 2
```
31415.92653589793
```

