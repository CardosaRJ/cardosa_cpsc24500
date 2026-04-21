"""
payroll_report.py - Week 4 Starter

PayrollReport handles all display and file output. It does not store data itself --
it gets data from the PayrollProcessor passed into its constructor.
"""


class PayrollReport:

    def __init__(self, processor):
        # TODO: store the processor
        self._processor = processor

    def display_all_employees(self):
        # TODO: print a header row, then each employee on its own line
        # Use self._processor.employees to get the list
        print("=" * 65)
        print(f"{'Name':<20} {'ID':<8} {'Rate':>8} {'Hours':>8} {'Gross Pay':>12}")
        print("=" * 65)
        for emp in self._processor.employees:
            print(emp)
        print("=" * 65)  

    def display_payroll_summary(self):
        # TODO: print total employees, total payroll, average pay,
        #       highest paid, lowest paid
        count = self._processor.get_employee_count()
        total = self._processor.calculate_total_payroll()
        avg = self._processor.calculate_average_pay()
        highest = self._processor.find_highest_paid()
        lowest = self._processor.find_lowest_paid()

        print("\n*** Summary of Payroll ***")
        print("-" * 26)
        print(f"Total employees:   {count}")
        print(f"Total payroll:     ${total:,.2f}")
        print(f"Average pay:       ${avg:,.2f}")
        if highest:
            print(f"Highest paid:      {highest.name} (${highest.calculate_gross_pay():,.2f})")
        if lowest:
            print(f"Lowest paid:       {lowest.name} (${lowest.calculate_gross_pay():,.2f})")

    def generate_report_file(self, filename):
        # TODO: write the full report (employees + summary) to a text file
        # Use a `with` block
        count = self._processor.get_employee_count()
        total = self._processor.calculate_total_payroll()
        avg = self._processor.calculate_average_pay()
        highest = self._processor.find_highest_paid()
        lowest = self._processor.find_lowest_paid()
        
        with open(filename, "w") as f:
            f.write("*" * 65 + "\n")
            f.write(" " * 25 + "Payroll Report\n")
            f.write("*" * 65 + "\n\n")
            f.write("=" * 65 + "\n")
            f.write(f"{'Name':<20} {'ID':<8} {'Rate':>8} {'Hours':>8} {'Gross Pay':>12}\n")
            f.write("=" * 65 + "\n")
            for emp in self._processor.employees:
                f.write(str(emp) + "\n")
            f.write("\n*** Summary of Payroll ***\n")
            f.write("-" * 26 + "\n")
            f.write(f"Total employees:   {count}\n")
            f.write(f"Total payroll:     ${total:,.2f}\n")
            f.write(f"Average pay:       ${avg:,.2f}\n")
            if highest:
                f.write(f"Highest paid:      {highest.name} (${highest.calculate_gross_pay():,.2f})\n")
            if lowest:
                f.write(f"Lowest paid:       {lowest.name} (${lowest.calculate_gross_pay():,.2f})\n")
        print(f"Your report has been saved to {filename}")