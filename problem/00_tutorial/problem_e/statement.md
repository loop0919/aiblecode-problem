# 問題文
高度ITエンジニア科の体験入学会では、チャットボットを作る体験をすることができます。  
簡易的に、挨拶をしてくれるチャットボットを書いてみましょう。

ユーザー名 $S$ が与えられます。<code>Welcome</code> 、スペース（<code> </code>）、ユーザー名、! マーク（<code>!</code>）をこの順に結合した文字列を出力してください。

## 制約
- $S$ は英大小文字からなる文字列
- $1 \leqq |S| \leqq 16$ （$|S|$ は $S$ の文字数）

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

        /* # ここからコードを入力してください。 */
    }
}

```
</div>
</details>

## 出力
<code>Welcome</code> 、スペース（<code> </code>）、ユーザー名、! マーク（<code>!</code>）をこの順に結合した文字列を出力してください。

<details>
<summary>出力のサンプルコード</summary>
<div>
文字列 <code>Hello World!</code> を出力するコードの一例です。

```py
print("Hello World!")

```

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}

```
</div>
</details>



## サンプル 1
### 入力例 1
```
Guest
```

### 出力例 1
```
Welcome Guest!
```

<code>Welcome</code> 、スペース（<code> </code>）、ユーザー名（<code>Guest</code>）、! マーク（<code>!</code>）をこの順に結合した文字列です。

## サンプル 2
### 入力例 2
```
aiblecode
```

### 出力例 2
```
Welcome aiblecode!
```
