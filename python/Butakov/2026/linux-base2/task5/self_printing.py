from pathlib import Path

print(Path(__file__).read_text(encoding='utf-8'), end='')
