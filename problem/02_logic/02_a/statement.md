# 問題文
英大小文字からなる文字列 $S$ が与えられます。  
<code>I</code> (大文字のアイ) と <code>l</code> (小文字のエル) が両方とも含まれている文字列のことを **紛らわしい文字列** と呼びます。

$S$ が紛らわしい文字列であるか判定してください。

## 制約
- $S$ は英大小文字からなる文字列
- $1 \leqq |S| \leqq 2 \times 10^5$ （$|S|$ は $S$ の文字数）

## 入力
入力は以下の形式で標準入力から与えられます。

$S$

<details>
<summary>入力のサンプルコード</summary>
<div>
与えられる入力を受け取るコードの一例です。

```py
S = input()
# ここからコードを入力してください。

```

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String S = sc.next();

        /* ここからコードを入力してください。 */
    }
}
```

```cpp
#include <bits/stdc++.h>

using namespace std;

int main() {
    string S;
    cin >> S;

    /* ここからコードを入力してください。 */
}
```
</div>
</details>


## 出力
$S$ が紛らわしい文字列ならば <code>Yes</code> 、そうでなければ <code>No</code> を標準出力から出力してください。

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
AIbleCode
```

### 出力例 1
```
Yes
```

<code>AIbleCode</code> には <code>I</code> と <code>l</code> が両方とも含まれています。これは紛らわしい文字列です。

## サンプル 2
### 入力例 2
```
TechnologyEngineer
```

### 出力例 2
```
No
```

<code>i</code> (小文字のアイ) と <code>I</code> (大文字のアイ) は別物であることに気を付けてください。  
この文字列は紛らわしい文字列ではないです。
