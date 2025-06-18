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

## 구글 스프레드시트 자동 뉴스 수집 자동화 가이드

### 1. 환경 및 준비 사항
- Python 3.x
- feedparser, gspread, google-auth 패키지 설치 (가상환경 권장)
- 구글 클라우드에서 서비스 계정 생성 및 JSON 키 발급
- Google Sheets API, Google Drive API 활성화
- 서비스 계정 이메일을 구글 시트에 편집자로 공유
- (권장) 구글 시트 첫 행에 컬럼명: 제목 | 링크 | 발행일 | 요약

### 2. rss_to_gsheet.py 주요 동작
- 블록미디어 RSS에서 모든 뉴스 항목을 파싱
- 구글 시트의 기존 링크(2번째 열 기준)와 중복되지 않는 뉴스만 추가
- 실행 시 추가된 뉴스 개수 출력

### 3. 윈도우 작업 스케줄러 자동화 설정
1. **python.exe 경로 확인**
   - 예시: `C:\Users\djatj\news\venv\Scripts\python.exe`
2. **스크립트 경로 확인**
   - 예시: `C:\Users\djatj\news\rss_to_gsheet.py`
3. **작업 스케줄러 실행 및 새 작업 만들기**
   - 이름: 예) RSS 자동 수집
   - 트리거: "매일" + "오전 9:00"
   - 동작: 프로그램/스크립트에 python.exe 경로, 인수에 스크립트 경로, 시작 위치에 프로젝트 폴더 경로 입력
4. **조건/설정**: 기본값 사용(필요시 절전 해제 등)
5. **테스트**: 작업 라이브러리에서 수동 실행하여 정상 동작 확인

### 4. 참고 및 주의사항
- 컴퓨터가 오전 9시에 켜져 있고, 작업 스케줄러가 활성화되어 있어야 자동 실행됨
- 스크립트는 중복 뉴스(링크 기준)를 자동으로 건너뜀
- 서비스 계정이 시트에 편집자로 공유되어 있어야 함
- API 사용 설정이 안 되어 있으면 403 에러가 발생할 수 있음 (Google Cloud Console에서 API 활성화 필요)
- 에러 발생 시 try-except로 에러 메시지 확인 가능

### 5. 예시 실행 결과
- "구글 시트에 3개의 새로운 뉴스가 추가되었습니다." 등으로 결과 출력
