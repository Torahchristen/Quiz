#!/usr/bin/env python3
"""
validate_quizzes.py - Validate quiz integrity and catalog consistency (DE and EN).
"""

import json
import glob
import os
import re
import sys

def validate_question_list(filename, questions, crit_errors, inconsistencies, quality_warnings, all_q_ids=None):
    seen_file_q_ids = set()
    for idx, q in enumerate(questions):
        q_id = q.get('questionId')
        if not q_id:
            crit_errors.append(f"{filename} Q#{idx+1}: Missing questionId")
        else:
            if q_id in seen_file_q_ids:
                inconsistencies.append(f"{filename} Q#{idx+1}: Duplicate questionId '{q_id}' within file")
            seen_file_q_ids.add(q_id)

            if all_q_ids is not None:
                if q_id in all_q_ids:
                    inconsistencies.append(f"Duplicate questionId '{q_id}' across files: {filename} and {all_q_ids[q_id]}")
                else:
                    all_q_ids[q_id] = filename

        for req_field in ['questionId', 'text', 'type', 'options', 'correctAnswers', 'bibleReference']:
            if req_field not in q or q[req_field] is None or q[req_field] == '':
                crit_errors.append(f"{filename} Q#{idx+1} ({q_id}): Missing/empty required field '{req_field}'")

        if 'explanation' not in q or q['explanation'] is None:
            crit_errors.append(f"{filename} Q#{idx+1} ({q_id}): Missing 'explanation' field")
        if 'explanationReviewed' not in q or not isinstance(q.get('explanationReviewed'), bool):
            crit_errors.append(f"{filename} Q#{idx+1} ({q_id}): Missing or non-boolean 'explanationReviewed' field")
        else:
            exp_text = (q.get('explanation') or '').strip()
            if q['explanationReviewed'] and not exp_text:
                crit_errors.append(f"{filename} Q#{idx+1} ({q_id}): explanationReviewed is True but explanation is empty")
            if not q['explanationReviewed'] and exp_text:
                quality_warnings.append(f"{filename} Q#{idx+1} ({q_id}): explanationReviewed is False but explanation is non-empty")

        if q.get('type') not in ['single_choice', 'multiple_choice', 'ordering']:
            crit_errors.append(f"{filename} Q#{idx+1} ({q_id}): Unknown question type '{q.get('type')}'")

        options = q.get('options', [])
        correct = q.get('correctAnswers', [])

        if len(options) < 2:
            crit_errors.append(f"{filename} Q#{idx+1} ({q_id}): Options count ({len(options)}) < 2")

        if not correct:
            crit_errors.append(f"{filename} Q#{idx+1} ({q_id}): correctAnswers is empty")

        qtype = q.get('type')
        if qtype == 'single_choice' and len(correct) != 1:
            crit_errors.append(f"{filename} Q#{idx+1} ({q_id}): single_choice needs exactly 1 correct answer")
        if qtype == 'multiple_choice' and not (2 <= len(correct) < len(options)):
            crit_errors.append(f"{filename} Q#{idx+1} ({q_id}): multiple_choice needs 2..n-1 correct answers")
        if qtype == 'ordering' and sorted(correct) != list(range(len(options))):
            crit_errors.append(f"{filename} Q#{idx+1} ({q_id}): ordering must list every option exactly once (correctAnswers = right sequence)")

        for c in correct:
            if not isinstance(c, int) or c < 0 or c >= len(options):
                crit_errors.append(f"{filename} Q#{idx+1} ({q_id}): correctAnswers index {c} out of bounds (options len: {len(options)})")

        for o_idx, opt in enumerate(options):
            if 'text' not in opt or opt['text'] is None or opt['text'] == '':
                crit_errors.append(f"{filename} Q#{idx+1} ({q_id}) Opt#{o_idx+1}: Missing option text")
            if 'explanation' not in opt or opt['explanation'] is None:
                quality_warnings.append(f"{filename} Q#{idx+1} ({q_id}) Opt#{o_idx+1}: Missing option explanation key")

        q_text = q.get('text', '')
        if '\ufffd' in q_text:
            crit_errors.append(f"{filename} Q#{idx+1} ({q_id}): Replacement character found in text: {q_text}")
        if '<' in q_text and '>' in q_text and not re.search(r'<\/?(b|i|u|span|p)>', q_text):
            quality_warnings.append(f"{filename} Q#{idx+1} ({q_id}): Potential HTML tag in text: {q_text}")


