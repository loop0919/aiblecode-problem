# 問題文
<code>0</code>, <code>1</code> からなる文字列　$S$ が与えられます。  

$S$ を符号なし $2$ 進整数として解釈したとき、それを $10$ 進整数に変換したものを出力してください。

ここで、以下のコードテンプレートを利用しても構いません。

<details>
<summary>コードテンプレート</summary>
<div>

コードテンプレートは以下の通りです。「空欄」を埋めてください。

```py
def convDecimal(binary: str) -> int:
    result = 0
    length = len(binary)
    for i in range(length):
        result = """空欄"""
    return result

if __name__ == "__main__":
    S = input()
    number = convDecimal(S)
    print(number)
```

```java
import java.util.Scanner;

public class Main {
    public static int convDecimal(String binary) {
        int i;
        int length = binary.length();
        int result = 0;
        for (i = 0; i < length; i++) {
            result = /* 空欄 */;
        }
        return result
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int S = sc.next();

        int number = convDecimal(S);
        System.out.println(number);
    }
}
```

```cpp
#include <bits/stdc++.h>
using namespace std;

int convDecimal(string binary) {
    int i, length, result;
    result = 0;
    length = binary.size();
    for (i = 0; i < length; i++) {
        result = /* 空欄 */;
    }
    return result;
}

int main() {
    string S;
    cin >> S;

    int number = convDecimal(S);
    cout << number << endl;
}
```

<div>
</details>

出典：令和6年度 基本情報技術者試験 科目B 公開問題 問2

## 制約
- $S$ は <code>0</code>, <code>1</code> からなる文字列
- $1 \leqq |S| \leqq 30$ （$|S|$ は $S$ の文字数） 
- $S$ の $1$ 文字目は <code>1</code> である

## 入力
入力は以下の形式で標準入力から与えられます。

$S$

## 出力
$S$ を符号なし $2$ 進整数として解釈したとき、それを $10$ 進整数に変換したものを標準出力に出力してください。

## サンプル 1
### 入力例 1
```
10010
```

### 出力例 1
```
18
```

<code>10010</code> を符号なし $2$ 進数として解釈し、それを $10$ 進数に変換すると $18$ となります。

## サンプル 2
### 入力例 2
```
10101010101010101010
```

### 出力例 2
```
699050
```
