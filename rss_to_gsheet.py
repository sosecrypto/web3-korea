import feedparser
import gspread
from google.oauth2.service_account import Credentials

# === 아래 항목을 본인 환경에 맞게 수정하세요 ===
SERVICE_ACCOUNT_FILE = 'web3data-e2dfd-d48bd6a62a71.json'  # 서비스 계정 키 파일명
SPREADSHEET_ID = '1wUkcc4PZIGr3qB48vL1Xagwf3jGSIAcrYj_QsGBUZT0'              # 구글 시트 ID
WORKSHEET_NAME = '시트1'                            # 워크시트 이름

# 구글 인증 및 시트 열기
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scopes)
gc = gspread.authorize(creds)
sh = gc.open_by_key(SPREADSHEET_ID)
worksheet = sh.worksheet(WORKSHEET_NAME)

# 1. 시트에 이미 있는 링크 목록 가져오기 (2번째 열이 링크라고 가정)
existing_links = set()
all_rows = worksheet.get_all_values()
for row in all_rows[1:]:  # 첫 행은 헤더라고 가정
    if len(row) > 1:
        existing_links.add(row[1])

# 2. RSS 피드 파싱
url = "https://www.blockmedia.co.kr/feed/"
feed = feedparser.parse(url)

# 3. 중복 없이 모든 뉴스 추가
new_count = 0
for entry in feed.entries:
    link = entry.link
    if link not in existing_links:
        row = [
            entry.title,
            entry.link,
            entry.published if hasattr(entry, 'published') else '',
            entry.summary if hasattr(entry, 'summary') else ''
        ]
        worksheet.append_row(row)
        new_count += 1

print(f"구글 시트에 {new_count}개의 새로운 뉴스가 추가되었습니다.")

try:
    print("구글 시트에 뉴스가 성공적으로 추가되었습니다.")
except Exception as e:
    print("에러 발생:", e) 