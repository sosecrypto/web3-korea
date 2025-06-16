import feedparser
from datetime import datetime
from typing import List, Dict, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RSSParser:
    def __init__(self):
        self.feed_urls = {
            'naver': 'https://news.naver.com/rss/main',
            'daum': 'https://news.daum.net/rss/today',
            'khan': 'https://www.khan.co.kr/rss/rssdata/total_news.xml'
        }
    
    def parse_feed(self, url: str) -> List[Dict[str, Any]]:
        """
        RSS 피드를 파싱하여 뉴스 항목 리스트를 반환합니다.
        """
        try:
            feed = feedparser.parse(url)
            news_items = []
            
            for entry in feed.entries:
                news_item = {
                    'title': entry.title,
                    'link': entry.link,
                    'published': self._parse_date(entry.published),
                    'summary': entry.summary if hasattr(entry, 'summary') else '',
                    'source': self._get_source_from_url(url)
                }
                news_items.append(news_item)
            
            return news_items
        except Exception as e:
            logger.error(f"RSS 피드 파싱 중 오류 발생: {str(e)}")
            return []
    
    def _parse_date(self, date_str: str) -> datetime:
        """
        문자열 날짜를 datetime 객체로 변환합니다.
        """
        try:
            return datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %z')
        except ValueError:
            return datetime.now()
    
    def _get_source_from_url(self, url: str) -> str:
        """
        URL에서 뉴스 소스를 추출합니다.
        """
        for source, feed_url in self.feed_urls.items():
            if source in url:
                return source
        return 'unknown'
    
    def get_all_news(self) -> List[Dict[str, Any]]:
        """
        모든 RSS 피드에서 뉴스를 수집합니다.
        """
        all_news = []
        for url in self.feed_urls.values():
            news_items = self.parse_feed(url)
            all_news.extend(news_items)
        return all_news 