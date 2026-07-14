from pathlib import Path
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

csv_dir = Path("./verbruggen/")

total_lines = 0

for csv_file in csv_dir.rglob("*.csv"):
    with open(csv_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        if len(lines) > 1:
            total_lines += len(lines) - 1  # on enlève l'entête

print(f"Nombre total de lignes (sans headers) : {total_lines}")

# Inder-Kuijken-leleux-Naha-Pahud-Pitelina-Rampal-Verbruggen
#11410+10154+.   11642+1132+ 11642+11489+11642+11489

# Porter-Kuijken-Pahud-Pitelina-Rampal-Lazarevitch
#11410+10154+11642+11489+11642+11489