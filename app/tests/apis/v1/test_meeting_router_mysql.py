import httpx
from starlette.status import HTTP_200_OK
from tortoise.contrib.test import TestCase, initializer, finalizer

from app import app
from app.configs.tortoise_config import TORTOISE_ORM
from app.tortoise_models.meeting import MeetingModel


class TestMeetingRouter(TestCase):
    async def test_api_create_meeting_mysql(self) -> None:
        # Given -> 생략, Meeting을 만들때 필요한 재료가 없다.
        # When
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app),  # FAST API 어플리케이션을 테스트.
            base_url="http://test",
        ) as client:
            response = await client.post(url="/v1/mysql/meetings")
        # Then : 테스트 결과 검증
        assert response.status_code == HTTP_200_OK  # 응답 값만 확인하는.
        url_code = response.json()["url_code"]
        assert (await MeetingModel.filter(url_code=url_code).exists()) is True
