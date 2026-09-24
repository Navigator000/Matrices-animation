import json
from pathlib import Path
plaintext = """Matrices are mathematical tools that are used for various purposes, including but not limited to:
- Cryptography
- Computer Graphics
- Data Analysis
- Machine Learning
- Scientific Computing
..and more.

Matrices can be represented in various forms, such as 2D arrays, 3D arrays, and higher-dimensional arrays.
They can also be manipulated using various mathematical operations, such as addition, subtraction, multiplication, and inversion.
Finally...
"""

data = {
    "plaintext": plaintext
}

json_path = Path(__file__).resolve().parent / "text.json" #cwds are more confusing than i thought

with open(json_path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)
