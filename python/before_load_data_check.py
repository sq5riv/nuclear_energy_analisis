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
        names = [normalize_column_name(name) for name in next(reader)]
        return names

def get_documented_file(md_txt_path: Path) -> str | None:
    """Return CSV filename declared in MD."""
    content = md_txt_path.read_text(encoding="utf-8")

    match = re.findall(
        r"(?:^|[-|\|])\s*`([^`]+?)(?<!\.csv)(?<!\.txt)(?<!\.pdf)(?<!\ )`",
        content
    )
    match = [normalize_column_name(m) for m in match]
    return list(set(match)) if match else None

def normalize_column_name(name: str) -> str:
    name = re.sub(r"drililng", "drilling", name).strip()
    return re.sub(r"\s+", " ", name).strip()

def names_chceck(doc_cols: list, data_cols: list) -> bool:
    """Return True if all column names match."""
    return set(data_cols) == set(doc_cols)

def colum_check(data_dir: str, logger: logging.Logger):
    """Check if all columns are present."""
    logger.info(f"Checking {data_dir} for columns")

    for csv_path, doc_path in get_file_pairs(data_dir, logger):

        data_cols = get_csv_columns(Path(csv_path))
        doc_cols = get_documented_file(Path(doc_path))
        if data_cols is None or doc_cols is None:
            logger.info(f"There is wrong data in {csv_path} or {doc_path} file")
        if not names_chceck(doc_cols, data_cols):
            print(f'{doc_cols=}, {data_cols=}')
            print(f'{set(doc_cols)- set(data_cols)}')
            print(f'{set(data_cols)- set(doc_cols)}')
        print(f'{names_chceck(doc_cols, data_cols)}, {csv_path=}')
