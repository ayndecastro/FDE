import unittest
from sort import sort

class TestPackageSorting(unittest.TestCase):
    # Standard packages
    def test_standard_package(self):
        self.assertEqual(sort(10, 10, 10, 5), "STANDARD")
    
    # Special packages - Bulky
    def test_bulky_by_volume(self):
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")  # 1,000,000 cm³
    
    def test_bulky_by_dimension(self):
        self.assertEqual(sort(150, 10, 10, 10), "SPECIAL")
    
    # Special packages - Heavy
    def test_heavy_package(self):
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")
    
    # Rejected packages
    def test_rejected_package(self):
        self.assertEqual(sort(150, 100, 100, 20), "REJECTED")
    
    # Invalid inputs
    def test_none_input(self):
        self.assertEqual(sort(None, 10, 10, 10), "REJECTED")
        self.assertEqual(sort(10, None, 10, 10), "REJECTED")
        self.assertEqual(sort(10, 10, None, 10), "REJECTED")
        self.assertEqual(sort(10, 10, 10, None), "REJECTED")
    
    def test_negative_input(self):
        self.assertEqual(sort(-1, 10, 10, 10), "REJECTED")
        self.assertEqual(sort(10, -1, 10, 10), "REJECTED")
        self.assertEqual(sort(10, 10, -1, 10), "REJECTED")
        self.assertEqual(sort(10, 10, 10, -1), "REJECTED")
    
    def test_non_numeric_input(self):
        self.assertEqual(sort("invalid", 10, 10, 10), "REJECTED")
        self.assertEqual(sort(10, "invalid", 10, 10), "REJECTED")
        self.assertEqual(sort(10, 10, "invalid", 10), "REJECTED")
        self.assertEqual(sort(10, 10, 10, "invalid"), "REJECTED")
    
    def test_edge_cases(self):
        # Standard package just below thresholds
        self.assertEqual(sort(149, 100, 67, 19.9), "STANDARD")
        # Special package at dimension threshold
        self.assertEqual(sort(150, 10, 10, 10), "SPECIAL")
    
    def test_floating_point_precision(self):
        # Just below bulky threshold
        self.assertEqual(sort(99.999, 100, 100, 10), "STANDARD")
        # Just above bulky threshold
        self.assertEqual(sort(100.001, 100, 100, 10), "SPECIAL")

    def test_extreme_dimensions(self):
        # Very large numbers
        self.assertEqual(sort(10000, 10000, 10000, 10000), "REJECTED")

    def test_string_number_inputs(self):
        # Test numeric strings without units
        self.assertEqual(sort("100", "100", "100", "10"), "SPECIAL")
        self.assertEqual(sort("10", "10", "10", "20"), "SPECIAL")
        
        # Test with units
        self.assertEqual(sort("100cm", "100cm", "100cm", "10kg"), "SPECIAL")
        self.assertEqual(sort("10cm", "10cm", "10cm", "20kg"), "SPECIAL")
        self.assertEqual(sort("10   cm", "10 cm", "10 cm", "20 kg"), "SPECIAL")
        # Standard case with units
        self.assertEqual(sort("100cm", "90cm", "25cm", "10kg"), "STANDARD")
        self.assertEqual(sort("100 cm", "90 cm", "25 cm", "10 kg"), "STANDARD")
        # Rejected case with units
        self.assertEqual(sort("150cm", "100cm", "100cm", "20kg"), "REJECTED")

    def test_exactly_at_thresholds(self):
        # Exactly at volume threshold
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")  # 1,000,000 cm³
        # Exactly at mass threshold
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")
        # Exactly at dimension threshold
        self.assertEqual(sort(150, 10, 10, 10), "SPECIAL")

if __name__ == '__main__':
    unittest.main()