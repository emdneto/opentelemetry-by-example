import json
import sys
import logging
import re
from re import compile as re_compile

logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger(__name__)

LANGUAGE_PROCESSORS = {
    'python': lambda pkg: f"pip install {pkg}",
    'node': lambda pkg: f"npm install {pkg}",
    'javascript': lambda pkg: f"npm install {pkg}",
    'go': lambda pkg: f"go get {pkg}"
}

def process_packages(language, packages):
    if language not in LANGUAGE_PROCESSORS:
        return packages

    processor = LANGUAGE_PROCESSORS[language]
    return [processor(pkg) for pkg in packages]

def process_content(content):
    pattern = re.compile(
        r"```(?P<language>\w+),install_deps\s*\n(?P<packages>[\s\S]+?)```",
        re.DOTALL
    )
    match = pattern.search(content)

    if not match:
        return content

    language, package_block = match.groups()
    packages = [pkg.strip() for pkg in package_block.splitlines() if pkg.strip()]
    processed_packages = process_packages(language, packages)

    updated_block = f"```{language}\n" + "\n".join(processed_packages) + "\n```"

    before = content[:match.start()]
    after = content[match.end():]
    new_content = before + updated_block + after

    return new_content

def recursive_process(chapter):
    content = chapter.get("content", "")
    chapter["content"] = process_content(content)

    # If the chapter has sub-items, recursively process each one.
    for sub_item in chapter.get("sub_items", []):
        # Process the content of the sub-item (which is also a chapter)
        recursive_process(sub_item.get("Chapter"))

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "supports":
        sys.exit(0)

    context, book = json.load(sys.stdin)

    sections = book.get('sections', [])
    for section in sections:
        if not isinstance(section, dict):
            continue

        recursive_process(section["Chapter"])

    # Output the modified book
    print(json.dumps(book))
