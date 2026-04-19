"""
employee.py - Week 4 Starter

The Employee class uses encapsulation: every attribute is a property with a setter
that validates the value before storing it.

Attributes (all properties with setters):
- name (str): cannot be empty; strip whitespace
- employee_id (str): cannot be empty; strip whitespace
- hourly_rate (float): cannot be negative
- hours_worked (float): cannot be negative; cannot exceed 168

Methods:
- calculate_gross_pay(): regular pay for first 40 hours, 1.5x overtime above 40
- __str__: formatted string with name, ID, rate, hours, gross pay

IMPORTANT: __init__ must assign through the setters (self.name = name),
not directly to self._name. This ensures validation runs at construction time.
"""


class Employee:

    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        # TODO: assign through the setters so validation runs
        # self.name = name
        # self.employee_id = employee_id
        # ...
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # TODO: strip whitespace
        # TODO: raise ValueError if empty
        # TODO: store in self._name
        pass

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        # TODO: strip and validate non-empty
        pass

    @property
    def hourly_rate(self):
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, value):
        # TODO: raise ValueError if negative
        pass

    @property
    def hours_worked(self):
        return self._hours_worked

    @hours_worked.setter
    def hours_worked(self, value):
        # TODO: raise ValueError if negative or > 168
        pass

    def calculate_gross_pay(self):
        # TODO: regular pay = min(hours, 40) * rate
        # TODO: overtime pay = max(hours - 40, 0) * rate * 1.5
        # TODO: return total
        pass

    def __str__(self):
        # TODO: return a formatted line with name, ID, rate, hours, gross pay
        pass
