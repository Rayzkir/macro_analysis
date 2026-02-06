from macro_analysis.reader import read_csv

def test_read_single_file(tmp_path):
    file = tmp_path / "data.csv"
    file.write_text(
        "country,year,gdp\n"
        "A,2020,10\n"
        "A,2021,20\n"
    )

    rows = read_csv([str(file)])

    assert len(rows) == 2
    assert rows[0]["country"] == "A"
    assert rows[1]["gdp"] == "20"

def test_read_multiple_files(tmp_path):
    file1 = tmp_path / "a.csv"
    file2 = tmp_path / "b.csv"

    file1.write_text("country,year,gdp\nA,2020,10\n")
    file2.write_text("country,year,gdp\nB,2021,30\n")

    rows = read_csv([str(file1), str(file2)])

    assert len(rows) == 2
    countries = {row["country"] for row in rows}
    assert countries == {"A", "B"}
