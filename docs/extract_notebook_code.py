import json

notebook_path = 'D:/Coding/Manu_Jackson-main/Manu_Jackson-main/jackson_vs_ginobili_analysis.ipynb'
output_path = 'D:/Coding/Manu_Jackson-main/Manu_Jackson-main/notebook_code.py'

try:
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    code_content = ""
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code':
            source = "".join(cell['source'])
            code_content += f"\n# --- Cell {i} ---\n{source}\n"

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(code_content)

    print(f"Code extracted to {output_path}")
except Exception as e:
    print(f"Error: {e}")
