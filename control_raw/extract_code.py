import json
import random
from pathlib import Path
import os

def extract_samples():
    """
    Processes .jsonl files in the '_original_data' directory to extract code samples.

    For each .jsonl file, it randomly selects up to 1000 lines, extracts the
    'original_string' from each, and saves it to a new file. The output
    file is named based on the language and the original line number, and
    saved in a directory corresponding to the language.
    """
    input_dir = Path("_original_data")
    output_dir = Path(".")
    
    # Ensure the main output directory exists
    output_dir.mkdir(exist_ok=True)

    lang_ext_map = {
        "java": ".java",
        "javascript": ".js",
        "python": ".py",
        "ruby": ".rb",
    }

    lang_dir_map = {
        "javascript": "js",
    }
    
    num_samples = 1000

    jsonl_files = list(input_dir.glob("*.jsonl"))
    if not jsonl_files:
        print(f"No .jsonl files found in {input_dir}")
        return

    print(f"Found files: {[f.name for f in jsonl_files]}")

    for jsonl_file in jsonl_files:
        lang_name = jsonl_file.stem.split('_')[0]
        if lang_name not in lang_ext_map:
            print(f"Skipping {jsonl_file.name}, unknown language.")
            continue

        print(f"Processing {jsonl_file.name} for language '{lang_name}'...")
        
        output_lang_dir = lang_dir_map.get(lang_name, lang_name)
        lang_output_dir = output_dir / output_lang_dir
        lang_output_dir.mkdir(exist_ok=True)

        try:
            with open(jsonl_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            num_lines = len(lines)
            sample_size = min(num_samples, num_lines)
            
            # Create a list of (index, line) tuples and sample from it
            indexed_lines = list(enumerate(lines))
            sampled_indexed_lines = random.sample(indexed_lines, sample_size)

            for i, line in sampled_indexed_lines:
                line_num = i + 1  # 1-indexed line number
                try:
                    data = json.loads(line)
                    original_string = data.get("original_string")

                    if original_string:
                        ext = lang_ext_map[lang_name]
                        output_filename = f"{line_num}{ext}"
                        output_path = lang_output_dir / output_filename
                        
                        with open(output_path, 'w', encoding='utf-8') as out_f:
                            out_f.write(original_string)

                except json.JSONDecodeError:
                    print(f"Warning: Could not decode JSON on line {line_num} in {jsonl_file.name}")
                    continue
        
        except FileNotFoundError:
            print(f"Error: File not found {jsonl_file.name}")
            continue

    print("\nExtraction complete.")
    print(f"Extracted files are saved in '{output_dir}' directory.")

if __name__ == "__main__":
    extract_samples()
