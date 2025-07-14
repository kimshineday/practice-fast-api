import random
import timeit
import uuid
from datetime import datetime

# test
from base62 import Base62

# from typing import Sequence
from sqids import sqids  # 숫자가 너무 크면 안된다.

squid = sqids.Sqids()


class Squids:

    @classmethod
    def encode(cls, nums: list[int]) -> str:  # def encode(cls, nums: Sequence[int]) -> str:
        return squid.encode(nums)


print(Squids.encode([1, 2]))  # print(Squids.encode((1,2)))
# 값을 리스트 형태가 아닌 튜플의 형태로 바꿀 수 있음. mypy test에서 에러로 인식할 수 있음으로 리스트를 Sequence로 지정
# Sequence는 순서가 있는 자료형.

if __name__ == "__main__":
    now = datetime.now()
    print(
        Squids.encode(
            [now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond, random.randint(1, 9)]
        )  # 시간 겹침을 방지하기 위해 뒤에 랜덤 숫자를 포함.
    )


# ---
# timeit으로 시간 측정
def do_squids():
    now = datetime.now()
    print(
        Squids.encode(
            [now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond, random.randint(1, 9)]
        )  # 시간 겹침을 방지하기 위해 뒤에 랜덤 숫자를 포함.
    )


def do_base62():
    uu = uuid.uuid4()
    return Base62.encode(uu.int)


if __name__ == "__main__":
    print(do_squids())
    print(do_base62())
    print(timeit.timeit(lambda: do_squids(), number=100000))  # 7.489537165994989
    print(timeit.timeit(lambda: do_base62(), number=100000))  # 0.35218699999677483
