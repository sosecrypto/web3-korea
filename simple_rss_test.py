# feedparser 라이브러리를 가져옵니다.
# 이 라이브러리는 RSS 피드를 쉽게 파싱할 수 있게 해주는 도구입니다.
# RSS 피드는 XML 형식으로 되어있는데, 이를 Python에서 쉽게 다룰 수 있게 변환해줍니다.
import feedparser
import json
from pprint import pprint

# 블록미디어의 RSS 피드 URL을 지정합니다.
# RSS 피드는 웹사이트의 최신 콘텐츠를 자동으로 가져올 수 있는 형식입니다.
# 블록미디어는 이 URL을 통해 최신 뉴스 목록을 제공합니다.
url = "https://www.blockmedia.co.kr/feed/"

# feedparser.parse() 함수를 사용하여 RSS 피드를 파싱합니다.
# 이 함수는 URL에서 RSS 피드를 가져와서 Python 객체로 변환합니다.
# feed 객체는 피드의 전체 정보와 각 뉴스 항목들을 포함합니다.
feed = feedparser.parse(url)

print("=== RSS 피드의 기본 정보 ===")
print(f"피드 제목: {feed.feed.title}")
print(f"피드 설명: {feed.feed.description}")
print(f"피드 링크: {feed.feed.link}")
print(f"피드 언어: {feed.feed.language}")
print(f"피드 업데이트 시간: {feed.feed.updated}")
print("\n=== RSS 피드의 메타데이터 ===")
print("사용 가능한 메타데이터 필드들:")
for key in feed.feed.keys():
    print(f"- {key}")

print("\n=== 첫 번째 뉴스 항목의 상세 정보 ===")
if feed.entries:
    first_entry = feed.entries[0]
    print("\n사용 가능한 필드들:")
    for key in first_entry.keys():
        print(f"- {key}")
    
    print("\n첫 번째 뉴스 항목의 상세 데이터:")
    print(f"제목: {first_entry.title}")
    print(f"링크: {first_entry.link}")
    print(f"발행일: {first_entry.published}")
    print(f"요약: {first_entry.summary if hasattr(first_entry, 'summary') else '요약 없음'}")
    print(f"작성자: {first_entry.author if hasattr(first_entry, 'author') else '작성자 정보 없음'}")
    print(f"카테고리: {first_entry.category if hasattr(first_entry, 'category') else '카테고리 없음'}")
    print(f"태그: {first_entry.tags if hasattr(first_entry, 'tags') else '태그 없음'}")
    
    # 추가 메타데이터가 있는 경우 출력
    if hasattr(first_entry, 'media_content'):
        print("\n미디어 콘텐츠:")
        pprint(first_entry.media_content)
    
    if hasattr(first_entry, 'content'):
        print("\n콘텐츠:")
        pprint(first_entry.content)

print("\n=== 전체 피드 구조 확인 ===")
print("피드 객체의 모든 속성:")
for key in dir(feed):
    if not key.startswith('_'):  # 내부 속성 제외
        print(f"- {key}") 