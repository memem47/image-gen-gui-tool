# GitHub 操作記録

✅ ステップ1: GitHubリポジトリの作成

1. GitHubにログイン → https://github.com/
2. ＋ ボタン → [New repository]
4. 下記を入力して [Create repository]
    - Repository name: image-gen-gui-tool
    - Description: A GUI tool for generating and saving test images with noise and warp support.
    - Publicにする
    - README をチェック入れる


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
