# Kristina Chorna
# Programming Exercise 6
# The objective of this code is to create a program that prompts the user to enter a phone number, SSN, and ZIP code
# and determines whether the answers are valid or invalid.


import re

def validate_phone(phone):
    # Validate US phone numbers
    pattern = r'^(\(\d{3}\)\s|\d{3}-)\d{3}-\d{4}$'
    return bool(re.match(pattern, phone))

def validate_ssn(ssn):
    # Validate US Social Security Number
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.match(pattern, ssn))

def validate_zip(zip_code):
    # Validate US ZIP code
    pattern = r'^\d{5}(-\d{4})?$'
    return bool(re.match(pattern, zip_code))

def main():
    # prompt the user to enter a phone number, SSN, and ZIP
    phone = input("Enter a phone number: ")
    ssn = input("Enter a Social Security Number: ")
    zip_code = input("Enter a ZIP code: ")

    # determine whether the answers were valid or invalid and display the results
    print("\nValidation Results:")
    print(f"Phone Number: {'Valid' if validate_phone(phone) else 'Invalid'}")
    print(f"Social Security Number: {'Valid' if validate_ssn(ssn) else 'Invalid'}")
    print(f"ZIP Code: {'Valid' if validate_zip(zip_code) else 'Invalid'}")

if __name__ == "__main__":
    main()
