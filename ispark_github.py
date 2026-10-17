"""
GitHub Actions için İSPARK veri çekici.
Tek seferlik çalışır (döngü yok): veriyi çeker, timestamp ekler, data/ispark_log.csv'ye ekler.
Zamanlamayı GitHub Actions yapar.
"""

import os
import sys
import time
from datetime import datetime
from zoneinfo import ZoneInfo

import pandas as pd
import requests

API_URL = "https://api.ibb.gov.tr/ispark/Park"
KLASOR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(KLASOR, "data", "ispark_log.csv")


def veri_cek():
    """3 deneme yapar; hepsi başarısız olursa hatayı fırlatır."""
    son_hata = None
    for deneme in range(1, 4):
        try:
            r = requests.get(
                API_URL,
                timeout=30,
                headers={"User-Agent": "Mozilla/5.0 (ispark-arastirma)"},
            )
            print(f"HTTP durum kodu: {r.status_code}")
            r.raise_for_status()
            return r.json()
        except Exception as e:
            son_hata = e
            print(f"Deneme {deneme} başarısız: {e}")
            time.sleep(10)
    raise son_hata


def main():
    data = veri_cek()
    df = pd.json_normalize(data)

    # GitHub sunucusu UTC çalışır; saati İstanbul saatine çeviriyoruz
    simdi = datetime.now(ZoneInfo("Europe/Istanbul")).strftime("%Y-%m-%d %H:%M:%S")
    df.insert(0, "timestamp", simdi)

    os.makedirs(os.path.dirname(CSV_FILE), exist_ok=True)
    dosya_var = os.path.exists(CSV_FILE)
    df.to_csv(
        CSV_FILE,
        mode="a",
        header=not dosya_var,
        index=False,
        encoding="utf-8-sig" if not dosya_var else "utf-8",
    )
    print(f"[{simdi}] {len(df)} satır eklendi -> {CSV_FILE}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"HATA: {e}")
        sys.exit(1)
