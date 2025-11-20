import glob
import os
import re

import nbformat

# Match %%writefile Something.java
writefile_pattern = re.compile(r"^%%writefile\s+([^\s]+\.java)", re.IGNORECASE)


java_fence_pattern = re.compile(r"```java\s*(.*?)```", re.DOTALL | re.IGNORECASE)

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
        # CASE 1 — Code cell with %%writefile (unchanged)
        if cell.cell_type == "code":
            source_lines = cell.source.splitlines()
            stripped_lines = [ln.strip() for ln in source_lines if ln.strip()]
            if stripped_lines:
                first_line = stripped_lines[0]
                writefile_match = writefile_pattern.match(first_line)

                if writefile_match:
                    java_filename = writefile_match.group(1)
                    content_lines = source_lines[1:]  # drop %%writefile
                    java_content = "\n".join(content_lines) + "\n"
                else:
                    continue

                # write the file (same as before)
                base_name, ext = os.path.splitext(java_filename)
                output_path = os.path.join(output_dir, java_filename)
                counter = 1
                while os.path.exists(output_path):
                    output_path = os.path.join(
                        output_dir, f"{base_name}_{counter}{ext}"
                    )
                    counter += 1

                header_comment = f"// Extracted from {os.path.basename(nb_file)}, cell {cell_index}\n"
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(header_comment + java_content)

                print(f"  Saved: {output_path}")
                continue

        # CASE 2 — Markdown cell with ```java fenced block AND a public class inside
        if cell.cell_type == "markdown":
            # Find all ```java ... ``` fenced blocks
            matches = java_fence_pattern.findall(cell.source)
            if not matches:
                continue

            for block_index, java_block in enumerate(matches):
                # Check for a public class declaration inside the fenced block
                if "public class" not in java_block:
                    continue

                clean_block = java_block.strip() + "\n"

                # Auto-generate filename
                java_filename = f"NotebookCell_{cell_index}_{block_index}.java"
                base_name, ext = os.path.splitext(java_filename)
                output_path = os.path.join(output_dir, java_filename)

                # Deduplicate filename
                counter = 1
                while os.path.exists(output_path):
                    output_path = os.path.join(output_dir, f"{base_name}_{counter}{ext}")
                    counter += 1

                # Write file with header comment
                header_comment = (
                    f"// Extracted from {os.path.basename(nb_file)}, "
                    f"markdown cell {cell_index}\n"
                )

                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(header_comment + clean_block)

                print(f"  Saved: {output_path}")

print("Done extracting Java files.")
