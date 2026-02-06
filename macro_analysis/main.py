from macro_analysis.reader import read_csv
from macro_analysis.reports import REPORTS
from tabulate import tabulate
import argparse
import sys

def run_report(files: list[str], report_name: str)-> None:
    rows = read_csv(files)
    report = REPORTS[report_name]
    
    table = report.generate(rows)
    print(tabulate(table, headers=report.headers, tablefmt="github", showindex=range(1,len(table)+1), floatfmt=".2f"))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="+", required=True)
    parser.add_argument("--report", required=True)
    return parser.parse_args()


def run():
    args = parse_args()
    if not args.report in REPORTS:
        available = ", ".join(REPORTS.keys())
        print(f"Invalid report: {args.report}. Available reports: {available}")
        sys.exit(1)
    run_report(args.files, args.report)


if __name__ == "__main__":
    run()
