from pydantic import ConfigDict

FROZEN_CONFIG = ConfigDict(frozen=True)
# FROZEN : 생성 이후에는 변경할 수 없는 객체 ex) tuple
