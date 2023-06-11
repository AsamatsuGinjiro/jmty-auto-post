import random
import string


def randomname(n):
    """
    n文字のランダムな文字列を生成する関数
    """
    randlst = [random.choice(string.ascii_letters + string.digits)
               for _ in range(n)]
    return ''.join(randlst)
