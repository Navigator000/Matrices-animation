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
Furthermore, matrices can be used to represent linear transformations, which are fundamental in many areas of mathematics and physics.

Let's take a look at some of them, shall we?
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

