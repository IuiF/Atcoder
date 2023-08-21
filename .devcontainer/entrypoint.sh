#!/bin/sh

FLAG="/home/vscode/.acc-flag"

if [ ! -f $FLAG ]; then
    # 初回起動時のみに実行するコマンド
    acc config default-task-choice all

    # atcoder-cliの設定フォルダへ移動
    cd `acc config-dir`

    # Pythonディレクトリの作成と必要なファイルの設定
    mkdir python
    cd python
    touch template.json
    touch main.py
    echo '{
"task":{
    "program": ["main.py"],
    "submit": "main.py"
    }
}' > template.json

    # デフォルトのテンプレートをPythonに変更
    acc config default-template python

    # フラグファイルを作成して次回からこの処理をスキップする
    touch $FLAG
fi

# 通常の起動処理（例：サービスの起動など）
exec "$@"
