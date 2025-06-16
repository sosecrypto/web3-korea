# RSS 뉴스 피드 파서

이 프로젝트는 블록미디어의 RSS 피드를 파싱하고 분석하는 파이썬 스크립트입니다.

## RSS 피드 정보
- 블록미디어 메인 RSS: https://www.blockmedia.co.kr/feed/

## 블록미디어 RSS 데이터 구조

### 피드 기본 정보
- title: 블록미디어
- description: 믿고 보는 No1. 블록체인 뉴스
- link: https://www.blockmedia.co.kr/
- language: ko-KR
- updated: 최신 업데이트 시간

### 피드 메타데이터 필드
- title: 피드 제목
- title_detail: 제목 상세 정보
- links: 관련 링크 목록
- link: 피드 링크
- subtitle: 부제목
- subtitle_detail: 부제목 상세 정보
- updated: 업데이트 시간
- updated_parsed: 파싱된 업데이트 시간
- language: 언어
- sy_updateperiod: 업데이트 주기
- sy_updatefrequency: 업데이트 빈도
- image: 이미지 정보

### 뉴스 항목(entry) 필드
- title: 뉴스 제목
- title_detail: 제목 상세 정보
- links: 관련 링크 목록
- link: 뉴스 원문 링크
- authors: 작성자 목록
- author: 작성자
- author_detail: 작성자 상세 정보
- published: 발행일
- published_parsed: 파싱된 발행일
- tags: 태그 목록
- id: 고유 식별자
- guidislink: GUID가 링크인지 여부
- summary: 뉴스 요약
- summary_detail: 요약 상세 정보
- media_thumbnail: 미디어 썸네일
- href: 하이퍼링크
- media_content: 미디어 콘텐츠 (이미지 URL 등)
- tag: 태그
- pubdate2: 발행일 (대체 형식)
- post-id: 포스트 ID

### 예시 데이터
```python
# 첫 번째 뉴스 항목 예시
{
    "title": "BNB 스마트 체인, 샌드위치 공격 증가와 거래량 급증 동시 발생",
    "link": "https://www.blockmedia.co.kr/archives/927783",
    "published": "Sun, 15 Jun 2025 22:21:19 +0000",
    "author": "블록미디어",
    "category": "Digital Asset",
    "tags": [
        {"term": "Digital Asset", "scheme": None, "label": None},
        {"term": "CMC", "scheme": None, "label": None},
        {"term": "가상자산", "scheme": None, "label": None},
        {"term": "거래소", "scheme": None, "label": None},
        {"term": "비트코인", "scheme": None, "label": None},
        {"term": "암호화폐", "scheme": None, "label": None},
        {"term": "코인", "scheme": None, "label": None}
    ],
    "media_content": [
        {
            "medium": "image",
            "url": "https://www.blockmedia.co.kr/wp-content/uploads/2025/06/BNB-샌드위치-공격-1.png"
        }
    ]
}
```

## 프로젝트 구조
```
news/
├── venv/                  # 가상환경 디렉토리
├── simple_rss_test.py     # RSS 피드 파싱 스크립트
└── README.md             # 프로젝트 문서
```

## 기능
- RSS 피드의 기본 정보 출력 (제목, 설명, 링크, 언어, 업데이트 시간)
- 피드의 메타데이터 필드 확인
- 첫 번째 뉴스 항목의 상세 정보 출력
  - 제목, 링크, 발행일
  - 요약, 작성자, 카테고리, 태그
  - 미디어 콘텐츠 (이미지 등)

## 환경 설정

### Python 버전
- Python 3.13.3

### 필수 패키지
- feedparser 6.0.11
- requests 2.32.4
- sgmllib3k 1.0.0
- urllib3 2.4.0
- idna 3.10
- charset_normalizer 3.4.2
- certifi 2025.6.15

## 설치 및 실행 방법

1. Python 설치 (3.13.3 이상 권장)

2. 가상환경 설정:
   ```powershell
   # 가상환경 생성
   python -m venv venv
   
   # 가상환경 활성화
   # Windows:
   .\venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   ```

3. pip 업그레이드:
   ```powershell
   python -m pip install --upgrade pip
   ```

4. 필수 패키지 설치:
   ```powershell
   pip install feedparser requests
   ```

5. 스크립트 실행:
   ```powershell
   python simple_rss_test.py
   ```

## 주의사항
- 스크립트 실행 전 반드시 가상환경을 활성화해야 합니다.
- 가상환경이 활성화되지 않은 상태에서는 `ModuleNotFoundError: No module named 'feedparser'` 오류가 발생할 수 있습니다. 