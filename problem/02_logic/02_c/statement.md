# 問題文
<strong>
本問題の強化版として 中島くんコントロール in 迷路 があります。<br/>  
中島くんコントロール in 迷路  との相違点は <font color="yellow">黄色</font> で記述しています。
</strong>

<br/>

縦 $H$ マス、横 $W$ マスのグリッドがあります。上から $i$ 番目、左から $j$ 番目のマスをマス $(i, j)$ といいます。

<font color="yellow"> <code>S</code> , <code>G</code> , <code>.</code> のいずれか</font>である文字 $C_{i, j}$ はマス $(i, j)$ の状態を表します。それぞれ以下のように説明されます。

- <code>S</code> : スタート地点となるマス
- <code>G</code> : ゴール地点となるマス
- <code>.</code> : 空きマス

はじめ、中島くんはスタート地点にいます。中島くんに対して、あなたが出力する文字列 $X$ の各文字で指示をすることができます。

中島くんは $i = 1, 2, \cdots, N$ の順に $X$ の $i$ 文字目で表される指示に従います。それぞれ以下のように説明されます。

- <code>^</code> : 上方向に $1$ マス移動する
- <code>v</code> : 下方向に $1$ マス移動する
- <code><</code> : 左方向に $1$ マス移動する
- <code>></code> : 右方向に $1$ マス移動する

ただし、グリッドの範囲外に移動することはできず、そうしようとした場合不正解と判定されます。

ゴール地点に到達させる指示となる文字列 $X$ のうち、**指示回数が最小となるもの**を $1$ つ提示してください。  
ここで、そのような指示が必ず存在することが制約により保証されます。

ただし、答えが複数ある場合、そのいずれを出力しても正解と判定されます。

## 制約
- $1 \leqq H \leqq 100$
- $1 \leqq W \leqq 100$
- $C_{i, j}$ は <font color="yellow"> <code>S</code> , <code>G</code> , <code>.</code> のいずれか</font>
- $C_{i, j} =$ <code>S</code> となる $(i, j)$ はちょうど $1$ つ
- $C_{i, j} =$ <code>G</code> となる $(i, j)$ はちょうど $1$ つ
- 答えとなる $X$ は必ず存在する。

## 入力
入力は以下の形式で標準入力から与えられます。

$H$&emsp;$W$  
$C_{1, 1}C_{1, 2}\ldots C_{1, W}$  
$C_{2, 1}C_{2, 2}\ldots C_{2, W}$  
$\vdots$  
$C_{H, 1}C_{H, 2}\ldots C_{H, W}$  

<details>
<summary>入力のサンプルコード</summary>
<div>
与えられる入力を受け取るコードの一例です。

```py
H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]

# ここからコードを入力してください。
```

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int H = sc.nextInt();
        int W = sc.nextInt();

        char[][] C = new char[H][W];
        for (int i = 0; i < H; i++) {
            String line = sc.next();
            
            for (int j = 0; j < W; j++) {
                C[i][j] = line.charAt(j);
            }
        }

        /* ここからコードを入力してください。 */
    }
}
```

```cpp
#include <bits/stdc++.h>

using namespace std;

int main() {
    int H, W;
    cin >> H >> W;

    vector<vector<char>> C(H, vector<char>(W));
    for (int i = 0; i < H; i++) {
        string line;
        cin >> line;

        for (int j = 0; j < W; j++) {
            C.at(i).at(j) = line.at(j);
        }
    }

    /* ここからコードを入力してください。 */
}
```
</div>
</details>

## 出力
中島くんに行う指示を表す文字列 $X$ を標準出力に出力してください。  
答えが複数ある場合、そのいずれを出力しても正解と判定されます。

<details>
<summary>出力のサンプルコード</summary>
<div>
文字列 <code>^v<></code> を出力するコードの一例です。

```py
print("^v<>")

```

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("^v<>");
    }
}

```

```cpp
#include <bits/stdc++.h>

using namespace std;

int main() {
    cout << "^v<>" << endl;
}
```
</div>
</details>

## サンプル 1
### 入力例 1
```
3 4
S...
....
...G
```

### 出力例 1
```
>>>vv
```

右に $3$ 回、下に $2$ 回移動することでゴール地点に到達することができます。

また、以下のように出力しても正解と判定されます。
```
>v>v>
```

## サンプル 2
### 入力例 2
```
1 2
GS
```

### 出力例 2
```
<
```

## サンプル 3
### 入力例 3
```
5 7
.......
..G....
.......
.......
....S..
```

### 出力例 3
```
^^^<<
```

