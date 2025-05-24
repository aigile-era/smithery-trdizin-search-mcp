# TR Dizin MCP Server

TR Dizin veritabanında arama yapmak için geliştirilmiş MCP (Model Context Protocol) sunucusu.

## Özellikler

- **Yayın Arama**: TR Dizin'de makale ve yayın arama
- **Dergi Arama**: TR Dizin'de dergi arama  
- **Yazar Arama**: TR Dizin'de yazar arama

## macOS'ta Kurulum

### 1. Python sanal ortamı oluşturun (önerilen)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Bağımlılıkları yükleyin
```bash
pip3 install -r requirements.txt
```

## Kullanım

### Geliştirme modunda çalıştırma
```bash
python3 server.py
```

### Claude Desktop ile Kullanım

Claude Desktop uygulamasında kullanmak için `~/Library/Application Support/Claude/claude_desktop_config.json` dosyasına ekleyin:

```json
{
  "mcpServers": {
    "trdizin": {
      "command": "python3",
      "args": ["/Users/utkuunluer/Desktop/trdizinmcp/server.py"],
      "env": {
        "PYTHONPATH": "/Users/utkuunluer/Desktop/trdizinmcp"
      }
    }
  }
}
```

## MCP Tools

### search_trdizin_publications
TR Dizin'de yayın arar.

**Parametreler:**
- `query`: Arama terimi
- `order`: Sıralama (publicationYear-DESC, publicationYear-ASC, relevance-DESC, title-ASC)
- `page`: Sayfa numarası (varsayılan: 1)
- `limit`: Sayfa başına sonuç sayısı (varsayılan: 20)

### search_trdizin_journals  
TR Dizin'de dergi arar.

**Parametreler:**
- `query`: Arama terimi
- `order`: Sıralama (title-ASC, title-DESC, relevance-DESC)
- `page`: Sayfa numarası (varsayılan: 1)
- `limit`: Sayfa başına sonuç sayısı (varsayılan: 20)

### search_trdizin_authors
TR Dizin'de yazar arar.

**Parametreler:**
- `query`: Arama terimi
- `order`: Sıralama (relevance-DESC, name-ASC, name-DESC)
- `page`: Sayfa numarası (varsayılan: 1)
- `limit`: Sayfa başına sonuç sayısı (varsayılan: 20)

## 🚀 macOS'ta Adım Adım Kurulum

```bash
# 1. Proje dizinine gidin
cd /Users/utkuunluer/Desktop/trdizinmcp

# 2. Python sanal ortamı oluşturun
python3 -m venv venv

# 3. Sanal ortamı etkinleştirin
source venv/bin/activate

# 4. Bağımlılıkları yükleyin
pip3 install -r requirements.txt

# 5. Server'ı çalıştırın
python3 server.py
```

## Docker ile Çalıştırma (Opsiyonel)

```bash
# Docker image oluşturun
docker build -t trdizin-mcp .

# Container'ı çalıştırın
docker run -it trdizin-mcp
```

## Terminal Komutları

### Sanal ortamı her seferinde etkinleştirmek için:
```bash
cd /Users/utkuunluer/Desktop/trdizinmcp
source venv/bin/activate
python3 server.py
```

### Sanal ortamdan çıkmak için:
```bash
deactivate
```

## Troubleshooting

### Python3 bulunamıyor hatası:
```bash
# Homebrew ile Python yükleyin
brew install python3
```

### Permission denied hatası:
```bash
chmod +x server.py
```

## Lisans

MIT
