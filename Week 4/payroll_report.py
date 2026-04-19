"""
payroll_report.py - Week 4 Starter

PayrollReport handles all display and file output. It does not store data itself --
it gets data from the PayrollProcessor passed into its constructor.
"""


class PayrollReport:

    def __init__(self, processor):
        # TODO: store the processor
        pass

    def display_all_employees(self):
        # TODO: print a header row, then each employee on its own line
        # Use self._processor.employees to get the list
        pass

    def display_payroll_summary(self):
        # TODO: print total employees, total payroll, average pay,
        #       highest paid, lowest paid
        pass

    def generate_report_file(self, filename):
        # TODO: write the full report (employees + summary) to a text file
        # Use a `with` block
        pass
