# -*- coding: utf-8 -*-
# GitHub Classroom: test_public.py
# こちらは公開テスト。CSVのサンプル以外のケースを実行する。

import io
import sys
import importlib
from pathlib import Path

# src/solution.py を優先して import
repo_root = Path(__file__).parent
src_dir = repo_root / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

solution = importlib.import_module("src.solution")


def run_test(input_data: str, expected_output: str, tag: str = ""):
    # 標準入出力を差し替え
    _stdin, _stdout = sys.stdin, sys.stdout
    try:
        sys.stdin = io.StringIO(input_data)
        sys.stdout = io.StringIO()
        solution.main()
        out = sys.stdout.getvalue().strip()
    finally:
        sys.stdin, sys.stdout = _stdin, _stdout
    assert out.strip() == expected_output.strip(), (
        f"\n[{tag}] Unexpected output\n"
        f"--- input ---\n{input_data}\n"
        f"--- expected ---\n{expected_output}\n"
        f"--- got ---\n{out}\n"
    )


def test_public_cases():
    cases = [
    ("""1""", """True""", """nan"""),
    ("""1,8,124,""", """False""", """nan"""),
    ("""a.out b.txt Python is a programming language""", """False""", """テストケース1"""),
    ("""1       ,       3     ,""", """False""", """テストケース2""")
    ]
    # cases の各要素は (input, output, name) のタプル
    for idx, (inp, expected, name) in enumerate(cases, 1):
        tag = name if name else f"case{idx}"
        run_test(inp, expected, tag)


if __name__ == "__main__":
    test_public_cases()
    print("All public tests passed.")
