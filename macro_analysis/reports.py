from abc import ABC, abstractmethod
from collections import defaultdict

class Report(ABC):
    @abstractmethod
    def generate(self, rows: list[dict]) -> list[list]:
        pass


class AverageGDPReport(Report):
    name = "average-gdp"
    headers = ["country", "gdp"]

    def generate(self, rows):
        gdp_by_country = defaultdict(list)

        for row in rows:
            gdp_by_country[row["country"]].append(float(row["gdp"]))

        result = []
        for country, values in gdp_by_country.items():
            avg = sum(values) / len(values)
            result.append([country, round(avg, 2)])

        result.sort(key=lambda x: x[1], reverse=True)
        return result


REPORTS = {
    AverageGDPReport.name: AverageGDPReport(),
}
