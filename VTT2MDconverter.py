########### PYTHON
# Script Title: VTT Styled Lines to Markdown Converter
# Script Description: Converts all .vtt (WebVTT subtitle) files in a user-specified folder to Markdown, extracting only lines that originally contained styling tags, stripping all tags, removing duplicates, and deleting the originals after conversion. Fully documented and modular per project standards.
# Script Author: myPyAI + Naveen Srivatsav
# Last Updated: 20250430
# """tla ---- MODULE vtt2md_styled ---- EXTENDS Sequences, Strings VARIABLES vtt_files, md_files, folder Init == 
#   \E f \in Folder :: vtt_files = ScanVTT(f) /\ md_files = <<>> Next == 
#   \E v \in vtt_files :: md_files' = md_files \o <<ConvertStyled(v)>> /\ vtt_files' = vtt_files \ {v} Success == 
#   vtt_files = {} /\ \A m \in md_files : IsMarkdown(m) ----"""
###########

# Standard library only. No third-party dependencies required.
from pathlib import Path
import re

def extract_styled_lines_to_markdown(vtt_file_path: Path) -> str:
    """
    Big-picture: Extracts only lines containing styling tags from a .vtt subtitle file, strips all tags, removes duplicates, and outputs Markdown text.
    Inputs:  vtt_file_path (Path) — Path to the .vtt file to convert.
    Outputs: markdown_content (str) — Subtitle text in Markdown format, only from styled lines.
    Role: Focuses on visually/emphasized content, ensuring output is concise and free of metadata or duplicate lines.
    """
    text = vtt_file_path.read_text(encoding='utf-8')
    lines = text.splitlines()
    md_lines = []
    seen = set()
    styling_tag_pattern = re.compile(r"<c(?:\.[^>]*)?>.*?</c>")
    remove_tags_pattern = re.compile(r"<[^>]+>")
    for raw_line in lines:
        if not styling_tag_pattern.search(raw_line):
            continue
        clean = remove_tags_pattern.sub('', raw_line).strip()
        if not clean:
            continue
        if clean in seen:
            continue
        seen.add(clean)
        md_lines.append(clean)
    return "\n\n".join(md_lines)

def main():
    """
    Big-picture:
    1. Prompt user for the folder containing .vtt files.
    2. Validate the folder path, scan for .vtt files.
    3. For each .vtt file, extract only styled lines, strip tags, remove duplicates, and save as .md.
    4. Delete the original .vtt file after successful conversion.
    Rationale: Modularizes the workflow for clarity, testability, and future extension (e.g., custom tag filters, logging).
    """
    folder_input = input("Enter path to folder containing .vtt files: ").strip()
    folder_path = Path(folder_input)
    if not folder_path.is_dir():
        print(f"Error: '{folder_input}' is not a valid directory.")
        return
    vtt_files = list(folder_path.glob('*.vtt'))
    if not vtt_files:
        print("No .vtt files found in the specified folder.")
        return
    for vtt_file in vtt_files:
        try:
            print(f"Processing '{vtt_file.name}'...")
            md_content = extract_styled_lines_to_markdown(vtt_file)
            md_file = vtt_file.with_suffix('.md')
            md_file.write_text(md_content, encoding='utf-8')
            vtt_file.unlink()
            print(f"Saved '{md_file.name}' and deleted '{vtt_file.name}'.")
        except Exception as error:
            print(f"Failed to process '{vtt_file.name}': {error}")
    print("Conversion complete.")

if __name__ == "__main__":
    main()
