def fibonacci(n: int) -> int:
    """
    n番目のフィボナッチ数を返す関数を実装せよ。

    F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2) (n>=2)
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    