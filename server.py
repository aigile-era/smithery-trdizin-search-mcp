from mcp.server.fastmcp import FastMCP
from app import TRDizinScraper
import json

# Initialize MCP server
mcp = FastMCP("trdizin-mcp")

# Initialize scraper
scraper = TRDizinScraper()

@mcp.tool()
async def search_trdizin_publications(query: str, order: str = "publicationYear-DESC", page: int = 1, limit: int = 20) -> str:
    """TR Dizin'de yayın ara"""
    results = scraper.search_publications(query, order, page, limit)
    return json.dumps(results, ensure_ascii=False, indent=2)

@mcp.tool()
async def search_trdizin_journals(query: str, order: str = "title-ASC", page: int = 1, limit: int = 20) -> str:
    """TR Dizin'de dergi ara"""
    results = scraper.search_journals(query, order, page, limit)
    return json.dumps(results, ensure_ascii=False, indent=2)

@mcp.tool()
async def search_trdizin_authors(query: str, order: str = "relevance-DESC", page: int = 1, limit: int = 20) -> str:
    """TR Dizin'de yazar ara"""
    results = scraper.search_authors(query, order, page, limit)
    return json.dumps(results, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    mcp.run(transport="stdio")
