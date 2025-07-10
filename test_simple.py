# # datetime
# # 택배가 언제 도착할지. eta.
# # 2영업일 이후 도착, 월-토 영업 / 산간지역 및 공휴일 고려하지 않음.
# # 공휴일 고려 시 공공데이터 공휴일 open api 사용해서 적용 시킬 수 있음.
# from datetime import datetime, timedelta
#
# # literal 사용 하지 않고 상수를 사용 하는 이유
# DELIVERY_DAYS = 2  # 2라는 숫자가 '배송일'임을 알려줌.
#
#
# def _is_holiday(day: datetime) -> bool:
#     return day.weekday() >= 5
#
#
# def get_eta(purchase_date: datetime) -> datetime:
#     current_Date = purchase_date
#     remaining_days = DELIVERY_DAYS
#
#     while remaining_days > 0:
#         current_Date += timedelta(days=1)
#         if not _is_holiday(current_Date):  # 다음날이 휴일/평일인지
#             remaining_days -= 1
#
#     return current_Date
#
#
# def test_get_eta_20250709():
#     result = get_eta(datetime(2025, 7, 9))
#     assert result == datetime(2025, 7, 11)
#
#
# def test_get_eta_20251231():
#     # 공휴일 정보 없어서 1월1일도 평일로 들어감.
#     result = get_eta(datetime(2025, 12, 31))
#     assert result == datetime(2026, 1, 2)
#
#
# def test_get_eta_20240228():  # 윤년
#     result = get_eta(datetime(2024, 2, 28))
#     assert result == datetime(2024, 3, 1)
#
#
# def test_get_eta_20250228():
#     result = get_eta(datetime(2025, 2, 28))
#     assert result == datetime(2025, 3, 4)
