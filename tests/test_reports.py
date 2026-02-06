from macro_analysis.reports import AverageGDPReport

def test_average_gdp_basic():
    rows = [
        {"country": "A", "gdp": "10"},
        {"country": "A", "gdp": "20"},
        {"country": "B", "gdp": "30"},
    ]

    report = AverageGDPReport()
    result = report.generate(rows)

    assert result == [
        ["B", 30.0],
        ["A", 15.0],
    ]

def test_average_gdp_sorted_desc():
    rows = [
        {"country": "A", "gdp": "100"},
        {"country": "B", "gdp": "200"},
    ]

    report = AverageGDPReport()
    result = report.generate(rows)

    assert result[0][0] == "B"
