# Project/agent/tools.py
import pathlib
import subprocess
from typing import Tuple

from langchain_core.tools import tool


PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
GENERATED_ROOT = PROJECT_ROOT / "generated_project"


def safe_path_for_project(path: str) -> pathlib.Path:
    p = (GENERATED_ROOT / path).resolve()
    try:
        p.relative_to(GENERATED_ROOT.resolve())
    except ValueError:
        raise ValueError("Attempt to write outside project root")

    return p


@tool
def write_file(path: str, content: str) -> str:
    p = safe_path_for_project(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    return f"WROTE:{p}"


@tool
def read_file(path: str) -> str:
    p = safe_path_for_project(path)
    if not p.exists() or not p.is_file():
        return ""
    with open(p, "r", encoding="utf-8") as f:
        return f.read()


@tool
def get_current_directory() -> str:
    return str(GENERATED_ROOT)


@tool
def list_files(directory: str = ".") -> str:
    p = safe_path_for_project(directory)
    if not p.exists():
        return "No files found."
    if not p.is_dir():
        return f"ERROR: {p} is not a directory"
    files = [str(f.relative_to(GENERATED_ROOT)) for f in p.rglob("*") if f.is_file()]
    return "\n".join(files) if files else "No files found."


@tool
def run_cmd(cmd: str, cwd: str = None, timeout: int = 30) -> Tuple[int, str, str]:
    cwd_dir = safe_path_for_project(cwd) if cwd else GENERATED_ROOT
    res = subprocess.run(
        cmd,
        shell=True,
        cwd=str(cwd_dir),
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    return res.returncode, res.stdout, res.stderr


def init_project_root() -> str:
    GENERATED_ROOT.mkdir(parents=True, exist_ok=True)
    return str(GENERATED_ROOT)
