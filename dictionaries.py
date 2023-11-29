"""
Course Management System:

This script provides a simple course management system implemented in Python.
It allows for the addition, removal, and checking of courses in a dictionary-based data structure.
"""
## Needed for type hints
from typing import Dict

# Reminder: you may remove the "pass" statements from the functions below once you implement them


def display_course_names(course_info: Dict[str, str]) -> None:
    """Display the names of all available courses."""
    print("\nAvailable Courses:")
    # TODO: Iterate through the course_info dictionary and print the course code and name for each course
    pass


def add_course(course_info: Dict[str, str]) -> None:
    """Add a new course to the course_info dictionary."""
    # TODO: Prompt the user for a course code and name, then add the course to the course_info dictionary
    # The course code should be converted to uppercase before being added to the dictionary
    pass


def remove_course(course_info: Dict[str, str]) -> None:
    """Remove an existing course from the course_info dictionary."""
    # TODO: Prompt the user for a course code to remove, then remove the course from the course_info dictionary
    # Python dictionary keys are case-sensitive, so the course code should be converted to uppercase before being removed
    # You must also make sure the course code exists in the dictionary before attempting to remove it.
    pass


def check_course_existence(course_info: Dict[str, str]) -> None:
    """Check if a course exists in the course_info dictionary."""
    # TODO: Prompt the user for a course code to check, then check if the course exists in the course_info dictionary
    # Again, the course code should be converted to uppercase before being checked
    pass


def main() -> None:
    """Main program loop."""

    # TODO: Initialize an empty dictionary to store course information

    while True:
        print("\nCourse Management System")
        print("1. Display Course Names")
        print("2. Add New Course")
        print("3. Remove Course")
        print("4. Check Course Existence")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        # TODO: Pass the course_info dictionary to the appropriate function based on the user's choice
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == '__main__':
    main()
