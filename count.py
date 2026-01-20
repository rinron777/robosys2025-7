# SPDX-FileCopyrightText: 2025 rinron777
# SPDX-License-Identifier: BSD-3-Clause

import sys
from collections import defaultdict

def validate_student_id(student_id: str):
    if len(student_id) != 7:
        return False, "E01_LENGTH"

    if not student_id.isdigit():
        return False, "E02_NON_DIGIT"

    year = int(student_id[0:2])
    dept = int(student_id[2:4])
    number = int(student_id[4:7])

    if year < 20 or year > 29:
        return False, "E03_YEAR"

    if dept < 1 or dept > 5:
        return False, "E04_DEPT"

    if number < 1 or number > 999:
        return False, "E05_NUMBER"

    return True, None


def main():
    summary = defaultdict(int)

    for line in sys.stdin:
        student_id = line.strip()
        if student_id == "":
            continue

        valid, error = validate_student_id(student_id)

        if valid:
            print(f"{student_id}: VALID")
            summary["VALID"] += 1
        else:
            print(f"{student_id}: INVALID {error}")
            summary["INVALID"] += 1
            summary[error] += 1

    print("\n--- SUMMARY ---")
    print(f"VALID: {summary['VALID']}")
    print(f"INVALID: {summary['INVALID']}")

    for code in ["E01_LENGTH", "E02_NON_DIGIT", "E03_YEAR", "E04_DEPT", "E05_NUMBER"]:
        print(f"{code}: {summary[code]}")


if __name__ == "__main__":
    main()

