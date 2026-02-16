import pytest
from employees import Employee

class TestEmployee:
    def employee(self):
        return Employee(emp_id=1, name="John Doe", salary=60000)

    def test_employee_initialization(self, employee):
        assert employee.emp_id == 1
        assert employee.name == "John Doe"
        assert employee.salary == 60000

    def test_increase_salary(self, employee):
        result = employee.increase_salary(5000)
        assert result == 65000
        assert employee.salary == 65000

    def test_increase_salary_invalid_amount(self, employee):
        with pytest.raises(ValueError, match="Amount must be positive"):
            employee.increase_salary(0)
        with pytest.raises(ValueError, match="Amount must be positive"):
            employee.increase_salary(-1000)

    def test_decrease_salary(self, employee):
        result = employee.decrease_salary(10000)
        assert result == 50000
        assert employee.salary == 50000

    def test_decrease_salary_invalid_amount(self, employee):
        with pytest.raises(ValueError, match="Amount must be positive"):
            employee.decrease_salary(0)
        with pytest.raises(ValueError, match="Amount must be positive"):
            employee.decrease_salary(-5000)

    def test_decrease_salary_exceeds_current(self, employee):
        with pytest.raises(ValueError, match="Cannot decrease more than salary"):
            employee.decrease_salary(70000)

    def test_get_annual_salary(self, employee):
        assert employee.get_annual_salary() == 720000

    def test_is_high_earner_true(self, employee):
        assert employee.is_high_earner() is True

    def test_is_high_earner_false(self):
        low_earner = Employee(emp_id=2, name="Jane Doe", salary=30000)
        assert low_earner.is_high_earner() is False

    def test_is_high_earner_boundary(self):
        boundary_earner = Employee(emp_id=3, name="Bob Smith", salary=50000)
        assert boundary_earner.is_high_earner() is True