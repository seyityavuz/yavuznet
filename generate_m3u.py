import json

# JSON dosyanızın yolu
json_dosya_yolu = 'data.json'
# Çıkış M3U8 dosyasının yolu
m3u_dosya_yolu = 'liste.m3u8'

try:
    with open(json_dosya_yolu, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # M3U8 içeriğini oluşturmaya başla
    m3u_content = "#EXTM3U\n"

    for item in data:
        title = item.get("title", "Bilinmeyen Kanal")
        group = item.get("group", "Genel")
        url = item.get("url", "")
        
        # M3U8 satır formatı
        m3u_content += f'#EXTINF:-1 group-title="{group}",{title}\n'
        m3u_content += f'{url}\n'

    with open(m3u_dosya_yolu, 'w', encoding='utf-8') as f:
        f.write(m3u_content)

    print("M3U8 dosyası başarıyla oluşturuldu!")

except Exception as e:
    print(f"Hata oluştu: {e}")

