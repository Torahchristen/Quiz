#!/usr/bin/env python3
"""
update_catalog.py - Update catalog.json and en/catalog.json based on canonical quiz JSON files.
"""

import json
import glob
import os
import sys
from datetime import datetime, timezone

EN_CATEGORIES = [
    {
        "id": "torah",
        "name": "Torah Weekly Portions",
        "description": "54 Parashot of the Torah"
    },
    {
        "id": "gesetz",
        "name": "Law & Torah",
        "description": "The Books of the Law (Exodus to Deuteronomy)"
    },
    {
        "id": "geschichte",
        "name": "Historical Books",
        "description": "Joshua to Esther"
    },
    {
        "id": "weisheit",
        "name": "Wisdom & Poetry",
        "description": "Job, Psalms, Proverbs, Ecclesiastes, Song of Solomon"
    },
    {
        "id": "propheten",
        "name": "Prophets (Major & Minor)",
        "description": "Isaiah to Malachi"
    },
    {
        "id": "at",
        "name": "Old Testament",
        "description": "The Old Testament: Law, History, Wisdom, and Prophets"
    },
    {
        "id": "nt",
        "name": "New Testament",
        "description": "Gospels, Acts, Epistles, and Revelation"
    },
    {
        "id": "themen",
        "name": "Topics & Feasts",
        "description": "Bible Topics, Feasts, and Doctrine"
    }
]


def main():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    catalog_path = os.path.join(root_dir, 'catalog.json')

    if not os.path.exists(catalog_path):
        print("ERROR: catalog.json not found!")
        sys.exit(1)

    with open(catalog_path, 'r', encoding='utf-8') as f:
        catalog_data = json.load(f)

    json_files = sorted([
        f for f in glob.glob(os.path.join(root_dir, '*.json'))
        if not f.endswith('catalog.json') and not f.endswith('1_mose_300_fragen_komplett.json')
    ])

    updated_quizzes = []

    for file_path in json_files:
        filename = os.path.basename(file_path)
        rel_url = f"./{filename}"

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        meta = data.get('metadata', {})
        questions = data.get('questions', [])

        actual_count = len(questions)
        actual_size = os.path.getsize(file_path)

        quiz_entry = {
            "quizId": meta.get("quizId"),
            "category": meta.get("category"),
            "title": meta.get("title"),
            "subtitle": meta.get("subtitle"),
            "author": meta.get("author", "Schlachter 1951"),
            "version": meta.get("version", "2.0.0"),
            "questionCount": actual_count,
            "difficulty": meta.get("difficulty", "medium"),
            "tags": meta.get("tags", []),
            "sizeBytes": actual_size,
            "downloadUrl": rel_url
        }
        updated_quizzes.append(quiz_entry)

    catalog_data['quizzes'] = updated_quizzes

    with open(catalog_path, 'w', encoding='utf-8') as f:
        json.dump(catalog_data, f, ensure_ascii=False, indent=2)
        f.write('\n')

    print(f"Successfully updated catalog.json with {len(updated_quizzes)} quizzes.")

    # Also update en/catalog.json if en/ exists
    en_dir = os.path.join(root_dir, 'en')
    if os.path.isdir(en_dir):
        en_json_files = sorted([
            f for f in glob.glob(os.path.join(en_dir, '*.json'))
            if not f.endswith('catalog.json')
        ])
        en_quizzes = []
        for file_path in en_json_files:
            filename = os.path.basename(file_path)
            rel_url = f"./en/{filename}"
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            meta = data.get('metadata', {})
            questions = data.get('questions', [])
            actual_count = len(questions)
            actual_size = os.path.getsize(file_path)
            en_quizzes.append({
                "quizId": meta.get("quizId"),
                "category": meta.get("category"),
                "title": meta.get("title"),
                "subtitle": meta.get("subtitle"),
                "author": meta.get("author", "King James Version (1769)"),
                "language": meta.get("language", "en"),
                "version": meta.get("version", "2.3.0"),
                "questionCount": actual_count,
                "difficulty": meta.get("difficulty", "medium"),
                "tags": meta.get("tags", []),
                "sizeBytes": actual_size,
                "downloadUrl": rel_url
            })
        en_catalog_path = os.path.join(en_dir, 'catalog.json')
        en_catalog_data = {
            "catalogVersion": catalog_data.get("catalogVersion", "2.3.0"),
            "lastUpdated": datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
            "language": "en",
            "categories": EN_CATEGORIES,
            "quizzes": en_quizzes
        }
        with open(en_catalog_path, 'w', encoding='utf-8') as f:
            json.dump(en_catalog_data, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print(f"Successfully updated en/catalog.json with {len(en_quizzes)} English quizzes.")


if __name__ == '__main__':
    main()
