"""
main.py - Week 4 Starter

Loads employees from employees.txt, then runs a menu loop.
"""

from payroll_processor import PayrollProcessor
from payroll_report import PayrollReport

import os
print("Current folder:", os.getcwd())
print("Files found:", os.listdir('.'))

def main():
    # TODO: create a PayrollProcessor
    # TODO: call load_from_file("employees.txt")
    # TODO: create a PayrollReport with the processor

    # TODO: loop showing a menu:
    #   1. View all employees
    #   2. View payroll summary
    #   3. Generate report file
    #   4. Quit
    print("-" * 45)
    print( "|" + " " * 9 + "Payroll Management System" + " " * 9 + "|")
    print("-" * 45)

    processor = PayrollProcessor()
    processor.load_from_file("employees.txt")

    report = PayrollReport(processor)

    while True:
        print("\n(1) View all employees")
        print("(2) View payroll summary")
        print("(3) Generate report file")
        print("(4) Quit")
        choice = input("\nSelect the option you need: ").strip()

        if choice == "1":
            report.display_all_employees()
        elif choice == "2":
            report.display_payroll_summary()
        elif choice == "3":
            report.generate_report_file("report_file.txt")
        elif choice == "4":
            print("Thank you, come back again!")
            break
        else:
            print("That is not a valid option. Please try again.")

if __name__ == "__main__":
    main()
