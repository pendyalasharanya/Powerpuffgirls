"""
scraper.py - Simple web scraper using requests + BeautifulSoup
"""
import requests
from bs4 import BeautifulSoup
import re
import time
import json
import os
from pathlib import Path

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
}
CACHE_FILE = Path("data/scraped_cache.json")


def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def scrape_url(url, timeout=8):
    try:
        r = requests.get(url, headers=HEADERS, timeout=timeout)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "lxml")
        for tag in soup(["script", "style", "nav", "footer", "head"]):
            tag.decompose()
        text = soup.get_text(separator=" ")
        lines = [l.strip() for l in text.splitlines() if len(l.strip()) > 30]
        return clean_text(" ".join(lines))[:5000]
    except Exception as e:
        return ""


def load_cache():
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    if CACHE_FILE.exists():
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_cache(cache):
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)


def get_college_content(college_name, url, force=False):
    cache = load_cache()
    if not force and college_name in cache:
        return cache[college_name]
    content = scrape_url(url)
    time.sleep(1)
    cache[college_name] = content
    save_cache(cache)
    return content
