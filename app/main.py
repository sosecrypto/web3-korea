from fastapi import FastAPI, HTTPException
from typing import List, Dict, Any
from .rss_parser import RSSParser

app = FastAPI(
    title="한국 뉴스 RSS API",
    description="한국 주요 뉴스 사이트의 RSS 피드를 수집하여 제공하는 API",
    version="1.0.0"
)

rss_parser = RSSParser()

@app.get("/")
async def root():
    return {"message": "한국 뉴스 RSS API에 오신 것을 환영합니다."}

@app.get("/api/news", response_model=List[Dict[str, Any]])
async def get_all_news():
    """
    모든 뉴스 소스에서 최신 뉴스를 가져옵니다.
    """
    try:
        news_items = rss_parser.get_all_news()
        return news_items
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/news/sources")
async def get_news_sources():
    """
    지원하는 뉴스 소스 목록을 반환합니다.
    """
    return {"sources": list(rss_parser.feed_urls.keys())}

@app.get("/api/news/{source}")
async def get_news_by_source(source: str):
    """
    특정 뉴스 소스의 최신 뉴스를 가져옵니다.
    """
    if source not in rss_parser.feed_urls:
        raise HTTPException(status_code=404, detail="지원하지 않는 뉴스 소스입니다.")
    
    try:
        news_items = rss_parser.parse_feed(rss_parser.feed_urls[source])
        return news_items
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 