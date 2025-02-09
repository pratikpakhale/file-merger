import argparse
from pathlib import Path
import sys
from datetime import datetime

def create_file_header(file_path: Path, relative_to: Path) -> str:
    """Create a formatted header with file metadata."""
    rel_path = file_path.relative_to(relative_to)
    return f"\n{'='*80}\n" \
           f"FILE: {rel_path}\n" \
           f"TIMESTAMP: {datetime.fromtimestamp(file_path.stat().st_mtime)}\n" \
           f"{'='*80}\n"

def merge_files(input_dir: str, pattern: str, output_file: str) -> None:
    """Merge all files matching pattern in input_dir into a single output file."""
    input_path = Path(input_dir).resolve()
    output_path = Path(output_file)
    
    if not input_path.exists():
        print(f"Error: Input directory '{input_dir}' does not exist")
        sys.exit(1)
    
    matching_files = list(input_path.rglob(pattern))
    
    if not matching_files:
        print(f"Warning: No files matching pattern '{pattern}' found in {input_dir}")
        sys.exit(0)
    
    print(f"Found {len(matching_files)} matching files")
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write(f"MERGED FILE COLLECTION\n")
        outfile.write(f"Generated on: {datetime.now()}\n")
        outfile.write(f"Source directory: {input_path}\n")
        outfile.write(f"Pattern: {pattern}\n\n")
        
        for file_path in sorted(matching_files):
            try:
                outfile.write(create_file_header(file_path, input_path))
                with open(file_path, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
                outfile.write("\n")
            except Exception as e:
                print(f"Warning: Error processing {file_path}: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Merge files matching a pattern into a single file')
    parser.add_argument('input_dir', help='Input directory to search for files')
    parser.add_argument('pattern', help='File pattern to match (e.g., "*.py", "*.txt")')
    parser.add_argument('output_file', help='Output file path')
    
    args = parser.parse_args()
    
    merge_files(args.input_dir, args.pattern, args.output_file)
    print(f"Merged files written to: {args.output_file}")

if __name__ == '__main__':
    main()
