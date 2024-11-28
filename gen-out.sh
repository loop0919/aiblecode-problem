#!/bin/bash

function usage {
  cat <<EOM
$(basename ${0}) は、テストケースの想定される出力を、codes/solve.py から生成するスクリプトです。
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

dir=$(cd $(dirname $0); pwd)/problem
folder="${dir}/$1/$2"

for file in `ls ${folder}/testcases/in`
do
    cat ${folder}/testcases/in/${file} | python3 ${folder}/codes/solve.py > ${folder}/testcases/out/${file}
done
