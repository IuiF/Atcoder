#!/bin/bash

# 指定されたディレクトリを削除
rm -rf ~/.local/share/TabNine
rm -rf ~/.vscode-server/data/User/globalStorage/tabnine.tabnine-vscode/
rm -rf ~/.config/TabNine/

# 10秒待機
# sleep 10

# code ~/.config/TabNine/tabnine_config.json

# JSONファイルを更新
# sed -i 's/"inline_suggestions_mode": null/"inline_suggestions_mode": true/' ~/.config/TabNine/tabnine_config.json
