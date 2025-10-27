import re
import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    cleaned = re.sub(r'<[^>]*>', '', html)

    lines = [line.strip() for line in cleaned.splitlines() if line.strip()]

    with codecs.open(result_file, 'w', 'utf-8') as f:
        f.write('\n'.join(lines))