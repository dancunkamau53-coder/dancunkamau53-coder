"""
Data Analyzer Module
Advanced Python example demonstrating data analysis and visualization capabilities.
Features: Data processing, statistics, and pattern detection.
"""

from typing import List, Dict, Tuple
import json
from dataclasses import dataclass


@dataclass
class DataPoint:
    """Represents a single data point with metadata."""
    value: float
    label: str
    timestamp: str


class DataAnalyzer:
    """Advanced data analysis tool for statistical computations."""
    
    def __init__(self, data: List[float]):
        """
        Initialize the analyzer with data.
        
        Args:
            data: List of numerical values to analyze
        """
        self.data = data
        self.sorted_data = sorted(data)
    
    def mean(self) -> float:
        """Calculate the arithmetic mean."""
        return sum(self.data) / len(self.data) if self.data else 0
    
    def median(self) -> float:
        """Calculate the median value."""
        if not self.sorted_data:
            return 0
        n = len(self.sorted_data)
        if n % 2 == 0:
            return (self.sorted_data[n // 2 - 1] + self.sorted_data[n // 2]) / 2
        return self.sorted_data[n // 2]
    
    def standard_deviation(self) -> float:
        """Calculate the standard deviation."""
        if not self.data:
            return 0
        mean = self.mean()
        variance = sum((x - mean) ** 2 for x in self.data) / len(self.data)
        return variance ** 0.5
    
    def quartiles(self) -> Dict[str, float]:
        """Calculate Q1, Q2 (median), and Q3."""
        if not self.sorted_data:
            return {"Q1": 0, "Q2": 0, "Q3": 0}

        def percentile(p: float) -> float:
            index = (p / 100) * (len(self.sorted_data) - 1)
            lower = int(index)
            upper = lower + 1
            if upper >= len(self.sorted_data):
                return self.sorted_data[lower]
            weight = index - lower
            return self.sorted_data[lower] * (1 - weight) + self.sorted_data[upper] * weight
        
        return {
            "Q1": percentile(25),
            "Q2": percentile(50),
            "Q3": percentile(75)
        }
    
    def outliers(self, threshold: float = 1.5) -> List[float]:
        """
        Detect outliers using IQR method.
        
        Args:
            threshold: IQR multiplier for outlier detection
            
        Returns:
            List of outlier values
        """
        if not self.data:
            return []
        q = self.quartiles()
        iqr = q["Q3"] - q["Q1"]
        lower_bound = q["Q1"] - threshold * iqr
        upper_bound = q["Q3"] + threshold * iqr
        
        return [x for x in self.data if x < lower_bound or x > upper_bound]
    
    def summary(self) -> Dict[str, float]:
        """Generate comprehensive statistical summary."""
        return {
            "count": len(self.data),
            "min": min(self.data) if self.data else 0,
            "max": max(self.data) if self.data else 0,
            "mean": self.mean(),
            "median": self.median(),
            "std_dev": self.standard_deviation(),
            "outliers_count": len(self.outliers())
        }


def demo():
    """Demonstrate the DataAnalyzer functionality."""
    sample_data = [23, 45, 67, 89, 12, 34, 56, 78, 90, 100, 1000]  # Includes outlier
    
    analyzer = DataAnalyzer(sample_data)
    
    print("=" * 50)
    print("DATA ANALYSIS REPORT")
    print("=" * 50)
    print(f"Input Data: {sample_data}")
    print(f"\nStatistical Summary:")
    
    summary = analyzer.summary()
    for key, value in summary.items():
        print(f"  {key:.<20} {value:.2f}")
    
    print(f"\nQuartiles: {analyzer.quartiles()}")
    print(f"Outliers: {analyzer.outliers()}")
    print("=" * 50)


if __name__ == "__main__":
    demo()
