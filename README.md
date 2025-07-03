# TR Dizin MCP Server

TR Dizin veritabanında arama yapmak için geliştirilmiş MCP (Model Context Protocol) sunucusu.

## Özellikler

- **Yayın Arama**: TR Dizin'de makale ve yayın arama
- **Dergi Arama**: TR Dizin'de dergi arama  
- **Yazar Arama**: TR Dizin'de yazar arama
- **Smithery Desteği**: Smithery platformu üzerinden kolay kurulum ve kullanım

## Smithery ile Kurulum (Önerilen)

Bu MCP server Smithery platformu üzerinden kolayca kullanılabilir:

1. [Smithery](https://smithery.ai) hesabınıza giriş yapın
2. TR Dizin MCP Server'ı bulun ve yükleyin
3. Firecrawl API anahtarınızı yapılandırmaya ekleyin
4. Claude Desktop veya diğer MCP istemcilerinizde kullanmaya başlayın

Link: https://smithery.ai/server/%40Utku-Unluer%2Fsmithery-trdizin-search-mcp/tools

### Firecrawl API Key Alma

1. [Firecrawl.dev](https://firecrawl.dev) adresine gidin
2. Hesap oluşturun veya giriş yapın
3. API anahtarınızı alın (fc- ile başlar)
4. Bu anahtarı Smithery yapılandırmasında kullanın

## Manuel Kurulum (Geliştirici)

### Gereksinimler

- Python 3.11+
- Firecrawl API anahtarı

### Kurulum Adımları

```bash
# 1. Repoyu klonlayın
git clone <repo-url>
cd trdizin-mcp

# 2. Sanal ortam oluşturun
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# veya
venv\Scripts\activate     # Windows

# 3. Bağımlılıkları yükleyin
pip install -r requirements.txt

# 4. Environment variable ayarlayın
export FIRECRAWL_API_KEY="your-api-key-here"

# 5. Server'ı çalıştırın
python server.py
```

### Claude Desktop ile Manuel Kullanım

`~/Library/Application Support/Claude/claude_desktop_config.json` dosyasına ekleyin:

```json
{
  "mcpServers": {
    "trdizin": {
      "command": "python3",
      "args": ["/path/to/trdizin-mcp/server.py"],
      "env": {
        "FIRECRAWL_API_KEY": "your-api-key-here",
        "PYTHONPATH": "/path/to/trdizin-mcp"
      }
    }
  }
}
```

## MCP Tools

### search_trdizin_publications
TR Dizin'de yayın arar.

**Parametreler:**
- `query`: Arama terimi (zorunlu)
- `order`: Sıralama seçenekleri:
  - `publicationYear-DESC` (varsayılan): Yayın yılına göre azalan
  - `publicationYear-ASC`: Yayın yılına göre artan
  - `relevance-DESC`: İlgiye göre azalan
  - `title-ASC`: Başlığa göre artan
- `page`: Sayfa numarası (varsayılan: 1)
- `limit`: Sayfa başına sonuç sayısı (varsayılan: 20, maksimum: 100)

**Örnek Kullanım:**
```
TR Dizin'de "makine öğrenmesi" konusunda yayın ara
```

### search_trdizin_journals  
TR Dizin'de dergi arar.

**Parametreler:**
- `query`: Arama terimi (zorunlu)
- `order`: Sıralama seçenekleri:
  - `title-ASC` (varsayılan): Başlığa göre artan
  - `title-DESC`: Başlığa göre azalan
  - `relevance-DESC`: İlgiye göre azalan
- `page`: Sayfa numarası (varsayılan: 1)
- `limit`: Sayfa başına sonuç sayısı (varsayılan: 20, maksimum: 100)

**Örnek Kullanım:**
```
TR Dizin'de "bilgisayar" içeren dergileri ara
```

### search_trdizin_authors
TR Dizin'de yazar arar.

**Parametreler:**
- `query`: Arama terimi (zorunlu)
- `order`: Sıralama seçenekleri:
  - `relevance-DESC` (varsayılan): İlgiye göre azalan
  - `name-ASC`: İsme göre artan
  - `name-DESC`: İsme göre azalan
- `page`: Sayfa numarası (varsayılan: 1)
- `limit`: Sayfa başına sonuç sayısı (varsayılan: 20, maksimum: 100)

**Örnek Kullanım:**
```
TR Dizin'de "Ahmet Özkan" yazarını ara
```

## Docker ile Çalıştırma

```bash
# Docker image oluşturun
docker build -t trdizin-mcp .

# Container'ı çalıştırın
docker run -e FIRECRAWL_API_KEY="your-api-key" -it trdizin-mcp
```

## Geliştirme

### Test Etme

MCP Inspector kullanarak test edebilirsiniz:

```bash
# MCP Inspector'ı yükleyin
npm install -g @modelcontextprotocol/inspector

# Server'ı test edin
mcp-inspector python server.py
```

### Hata Ayıklama

Verbose logging için:

```bash
export DEBUG=1
python server.py
```

## Sorun Giderme

### Yaygın Hatalar

1. **"Firecrawl API key is required"**
   - Firecrawl API anahtarınızın doğru yapılandırıldığından emin olun
   - API anahtarının geçerli olduğunu kontrol edin

2. **"Module not found"**
   - Tüm bağımlılıkların yüklendiğinden emin olun: `pip install -r requirements.txt`
   - Python path'ının doğru ayarlandığından emin olun

3. **"Connection timeout"**
   - İnternet bağlantınızı kontrol edin
   - TR Dizin sitesinin erişilebilir olduğunu kontrol edin

### Destek

- Sorunlar için GitHub Issues kullanın
- Firecrawl API ile ilgili sorunlar için [Firecrawl Documentation](https://docs.firecrawl.dev) kontrol edin
- Smithery ile ilgili sorunlar için [Smithery Documentation](https://smithery.ai/docs) kontrol edin

## Lisans

MIT License

## Katkıda Bulunma

1. Bu repoyu fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## Changelog

### v1.1.0
- Smithery desteği eklendi
- Konfigürasyon yönetimi iyileştirildi
- API key güvenliği artırıldı
- Docker optimizasyonları

### v1.0.0
- İlk sürüm
- Temel TR Dizin arama fonksiyonları
- MCP server implementasyonu




