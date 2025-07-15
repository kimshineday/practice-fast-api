from __future__ import annotations

from tortoise import Model, fields

from app.tortoise_models.base_model import BaseModel


class MeetingModel(BaseModel, Model):  # 다중상속, 파이썬은 다중상속이 허용되는 언어.
    url_code = fields.CharField(max_length=255, unique=True)  # url을 Where로 걸고 사용하는 경우가 많음.

    class Meta:
        table = "meetings"  # 테이블 이름 명시

    @classmethod
    async def create_meeting(cls, url_code: str) -> MeetingModel:  # 미팅 모델이 정의를 내리는 중.
        # 타입만 필요하기에 annotations 를 import.
        return await cls.create(url_code=url_code)
