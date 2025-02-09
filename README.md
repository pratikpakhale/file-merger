# File Merger CLI

A command-line tool that merges multiple files matching a pattern into a single output file while preserving directory structure information. Perfect for preparing codebases for LLM analysis or creating consolidated documentation.

## Features

- 📁 Recursive directory scanning
- 🔍 Pattern-based file matching
- 🗺️ Preserves original directory structure information
- 📝 Includes file metadata (paths and timestamps)
- 🔒 Secure file handling
- 🐍 Cross-platform compatibility

## Installation

```bash
# Clone the repository
pip install git+https://github.com/pratikpakhale/file-merger
```
## Usage

Basic command structure:
```bash
merge-files <input_directory> <file_pattern> <output_file>
```

Examples:
```bash
# Merge all Python files
merge-files ./src "*.py" merged_code.txt

# Merge all markdown files
merge-files ./docs "*.md" documentation.txt

# Merge specific file types
merge-files ./project "*.{js,ts}" typescript_code.txt
```

## Output Format

The merged file includes:
- Collection metadata header
- For each file:
  - Original relative path
  - File modification timestamp
  - File contents
- Clear separators between files

Example output:
```javascript
MERGED FILE COLLECTION
Generated on: 2025-02-09 01:53:00
Source directory: /absolute/path/to/input
Pattern: *.py

================================================================================
FILE: src/module/file1.py
TIMESTAMP: 2025-02-09 01:52:00
================================================================================
[file contents here]

================================================================================
FILE: src/module/file2.py
TIMESTAMP: 2025-02-09 01:52:30
================================================================================
[file contents here]
```

## Requirements

- Python 3.6 or higher
- No additional dependencies required

## Security

- Safe path handling to prevent path traversal
- UTF-8 encoding for file operations
- No shell command execution
- Proper error handling for file operations

## Development

To contribute to this project:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Project Structure

```javascript
file_merger/
├── setup.py
├── file_merger/
│   ├── __init__.py
│   └── cli.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgments

Built with Python's standard library
Inspired by the need to prepare code for LLM analysis

Code entirely written by Sonnet 3.5 (except for this line)