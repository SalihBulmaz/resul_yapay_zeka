#!/usr/bin/env python3
"""
Parser to convert kod.md file to IPython notebook (.ipynb) format.
Extracts Python code blocks and markdown content in order.
"""

import re
import json
from pathlib import Path


def parse_markdown_to_notebook(md_file_path, output_file_path=None):
    """
    Parse a markdown file and convert it to IPython notebook format.
    
    Args:
        md_file_path (str): Path to the markdown file
        output_file_path (str): Path for the output .ipynb file (optional)
    
    Returns:
        str: Path to the created notebook file
    """
    
    # Read the markdown file
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split content by Python code blocks
    # This regex matches ```python ... ``` blocks
    code_block_pattern = r'```python\s*\n(.*?)\n```'
    
    # Find all code blocks and their positions
    code_blocks = []
    for match in re.finditer(code_block_pattern, content, re.DOTALL):
        start_pos = match.start()
        end_pos = match.end()
        code_content = match.group(1).strip()
        code_blocks.append({
            'start': start_pos,
            'end': end_pos,
            'content': code_content
        })
    
    # Create notebook structure
    notebook = {
        "cells": [],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    # Process content in order
    last_end = 0
    
    for i, code_block in enumerate(code_blocks):
        # Add markdown content before this code block
        markdown_content = content[last_end:code_block['start']].strip()
        if markdown_content:
            notebook["cells"].append({
                "cell_type": "markdown",
                "metadata": {},
                "source": markdown_content
            })
        
        # Add the code block
        notebook["cells"].append({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": code_block['content']
        })
        
        last_end = code_block['end']
    
    # Add any remaining markdown content after the last code block
    remaining_content = content[last_end:].strip()
    if remaining_content:
        notebook["cells"].append({
            "cell_type": "markdown",
            "metadata": {},
            "source": remaining_content
        })
    
    # If no code blocks were found, treat the entire content as markdown
    if not code_blocks:
        notebook["cells"].append({
            "cell_type": "markdown",
            "metadata": {},
            "source": content
        })
    
    # Determine output file path
    if output_file_path is None:
        md_path = Path(md_file_path)
        output_file_path = md_path.with_suffix('.ipynb')
    
    # Write the notebook file
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Successfully converted '{md_file_path}' to '{output_file_path}'")
    print(f"📊 Created {len(notebook['cells'])} cells")
    
    # Count cell types
    markdown_cells = sum(1 for cell in notebook['cells'] if cell['cell_type'] == 'markdown')
    code_cells = sum(1 for cell in notebook['cells'] if cell['cell_type'] == 'code')
    
    print(f"   - {markdown_cells} markdown cells")
    print(f"   - {code_cells} code cells")
    
    return str(output_file_path)


def main():
    """Main function to run the parser."""
    md_file = "kod.md"
    
    if not Path(md_file).exists():
        print(f"❌ Error: '{md_file}' file not found!")
        return
    
    try:
        output_file = parse_markdown_to_notebook(md_file)
        print(f"\n🎉 Conversion completed! You can now open '{output_file}' in Jupyter Notebook or VS Code.")
    except Exception as e:
        print(f"❌ Error during conversion: {e}")


if __name__ == "__main__":
    main()
