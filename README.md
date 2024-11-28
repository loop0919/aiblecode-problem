# AIbleCode-Problem

AIbleCodeの問題を管理するリポジトリです。

---

## 環境
以下の条件を満たす環境で動作するはずです。
- Bashシェルが使える（ubuntu-22.04、amazon linux 2023 で動作を確認済み）
- Python3 や pip が使える

---

## 使い方

### `make.sh`

問題の雛型を作ります。`problem` ディレクトリの下に下図のように生成されます。  
サイト上では、`/problem/[category_id]/[problem_id]` でアクセスできます。

```bash
$ ./make.sh [category_id] [problem_id]
```

- `category_id` : カテゴリのパス名
- `problem_id` : 問題のパス名

```
problem/
└── [category_id]/
    ├── metadata.yml # カテゴリのメタデータ
    └── [problem_id]/
        ├── codes/
        │   ├── generate.py # 入力ファイル生成コード
        │   └── solve.py # 出力ファイル生成コード
        ├── testcases/
        │   ├── in/
        │   └── out/
        ├── metadata.yml # 問題のメタデータ
        ├── statement.md # 問題文
        ├── educational.md # 解説
```

---

### `gen-in.sh`

`generate.py` からテストケースの入力ファイルを生成します。
テストケースは `in/[name_prefix]01.txt`, `in/[name_prefix]02.txt`, ... と生成されます。

```bash
$ ./make.sh [category_id] [problem_id] [name_prefix] [count]
```

- `category_id` : カテゴリのパス名
- `problem_id` : 問題のパス名
- `name_prefix` : テストケース名の接頭辞
- `count` : 生成するテストケースの個数

---

### `gen-out.sh`

`solve.py` からテストケースの出力ファイルを生成します。
テストケースは、`in/` 内のファイル名と同じものが `out/` 内に生成されます。

```bash
$ ./make.sh [category_id] [problem_id]
```

- `category_id` : カテゴリのパス名
- `problem_id` : 問題のパス名

---

### `migrate.py`

AIbleCodeサーバ上に問題をアップロードします。  
**（TODO: 全問題がアップロードされるので、問題を選んでアップできるように後でする。）**

1. `.env-dummy` を `.env` に変更し、以下の内容を記入する。

```.env
ADMIN_USERNAME="[管理者のユーザー名]"
ADMIN_PASSWORD="[管理者のパスワード]"
AIBLECODE_API_HOST="[APIのホストのURI]"
```

2. 以下のコマンドを実行する。

```bash
$ pip install -r requirements.txt
$ python3 migrate.py
```
