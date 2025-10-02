# 小テスト1-1

## 演習問題
関数 `fibonacci(n: int) -> int` を定義せよ。  
この関数は、n 番目のフィボナッチ数を返すものとする。

- 定義: F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2) for n>=2
- n は 0 以上の整数とする

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