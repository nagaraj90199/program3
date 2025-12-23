import pytest
from Employee import Employee_details
def test_employee.py():
   expected_output=(
  empname="Harsha"
  empid="S109"
  salary=70000
)
assert(Employee_details("Harsha","S109",70000)==expected_output
