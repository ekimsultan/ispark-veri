# ispark-veri
# İSPARK Otopark Doluluk Verisi

Bu depo, "İSPARK Otopark Doluluk Analizi ve Park Et Devam Et (P+R) Kapasite
Optimizasyonu" başlıklı araştırma çalışması için toplanan ham veriyi içerir.

## Veri toplama

- Kaynak: İBB İSPARK Park API (https://api.ibb.gov.tr/ispark/Park)
- Sıklık: yaklaşık 15 dakikada bir (GitHub Actions ile otomatik)
- Zaman damgası: İstanbul saati (UTC+3), her satırın ilk sütunu `timestamp`
- Dosya: `data/ispark_log.csv`
- Not: Zamanlanmış çalışmalar GitHub tarafından geciktirilebilir, bu yüzden
  aralıklar tam 15 dakika olmayabilir. Eksik zaman dilimleri olabilir.

## Veri kaynağı ve lisans

Veri, İstanbul Büyükşehir Belediyesi (İBB) Açık Veri Portalı üzerinden
yayınlanan İSPARK park verisidir ve İBB Açık Veri Lisansı kapsamında
kullanılmıştır.

Atıf 4.0 Uluslararası (CC BY 4.0) kapsamında lisanslanan kamu sektörü bilgilerini içerir.

Bu çalışma İBB tarafından desteklenmemekte veya onaylanmamaktadır.

## Sınırlılıklar

- Veri, API'nin döndürdüğü otoparkları kapsar; İstanbul'daki tüm İSPARK
  otoparklarını kapsamayabilir.
- Doluluk bilgisi, P+R talebinin doğrudan ölçümü değil, bir göstergesidir.
- Veri "olduğu gibi" sunulur; hatalı veya tutarsız kayıtlar içerebilir.
