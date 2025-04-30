# VTT to Markdown Converter

### Overview
This tool batch-converts WebVTT subtitle files (.vtt) in a specified folder to Markdown (.md), extracting only lines that originally contained styling tags (e.g., <c.colorE5E5E5>...</c>). All tags are stripped, duplicates are removed, and the original VTT files are deleted after conversion.

Focus: Only visually/emphasized (styled) subtitle lines are preserved.
Output: Clean, deduplicated Markdown text files for each VTT input.
No dependencies: Uses only Python standard library.

### Features
- Batch process all .vtt files in a folder
- Extracts only lines with styling tags
- Strips all tags (styling, timestamps, HTML-like)
- Removes duplicate lines
- Deletes original .vtt files after successful conversion
- Fully documented, modular, and easy to extend

###Requirements
- Python 3.7 or higher
- No third-party packages required

### Usage
Place your .vtt files in a folder.
Run the script:

``` bash
python VTT2MDconverter.py
```

Enter the path to your folder when prompted.
Converted .md files will be saved in the same folder; the original .vtt files will be deleted.

### Customization
To change which lines are extracted, adjust the styling_tag_pattern in the script.
To preserve .vtt files, comment out or remove the vtt_file.unlink() line in main().

### License
MIT License. See LICENSE file for details.

### Author
myPyAI + Naveen Srivatsav