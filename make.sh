#!/bin/bash

function usage {
  cat <<EOM
$(basename ${0}) は、問題の雛型を生成するスクリプトです。
Usage: $(basename "$0") [OPTION]...
  -h, --help  ヘルプを表示

  $(basename "$0") [category_id] [problem_id]
    category_id: カテゴリのパス名
    problem_id: 問題のパス名
EOM

  exit 2
}

while getopts ":h" optKey; do
    case "$optKey" in
        '-h'|'--help'|* )
            usage
            ;;
    esac
done

if [ $# -ne 2 ]; then
    usage
fi

category=$1
problem=$2

dir=$(cd $(dirname $0); pwd)/problem

category_folder=${dir}/${category}
folder=${dir}/${category}/${problem}

mkdir -p ${folder}

if [ ! -e ${category_folder}/metadata.yml ]; then
  echo "category:"$'\n'"  title:"$'\n'"  description:" > ${category_folder}/metadata.yml
fi

if [ ! -e ${folder}/statement.md ]; then
  echo "## 問題文"$'\n'\
  "[ここに問題文を書く]"$'\n'$'\n'\
  "## 制約"$'\n'\
  "- [ここに制約を書く]"$'\n'$'\n'\
  "## 入力"$'\n'\
  "[ここに入力の説明を書く]"$'\n'$'\n'\
  "## 出力"$'\n' \
  "[ここに出力の説明を書く]"$'\n'$'\n'\
  "## サンプル"$'\n'\
  "### サンプル 1"$'\n'\
  "[ここにサンプルを書く]"\
  > ${folder}/statement.md
fi

if [ ! -e ${folder}/editorial.md ]; then
  echo "## 解説"$'\n'\
  "[ここに解説を書く]" > ${folder}/editorial.md
fi

if [ ! -e ${folder}/metadata.yml ]; then
  echo "problem:"$'\n'"  title: # タイトル"$'\n'"  level: # 難易度[1から5までの整数]"$'\n'"  time_limit: 2.0 # 制限時間[sec]"$'\n'"  memory_limit: 256 # 制限メモリ[MB]" \
> ${folder}/metadata.yml
fi

mkdir -p ${folder}/codes

if [ ! -e ${folder}/codes/generate.py ]; then
  echo "# テストケースの生成コードを書く" > ${folder}/codes/generate.py
fi

if [ ! -e ${folder}/codes/solve.py ]; then
  echo "# 解答コードを書く" > ${folder}/codes/solve.py
fi

mkdir -p ${folder}/testcases/in
mkdir -p ${folder}/testcases/out
