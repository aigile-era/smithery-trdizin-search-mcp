from mcp.server.fastmcp import FastMCP
from app import TRDizinScraper
import json
import os
import sys

# Initialize MCP server
mcp = FastMCP("trdizin-mcp")

# Global scraper instance
scraper = None

def initialize_scraper(config=None):
    """Scraper'ı konfigürasyonla başlat"""
    global scraper
    api_key = None
    
    if config and 'firecrawlApiKey' in config:
        api_key = config['firecrawlApiKey']
    else:
        api_key = os.getenv('FIRECRAWL_API_KEY')
    
    if not api_key:
        raise ValueError("Firecrawl API key is required. Please provide it in the configuration or set FIRECRAWL_API_KEY environment variable.")
    
    scraper = TRDizinScraper(api_key=api_key)

@mcp.tool()
async def search_trdizin_publications(query: str, order: str = "publicationYear-DESC", page: int = 1, limit: int = 20) -> str:
    """TR Dizin'de yayın ara
    
    Args:
        query: Arama terimi
        order: Sıralama (publicationYear-DESC, publicationYear-ASC, relevance-DESC, title-ASC)
        page: Sayfa numarası (varsayılan: 1)
        limit: Sayfa başına sonuç sayısı (varsayılan: 20)
    """
    if scraper is None:
        return json.dumps({"error": "Server not configured. Please provide Firecrawl API key.", "success": False}, ensure_ascii=False, indent=2)
    
    results = scraper.search_publications(query, order, page, limit)
    return json.dumps(results, ensure_ascii=False, indent=2)

@mcp.tool()
async def search_trdizin_journals(query: str, order: str = "title-ASC", page: int = 1, limit: int = 20) -> str:
    """TR Dizin'de dergi ara
    
    Args:
        query: Arama terimi
        order: Sıralama (title-ASC, title-DESC, relevance-DESC)
        page: Sayfa numarası (varsayılan: 1)
        limit: Sayfa başına sonuç sayısı (varsayılan: 20)
    """
    if scraper is None:
        return json.dumps({"error": "Server not configured. Please provide Firecrawl API key.", "success": False}, ensure_ascii=False, indent=2)
    
    results = scraper.search_journals(query, order, page, limit)
    return json.dumps(results, ensure_ascii=False, indent=2)

@mcp.tool()
async def search_trdizin_authors(query: str, order: str = "relevance-DESC", page: int = 1, limit: int = 20) -> str:
    """TR Dizin'de yazar ara
    
    Args:
        query: Arama terimi
        order: Sıralama (relevance-DESC, name-ASC, name-DESC)
        page: Sayfa numarası (varsayılan: 1)
        limit: Sayfa başına sonuç sayısı (varsayılan: 20)
    """
    if scraper is None:
        return json.dumps({"error": "Server not configured. Please provide Firecrawl API key.", "success": False}, ensure_ascii=False, indent=2)
    
    results = scraper.search_authors(query, order, page, limit)
    return json.dumps(results, ensure_ascii=False, indent=2)

# Configuration callback for runtime configuration
def configure_server(config):
    """Server konfigürasyonu için callback fonksiyonu"""
    try:
        initialize_scraper(config)
        return {"success": True, "message": "Server configured successfully"}
    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    # Eğer konfigürasyon command line'dan gelirse
    if len(sys.argv) > 1:
        try:
            config = json.loads(sys.argv[1])
            initialize_scraper(config)
        except json.JSONDecodeError:
            # Eğer JSON değilse environment variable'dan almaya çalış
            initialize_scraper()
    else:
        # Environment variable'dan almaya çalış
        try:
            initialize_scraper()
        except ValueError:
            # Konfigürasyon olmadan çalıştır, runtime'da konfigüre edilecek
            pass
    
    mcp.run(transport="stdio")