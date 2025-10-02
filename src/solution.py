# -*- coding: utf-8 -*-
# GitHub Classroom: src/solution.py

import re

# 以下の関数は、入力がカンマで区切られた数字のリスト形式であるかどうかを判定する
def is_comma_separated_numbers(s):
    pattern = r'___'  # (1) 入力がカンマで区切られた数字のリストを表す正規表現を記述せよ
    match = re.fullmatch(pattern, s)
    return match is not None

# 以下の関数は、入力がカンマで区切られた数字のリスト形式であるかどうかを判定する
def is_comma_separated_numbers(s):
    pattern = r'___'  # (1) 入力がカンマで区切られた数字のリストを表す正規表現を記述せよ
    match = re.fullmatch(pattern, s)
    return match is not None


def main():
    try:
        s = input()
    except EOFError:
        s = ""
    print(is_comma_separated_numbers(s))


if __name__ == "__main__":
    # サンプルケース（CSVの先頭3件）で自己テストを行う。
    # 標準入出力を一時的に差し替えて main() を実行し、期待出力と一致するか検証する。
    import io, sys

    def _run_once(inp: str) -> str:
        _stdin, _stdout = sys.stdin, sys.stdout
        try:
            sys.stdin = io.StringIO(inp)
            sys.stdout = io.StringIO()
            main()
            return sys.stdout.getvalue().strip()
        finally:
            sys.stdin, sys.stdout = _stdin, _stdout

    samples = [
        ("""1,2,3,4,5""", """True"""),
        ("""1,2,3,a,5""", """False"""),
        ("""1  , 2,   3""", """False""")
    ]

    all_ok = True
    for idx, (inp, expected) in enumerate(samples, 1):
        out = _run_once(inp)
        ok = (out.strip() == expected.strip())
        print(f"[sample {idx}] {'OK' if ok else 'NG'}")
        if not ok:
            print("----- input -----")
            print(inp)
            print("----- expected -----")
            print(expected)
            print("----- got -----")
            print(out)
            all_ok = False
    if all_ok:
        print("All sample tests passed.")
    else:
        print("Some sample tests failed.")
