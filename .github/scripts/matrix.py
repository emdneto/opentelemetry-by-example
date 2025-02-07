import os
import json

snippet_dir = os.environ.get("SNIPPET_DIR")

if not snippet_dir:
    print("Error: SNIPPET_DIR environment variable is required")
    exit(1)

all_snippets = os.environ.get("ALL_SNIPPETS", "false").lower()  # "true" or "false"

# The changed files environment variable should be a JSON array like: ["path/to/foo", "path/to/bar", ...]
# If it doesn't exist or is empty, default to "[]"
changed_files_str = os.environ.get("CHANGED_FILES", "[]")
#changed_files_str = os.environ.get("CHANGED_FILES", "[\"src/python\",\"src/python/hello-world\"]")
try:
    changed_files = json.loads(changed_files_str)
except json.JSONDecodeError:
    changed_files = []

# Find all directories under snippet_dir that contain the `devenv.nix`
found_snippet_dirs = []
for root, dirs, files in os.walk(snippet_dir):
    if "devenv.nix" in files:
        # 'root' is the full path from snippet_dir downward
        found_snippet_dirs.append(root)

# If ALL_SNIPPETS == "true", use all discovered snippet directories
# Otherwise, only include snippet dirs that have changed
if all_snippets == "true":
    snippet_dirs = found_snippet_dirs
else:
    snippet_dirs = []
    for sdir in found_snippet_dirs:
        # If any changed file (in changed_files) starts with this snippet directory path, consider it "changed"
        # e.g. snippet_dir = "src/dev/python/hello-world", changed_file might be "src/dev/python/hello-world/devenv.yaml"
        if any(cf.startswith(sdir) for cf in changed_files):
            snippet_dirs.append(sdir)

# Build final matrix: each snippet is { "snippet": "python:hello-world", "dir": "src/python/hello-world" }
matrix = []
for sdir in snippet_dirs:
    chunks = sdir.split("/")
    name = ":".join(chunks[1:])
    matrix.append({"name": name, "dir": sdir})

# Output the matrix in the format that GitHub Actions can parse:
# We'll print a line like `matrix=[ ...json... ]` so the step can do python matrix.py >> $GITHUB_OUTPUT
print(f"matrix={json.dumps(matrix)}")
