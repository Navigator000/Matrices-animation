import json
from pathlib import Path
plaintext = """Matrices are mathematical tools that are used for various purposes, including but not limited to:
- Cryptography
- Computer Graphics
- Data Analysis
...among others.
For this animation, we'll take a look at one field in particular:
CRYPTOGRAPHY.
"""

lines = plaintext.splitlines()

indexed_lines = {str(index): line for index, line in enumerate(lines)}

data = {
    "plaintext": indexed_lines
}

json_path = Path(__file__).resolve().parent / "text.json" #cwds are more confusing than i thought

try:
    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
        print("JSON contents written")
except Exception as e:
    print(f"Error writing to {json_path}: {e}")

