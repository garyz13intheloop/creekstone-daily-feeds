"""Backfill daily markdown + structured data for a date range.

This script calls existing per-source scripts with the right env vars so that
both the markdown file names and structured outputs are stamped with the target
date.

Usage:
  python scripts/backfill_range.py 2026-02-16 2026-02-23

Notes:
- Requires .env (OPENAI_API_KEY, PRODUCTHUNT_DEVELOPER_TOKEN, etc.) or equivalent env vars.
- GitHub Trending data is inherently point-in-time; backfills reproduce using *today's*
  GitHub Trending page, just stamped to the target date. If you want reproducible
  historical trending, you need an archive source.
"""

from __future__ import annotations

import os
import subprocess
import sys
from datetime import datetime, timedelta


def _dates(start: str, end: str):
    s = datetime.strptime(start, "%Y-%m-%d").date()
    e = datetime.strptime(end, "%Y-%m-%d").date()
    if e < s:
        raise ValueError("end < start")
    cur = s
    while cur <= e:
        yield cur.strftime("%Y-%m-%d")
        cur = cur + timedelta(days=1)


# 每个脚本最多跑 12 分钟，防止真卡死时无限等待
_SCRIPT_TIMEOUT = int(os.getenv("BACKFILL_SCRIPT_TIMEOUT", "1800"))


def _run(cmd: list[str], env: dict[str, str]):
    print("\n$", " ".join(cmd))
    try:
        subprocess.run(cmd, env=env, check=True, timeout=_SCRIPT_TIMEOUT)
    except subprocess.TimeoutExpired:
        print(f"⚠️  超时 ({_SCRIPT_TIMEOUT}s)，跳过: {' '.join(cmd)}")
    except subprocess.CalledProcessError as e:
        print(f"⚠️  脚本退出码 {e.returncode}，继续下一个来源: {' '.join(cmd)}")


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python scripts/backfill_range.py <start YYYY-MM-DD> <end YYYY-MM-DD>")
        return 2

    start, end = sys.argv[1], sys.argv[2]

    base_env = dict(os.environ)

    for d in _dates(start, end):
        env = dict(base_env)

        # Product Hunt: fetch same day window and stamp outputs with that date.
        env["PRODUCTHUNT_FETCH_DATE"] = d
        env["PRODUCTHUNT_OUTPUT_DATE"] = d

        # arXiv: fix window end and stamp outputs with that date.
        env["ARXIV_TARGET_DATE"] = d
        env["ARXIV_OUTPUT_DATE"] = d

        # GitHub: stamp outputs with that date.
        env["GITHUB_TARGET_DATE"] = d

        # ClawHub: filter/update window and stamp outputs with that date.
        env["CLAWHUB_TARGET_DATE"] = d
        env["CLAWHUB_OUTPUT_DATE"] = d

        _run([sys.executable, "scripts/product_hunt_list_to_md.py"], env)
        _run([sys.executable, "scripts/arxiv_papers_to_md.py"], env)
        _run([sys.executable, "scripts/github_trending_to_md.py"], env)
        _run([sys.executable, "scripts/clawhub_skills_to_md.py"], env)

    # refresh insights + columns after backfill
    _run([sys.executable, "scripts/keyword_trends.py"], base_env)
    _run([sys.executable, "scripts/generate_columns.py"], base_env)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
