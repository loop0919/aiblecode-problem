#!/bin/bash

function usage {
  cat <<EOM
$(basename ${0}) は、テストケースの入力を、codes/generate.py から生成するスクリプトです。
Usage: $(basename "$0") [OPTION]...
  -h, --help  ヘルプを表示

  $(basename "$0") [category_id] [problem_id] [name_prefix] [count]
    category_id: カテゴリのパス名
    probleme_id: 問題のパス名
    name_prefix: テストケース名の接頭辞
    count: 作成するテストケースの数
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

if [ $# -ne 4 ]; then
    usage
fi


dir=$(cd $(dirname $0); pwd)/problem
folder="${dir}/$1/$2"
name_prefix=$3
count=$4

for i in `seq 1 ${count}`
do
    if test ${i} -lt 10 ; then
        file="${name_prefix}0${i}"
    else
        file="${name_prefix}${i}"
    fi

    echo ${i} | python3 ${folder}/codes/generate.py ${i} > ${folder}/testcases/in/${file}.txt

done
