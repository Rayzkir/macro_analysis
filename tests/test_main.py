from macro_analysis.main import run_report

def test_print_report_output(tmp_path, capsys):
    file = tmp_path / "data.csv"
    file.write_text(
        "country,year,gdp\n"
        "A,2020,10\n"
        "A,2021,20\n"
    )

    run_report([str(file)], "average-gdp")

    captured = capsys.readouterr().out

    assert "A" in captured
    assert "15.0" in captured
