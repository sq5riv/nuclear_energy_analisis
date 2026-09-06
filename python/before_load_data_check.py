import csv
import logging
import re
from pathlib import Path

def get_file_pairs(data_dir: str, logger: logging.Logger) -> list[tuple[Path, Path]]:
    """Find CSV files and their corresponding README.md files."""

    pairs = []
    logger.info(f"Finding CSV files in {data_dir}")
    for csv_path in Path(data_dir).glob("*.csv"):
        md_path = Path(f"{data_dir}/README_{csv_path.stem}.md")
        txt_path = Path(f"{data_dir}/README_{csv_path.stem}.txt")

        if md_path.exists():
            pairs.append((csv_path, md_path))
        elif txt_path.exists():
            pairs.append((csv_path, txt_path))
        else:
            logger.info(f"Skipping {csv_path}")

    return pairs

def get_csv_columns(csv_path: Path) -> list[str]:
    """Return column names from CSV."""
    with csv_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)
        return next(reader)

def get_documented_file(md_path: Path) -> str | None:
    """Return CSV filename declared in MD."""
    content = md_path.read_text(encoding="utf-8")

    match = re.search(
        r"\*\*Corresponding file:\*\*\s*`([^`]+)`",
        content
    )

    return match.group(1) if match else None

def colum_check(data_dir: str, logger: logging.Logger):
    """Check if all columns are present."""
    logger.info(f"Checking {data_dir} for columns")
    #get_csv_columns(Path(data_dir))
    print(get_file_pairs(data_dir, logger))