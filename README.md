# レポート課題2-2

### 問題：Pythonの正規表現①
***
is_comma_separated_numbersという関数が、1つ以上の数字がカンマで区切られた形式の文字列かどうかを判定するように、空欄(_____)を埋めよ。
Pythonの正規表現の使い方については、Python関連の本やWebで検索して自分調べること。
注：数字とカンマが空白無しに連続していることが求められる。

## 提出方法
1. `src/solution.py` にコードを記述する
2. `pytest` をローカルで実行し、すべてのテストが通ることを確認する
3. GitHub に push すると、自動採点が行われる

### ローカル実行（Anaconda/Miniconda 前提）
以下では Windows の Anaconda Powershell Prompt を想定する。
```powershell
# 仮想環境の作成（初回のみ）
conda create -n comp311 python=3.11 -y
# 環境を有効化
conda activate comp311
# 依存パッケージのインストール
pip install -r requirements.txt
# テストの実行
pytest -q
```