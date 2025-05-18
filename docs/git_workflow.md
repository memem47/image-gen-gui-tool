# GitHub 操作記録

✅ ステップ1: GitHubリポジトリの作成

1. GitHubにログイン → https://github.com/
2. ＋ ボタン → [New repository]
4. 下記を入力して [Create repository]
    - Repository name: image-gen-gui-tool
    - Description: A GUI tool for generating and saving test images with noise and warp support.
    - Publicにする
    - README をチェック入れる

✅ ステップ2: 開発用ローカル環境の準備

```bash
# Bashコマンド
# 任意のディレクトリで作業
git clone https://github.com/<your-username>/image-gen-gui-tool.git
cd image-gen-gui-tool
python -m venv venv

# Windows (Git Bash / WSL / Cygwin)
source venv/Scripts/activate

pip install --upgrade pip
pip install opencv-python pillow numpy
pip install pyinstaller  # EXE化用
```

✅ ステップ3: 最小限のGUIベース作成（画像表示＋ランダム生成）

main.py

✅ ステップ4: .gitignoreとREADME.mdを追加

.gitignore
README.md

✅ ステップ5: Git 操作手順（手順自体もドキュメント化）
Git 操作の記録もドキュメントに追加する方法（docs/git_workflow.mdなど）

