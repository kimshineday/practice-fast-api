import string
from typing import Final


class Base62:  # final:재할당을 막아준다.
    BASE: Final[str] = string.ascii_letters + string.digits
    BASE_LEN: Final[int] = len(BASE)

    @classmethod
    def encode(cls, num: int) -> str:
        if num < 0:
            raise ValueError(f"{cls}.encode() needs positive integer but you passed: {num}")

        if num == 0:
            return cls.BASE[0]

        result = []
        # result = ""  # 문자열은 바꿀 수 없다.
        while num:
            num, remainder = divmod(num, cls.BASE_LEN)
            result.append(cls.BASE[remainder])
        return "".join(result)


print(Base62.encode(62))
# print(Base62.encode(124))
# print(Base62.BASE[2])
