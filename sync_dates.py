import re
from pathlib import Path

root = Path('.')
updated = []
for path in sorted(root.rglob('_index.md')):
    if 'themes/' in str(path):
        continue
    vi_path = path.with_name('_index.vi.md')
    if not vi_path.exists():
        continue

    text_md = path.read_text(encoding='utf-8')
    text_vi = vi_path.read_text(encoding='utf-8')

    def extract_date(text):
        m = re.search(r'^date:\s*(.+)$', text, re.M)
        return m.group(1).strip() if m else None

    md_date = extract_date(text_md)
    vi_date = extract_date(text_vi)

    if md_date and vi_date and md_date != vi_date:
        new_vi = re.sub(r'^(date:\s*).+$', rf'\1{md_date}', text_vi, count=1, flags=re.M)
        vi_path.write_text(new_vi, encoding='utf-8')
        updated.append((str(vi_path), md_date))

print(f'updated_count={len(updated)}')
for item in updated:
    print(f'{item[0]} -> {item[1]}')
