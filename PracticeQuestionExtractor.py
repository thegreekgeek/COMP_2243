import glob
import os
import re

import nbformat

# Match %%writefile Something.java
writefile_pattern = re.compile(r"^%%writefile\s+([^\s]+\.java)", re.IGNORECASE)

# Get directory of this script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Folder containing notebooks (sibling folder)
notebook_dir = os.path.join(script_dir, "programming_problem_solving")

# Output base directory (alongside the notebooks)
base_output_dir = os.path.join(script_dir, "extracted_java")
os.makedirs(base_output_dir, exist_ok=True)

# Find all notebooks in programming_problem_solving/
notebook_files = glob.glob(os.path.join(notebook_dir, "*.ipynb"))

for nb_file in notebook_files:
    nb = nbformat.read(nb_file, as_version=4)
    notebook_name = os.path.splitext(os.path.basename(nb_file))[0]

    # Folder for this notebook’s Java files
    output_dir = os.path.join(base_output_dir, notebook_name)
    os.makedirs(output_dir, exist_ok=True)

    print(f"Processing {nb_file}...")

    for cell_index, cell in enumerate(nb.cells):
        if cell.cell_type != "code":
            continue

        source_lines = cell.source.strip().splitlines()
        if not source_lines:
            continue

        match = writefile_pattern.match(source_lines[0])
        if not match:
            continue

        java_filename = match.group(1)
        java_content = "\n".join(source_lines[1:]) + "\n"

        base_name, ext = os.path.splitext(java_filename)
        output_path = os.path.join(output_dir, java_filename)

        # Handle duplicate filenames
        counter = 1
        while os.path.exists(output_path):
            output_path = os.path.join(output_dir, f"{base_name}_{counter}{ext}")
            counter += 1

        # Add comment header showing notebook and cell index
        header_comment = (
            f"// Extracted from {os.path.basename(nb_file)}, cell {cell_index}\n"
        )
        full_content = header_comment + java_content

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(full_content)

        print(f"  Saved: {output_path}")

print("Done extracting Java files.")
