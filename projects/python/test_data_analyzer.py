import unittest

from data_analyzer import DataAnalyzer


class TestDataAnalyzer(unittest.TestCase):
    def test_mean_median_std_dev(self):
        analyzer = DataAnalyzer([10, 20, 30, 40])

        self.assertAlmostEqual(analyzer.mean(), 25.0)
        self.assertAlmostEqual(analyzer.median(), 25.0)
        self.assertAlmostEqual(analyzer.standard_deviation(), 11.1803398875, places=7)

    def test_quartiles(self):
        analyzer = DataAnalyzer([1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(analyzer.quartiles(), {"Q1": 2.75, "Q2": 4.5, "Q3": 6.25})

    def test_outliers(self):
        analyzer = DataAnalyzer([10, 12, 14, 15, 100])
        self.assertEqual(analyzer.outliers(), [100])

    def test_empty_dataset(self):
        analyzer = DataAnalyzer([])
        self.assertEqual(analyzer.mean(), 0)
        self.assertEqual(analyzer.median(), 0)
        self.assertEqual(analyzer.standard_deviation(), 0)
        self.assertEqual(analyzer.quartiles(), {"Q1": 0, "Q2": 0, "Q3": 0})
        self.assertEqual(analyzer.outliers(), [])
        self.assertEqual(
            analyzer.summary(),
            {
                "count": 0,
                "min": 0,
                "max": 0,
                "mean": 0,
                "median": 0,
                "std_dev": 0,
                "outliers_count": 0,
            },
        )


if __name__ == "__main__":
    unittest.main()
