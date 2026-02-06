import pytest
from macro_analysis.main import run

def test_invalid_report(monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["prog", "--files", "file.csv", "--report", "unknown"]
    )

    with pytest.raises(SystemExit):
        run()
