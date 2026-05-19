#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path
import zipfile
import shutil

if len(sys.argv) < 2:
    print("Usage: python split_mp3.py input.mp3 output_folder")
    sys.exit(1)

input_file = Path(sys.argv[1]).expanduser()
output_dir = Path("chunks")

if output_dir.exists():
    shutil.rmtree(output_dir)

output_dir.mkdir()

subprocess.run([
    "ffmpeg",
    "-i", str(input_file),
    "-map", "0:a",
    "-f", "segment",
    "-segment_time", "30",
    "-c", "copy",
    str(output_dir / "part_%03d.mp3")
], check=True)

zip_name = input_file.stem + "_chunks.zip"

with zipfile.ZipFile(zip_name, "w") as z:
    for file in sorted(output_dir.iterdir()):
        z.write(file, file.name)

print("Created:", zip_name)