def main():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    json_files = sorted([
        f for f in glob.glob(os.path.join(root_dir, '*.json'))
        if not f.endswith('catalog.json') and not f.endswith('1_mose_300_fragen_komplett.json')
    ])

    catalog_path = os.path.join(root_dir, 'catalog.json')
    if not os.path.exists(catalog_path):
        print("ERROR: catalog.json not found!")
        sys.exit(1)

    with open(catalog_path, 'r', encoding='utf-8') as f:
        catalog_data = json.load(f)

    cat_quizzes = catalog_data.get('quizzes', [])
    cat_urls = {q['downloadUrl']: q for q in cat_quizzes}

    crit_errors = []
    inconsistencies = []
    quality_warnings = []

    all_q_ids = {}
    de_data_by_file = {}

    print(f"Checking {len(json_files)} DE quiz JSON files against catalog ({len(cat_quizzes)} entries)...")

    for file_path in json_files:
        filename = os.path.basename(file_path)
        rel_url = f"./{filename}"

        if rel_url not in cat_urls:
            inconsistencies.append(f"{filename}: File missing from catalog downloadUrls ({rel_url})")

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            de_data_by_file[filename] = data
        except Exception as e:
            crit_errors.append(f"{filename}: Failed to parse JSON: {e}")
            continue

        meta = data.get('metadata', {})
        questions = data.get('questions', [])

        req_meta = ['quizId', 'title', 'subtitle', 'author', 'version', 'category', 'difficulty', 'tags', 'questionCount', 'canonicalBookNumber', 'testament']
        for rm in req_meta:
            if rm not in meta or meta[rm] is None or meta[rm] == '':
                inconsistencies.append(f"{filename}: Missing or empty metadata field '{rm}'")

        if meta.get('questionCount') != len(questions):
            inconsistencies.append(f"{filename}: metadata.questionCount ({meta.get('questionCount')}) != actual questions ({len(questions)})")

        if rel_url in cat_urls:
            cq = cat_urls[rel_url]
            if cq.get('questionCount') != len(questions):
                inconsistencies.append(f"{filename}: Catalog questionCount ({cq.get('questionCount')}) != actual questions ({len(questions)})")
            if cq.get('quizId') != meta.get('quizId'):
                inconsistencies.append(f"{filename}: Catalog quizId ('{cq.get('quizId')}') != metadata.quizId ('{meta.get('quizId')}')")
            real_size = os.path.getsize(file_path)
            if cq.get('sizeBytes') != real_size:
                inconsistencies.append(f"{filename}: Catalog sizeBytes ({cq.get('sizeBytes')}) != actual size ({real_size})")

        validate_question_list(filename, questions, crit_errors, inconsistencies, quality_warnings, all_q_ids)

    # Check en/ directory if present
    en_dir = os.path.join(root_dir, 'en')
    if os.path.isdir(en_dir):
        en_files = sorted([
            f for f in glob.glob(os.path.join(en_dir, '*.json'))
            if not f.endswith('catalog.json')
        ])
        en_catalog_path = os.path.join(en_dir, 'catalog.json')
        en_cat_urls = {}
        if os.path.exists(en_catalog_path):
            try:
                with open(en_catalog_path, 'r', encoding='utf-8') as f:
                    en_cat_data = json.load(f)
                en_cat_urls = {q['downloadUrl']: q for q in en_cat_data.get('quizzes', [])}
            except Exception as e:
                crit_errors.append(f"en/catalog.json: Failed to parse JSON: {e}")
        elif en_files:
            inconsistencies.append("en/catalog.json missing while en/*.json files exist")

        print(f"Checking {len(en_files)} EN quiz JSON files against DE counterparts and en/catalog.json...")
        en_q_ids = {}
        for en_path in en_files:
            filename = os.path.basename(en_path)
            en_label = f"en/{filename}"
            rel_url = f"./en/{filename}"

            if en_cat_urls and rel_url not in en_cat_urls:
                inconsistencies.append(f"{en_label}: Missing from en/catalog.json ({rel_url})")

            try:
                with open(en_path, 'r', encoding='utf-8') as f:
                    en_data = json.load(f)
            except Exception as e:
                crit_errors.append(f"{en_label}: Failed to parse JSON: {e}")
                continue

            en_meta = en_data.get('metadata', {})
            en_questions = en_data.get('questions', [])

            req_en_meta = ['quizId', 'title', 'subtitle', 'author', 'language', 'version', 'category', 'difficulty', 'tags', 'questionCount', 'canonicalBookNumber', 'testament']
            for rm in req_en_meta:
                if rm not in en_meta or en_meta[rm] is None or en_meta[rm] == '':
                    inconsistencies.append(f"{en_label}: Missing or empty metadata field '{rm}'")

            if en_meta.get('author') != 'King James Version (1769)':
                inconsistencies.append(f"{en_label}: metadata.author must be 'King James Version (1769)', got '{en_meta.get('author')}'")
            if en_meta.get('language') != 'en':
                inconsistencies.append(f"{en_label}: metadata.language must be 'en', got '{en_meta.get('language')}'")
            if not str(en_meta.get('quizId', '')).endswith('_en'):
                inconsistencies.append(f"{en_label}: metadata.quizId must end with '_en', got '{en_meta.get('quizId')}'")

            if en_meta.get('questionCount') != len(en_questions):
                inconsistencies.append(f"{en_label}: metadata.questionCount ({en_meta.get('questionCount')}) != actual questions ({len(en_questions)})")

            if rel_url in en_cat_urls:
                cq = en_cat_urls[rel_url]
                if cq.get('questionCount') != len(en_questions):
                    inconsistencies.append(f"{en_label}: en/catalog questionCount != actual questions")
                if cq.get('quizId') != en_meta.get('quizId'):
                    inconsistencies.append(f"{en_label}: en/catalog quizId != metadata.quizId")
                real_size = os.path.getsize(en_path)
                if cq.get('sizeBytes') != real_size:
                    inconsistencies.append(f"{en_label}: en/catalog sizeBytes ({cq.get('sizeBytes')}) != actual size ({real_size})")

            validate_question_list(en_label, en_questions, crit_errors, inconsistencies, quality_warnings, en_q_ids)

            # Compare with German file
            de_data = de_data_by_file.get(filename)
            if not de_data:
                crit_errors.append(f"{en_label}: No matching German file {filename}")
                continue

            de_meta = de_data.get('metadata', {})
            de_questions = de_data.get('questions', [])

            expected_en_quiz_id = f"{de_meta.get('quizId')}_en"
            if en_meta.get('quizId') != expected_en_quiz_id:
                inconsistencies.append(f"{en_label}: quizId '{en_meta.get('quizId')}' != expected '{expected_en_quiz_id}'")

            if len(en_questions) != len(de_questions):
                crit_errors.append(f"{en_label}: Question count ({len(en_questions)}) != DE question count ({len(de_questions)})")
            else:
                for idx, (dq, eq) in enumerate(zip(de_questions, en_questions)):
                    if dq.get('questionId') != eq.get('questionId'):
                        crit_errors.append(f"{en_label} Q#{idx+1}: questionId '{eq.get('questionId')}' != DE '{dq.get('questionId')}'")
                    if dq.get('type') != eq.get('type'):
                        crit_errors.append(f"{en_label} Q#{idx+1} ({eq.get('questionId')}): type '{eq.get('type')}' != DE '{dq.get('type')}'")
                    if len(dq.get('options', [])) != len(eq.get('options', [])):
                        crit_errors.append(f"{en_label} Q#{idx+1} ({eq.get('questionId')}): options len ({len(eq.get('options', []))}) != DE ({len(dq.get('options', []))})")
                    if dq.get('correctAnswers') != eq.get('correctAnswers'):
                        crit_errors.append(f"{en_label} Q#{idx+1} ({eq.get('questionId')}): correctAnswers {eq.get('correctAnswers')} != DE {dq.get('correctAnswers')}")
                    if dq.get('difficulty') != eq.get('difficulty'):
                        inconsistencies.append(f"{en_label} Q#{idx+1} ({eq.get('questionId')}): difficulty '{eq.get('difficulty')}' != DE '{dq.get('difficulty')}'")

    print("\n================ VALIDATION REPORT ================")
    print(f"🔴 Critical Errors:   {len(crit_errors)}")
    for e in crit_errors[:30]:
        print(f"  - {e}")
    if len(crit_errors) > 30:
        print(f"  ... and {len(crit_errors) - 30} more critical errors")

    print(f"🟡 Inconsistencies:   {len(inconsistencies)}")
    for e in inconsistencies[:30]:
        print(f"  - {e}")
    if len(inconsistencies) > 30:
        print(f"  ... and {len(inconsistencies) - 30} more inconsistencies")

    print(f"🟢 Quality Warnings:  {len(quality_warnings)}")
    for e in quality_warnings[:15]:
        print(f"  - {e}")
    if len(quality_warnings) > 15:
        print(f"  ... and {len(quality_warnings) - 15} more warnings")

    print("===================================================\n")

    if crit_errors or inconsistencies:
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
