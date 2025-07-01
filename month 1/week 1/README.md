# Markdown to IPython Notebook Parser

This parser converts markdown files containing Python code blocks to IPython notebook (.ipynb) format.

## Features

- ✅ Converts markdown content to markdown cells
- ✅ Extracts Python code blocks (```python ... ```) to code cells
- ✅ Maintains the original order of content
- ✅ Preserves Turkish characters and special formatting
- ✅ Generates valid IPython notebook JSON format

## Usage

### Basic Usage

```bash
python parser.py
```

This will convert `kod.md` to `kod.ipynb` in the same directory.

### Programmatic Usage

```python
from parser import parse_markdown_to_notebook

# Convert a markdown file to notebook
output_file = parse_markdown_to_notebook('input.md', 'output.ipynb')
```

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Output

The parser creates a valid IPython notebook with:
- **Markdown cells**: All non-code content from the markdown file
- **Code cells**: All Python code blocks (```python ... ```)
- **Metadata**: Proper notebook metadata for Python 3 kernel

## Example

Input (`kod.md`):
```markdown
# Title

Some markdown content.

```python
import pandas as pd
print("Hello World")
```

More markdown content.
```

Output (`kod.ipynb`):
- Cell 0 (markdown): "# Title\n\nSome markdown content.\n\n"
- Cell 1 (code): "import pandas as pd\nprint(\"Hello World\")"
- Cell 2 (markdown): "More markdown content."

## Files

- `parser.py` - Main parser script
- `kod.md` - Input markdown file (Pandas tutorial)
- `kod.ipynb` - Generated IPython notebook
- `README.md` - This documentation

## Success!

The parser successfully converted `kod.md` to `kod.ipynb` with:
- 53 total cells
- 27 markdown cells  
- 26 code cells

You can now open `kod.ipynb` in Jupyter Notebook, VS Code, or any other IPython notebook viewer. 