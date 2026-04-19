"""
payroll_processor.py - Week 4 Starter

The PayrollProcessor manages a list of Employee objects and computes statistics.

Notes:
- self._employees should be private
- The `employees` property returns a COPY of the internal list (use list(self._employees))
- load_from_file() reads tab-delimited lines: name<TAB>id<TAB>rate<TAB>hours
- Skip blank lines and lines with the wrong number of fields (print a warning)
- Catch ValueError from the Employee constructor and print a warning
- Catch FileNotFoundError if the file doesn't exist
"""

from employee import Employee


class PayrollProcessor:

    def __init__(self):
        # TODO: initialize self._employees as an empty list
        pass

    @property
    def employees(self):
        # TODO: return a COPY of the list, not the original
        pass

    def load_from_file(self, filename):
        # TODO: open the file in a try/except for FileNotFoundError
        # TODO: for each line:
        #   - strip whitespace; skip blank lines
        #   - split on tab; if not exactly 4 fields, print a warning and continue
        #   - try to create an Employee; catch ValueError and print a warning
        #   - append to self._employees on success
        pass

    def calculate_total_payroll(self):
        # TODO: return the sum of gross pay across all employees
        pass

    def find_highest_paid(self):
        # TODO: return the Employee with the highest gross pay (or None if empty)
        pass

    def find_lowest_paid(self):
        # TODO: return the Employee with the lowest gross pay (or None if empty)
        pass

    def get_employee_count(self):
        # TODO
        pass

    def calculate_average_pay(self):
        # TODO: return total / count, or 0.0 if empty
        pass
