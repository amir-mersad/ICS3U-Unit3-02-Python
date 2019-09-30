#!/usr/bin/env python3

# Created by Amir Mersad
# Created on September 2019
# This program checks if there are more there 30 students

import constants


def main():
    # This function checks if there are more than 30 student

    # Input
    number_of_students = int(input("Enter the number of students: "))
    print("")

    # Process
    if number_of_students > constants.MAX_STUDENT_NUMBER:
        # Output
        print("Too many students!")


if __name__ == "__main__":
    main()
