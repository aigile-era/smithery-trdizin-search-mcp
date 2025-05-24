import json
from firecrawl import FirecrawlApp
from typing import Dict, Any, Optional
from urllib.parse import quote
import os

class TRDizinScraper:
    def __init__(self, api_key: Optional[str] = None):
        """
        TR Dizin Scraper sınıfı
        
        Args:
            api_key: Firecrawl API anahtarı. Eğer verilmezse FIRECRAWL_API_KEY environment variable'ından alınır.
        """
        if api_key:
            self.api_key = api_key
        else:
            self.api_key = os.getenv('FIRECRAWL_API_KEY')
            
        if not self.api_key:
            raise ValueError("Firecrawl API anahtarı gerekli! Lütfen FIRECRAWL_API_KEY environment variable'ını ayarlayın veya api_key parametresini kullanın.")
            
        self.fc = FirecrawlApp(api_key=self.api_key)
        self.base_url = "https://search.trdizin.gov.tr"

    def search_publications(self, query: str, order: str = "publicationYear-DESC", page: int = 1, limit: int = 20) -> Dict[str, Any]:
        """TR Dizin'de yayın arama"""
        encoded_query = quote(query)
        url = f"{self.base_url}/tr/yayin/ara?q={encoded_query}&order={order}&page={page}&limit={limit}"
        
        try:
            result = self.fc.scrape_url(url, formats=['markdown'])
            return {
                "url": url,
                "query": query,
                "data": result.markdown if hasattr(result, 'markdown') else str(result),
                "success": True
            }
        except Exception as e:
            return {"error": f"Yayın arama hatası: {str(e)}", "success": False}

    def search_journals(self, query: str, order: str = "title-ASC", page: int = 1, limit: int = 20) -> Dict[str, Any]:
        """TR Dizin'de dergi arama"""
        encoded_query = quote(query)
        url = f"{self.base_url}/tr/dergi/ara?q={encoded_query}&order={order}&page={page}&limit={limit}"
        
        try:
            result = self.fc.scrape_url(url, formats=['markdown'])
            return {
                "url": url,
                "query": query,
                "data": result.markdown if hasattr(result, 'markdown') else str(result),
                "success": True
            }
        except Exception as e:
            return {"error": f"Dergi arama hatası: {str(e)}", "success": False}

    def search_authors(self, query: str, order: str = "relevance-DESC", page: int = 1, limit: int = 20) -> Dict[str, Any]:
        """TR Dizin'de yazar arama"""
        encoded_query = quote(query)
        url = f"{self.base_url}/tr/yazar/ara?q={encoded_query}&order={order}&page={page}&limit={limit}"
        
        try:
            result = self.fc.scrape_url(url, formats=['markdown'])
            return {
                "url": url,
                "query": query,
                "data": result.markdown if hasattr(result, 'markdown') else str(result),
                "success": True
            }
        except Exception as e:
            return {"error": f"Yazar arama hatası: {str(e)}", "success": False}