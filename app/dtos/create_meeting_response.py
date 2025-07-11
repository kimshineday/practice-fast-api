from typing import Annotated

from pydantic import BaseModel, Field

from app.dtos.frozen_config import FROZEN_CONFIG


class CreateMeetingResponse(BaseModel):
    model_config = FROZEN_CONFIG  # 클래스 내부가 변경되지 않음

    url_code: Annotated[str, Field(description="미팅 url 코드. unique 합니다.")]  # 설명
    # 라이브러리에서 부차적으로 넣고 싶을때 사용. 원래 타입과 라이브러리에서 지정하는 것을 추가.
