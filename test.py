"""
tests for calc app
"""
import calculator


class TestCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(2, 3)
        
    def test_subtract(self):
        assert 5 == calculator.subtract(10, 5)

    def test_divide(self):
        assert 2 == calculator.divide(10, 5)
    
    def test_multiply(self):
        assert 50 == calculator.divide(10, 5)
    