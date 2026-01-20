import sys
from collections import defaultdict

def validate_student_id(student_id: str):
    # 桁数チェック
    if len(student_id) != 7:
        return False, "E01_LENGTH"

    # 数字のみか
    if not student_id.isdigit():
        return False, "E02_NON_DIGIT"

    year = int(student_id[0:2])
    dept = int(student_id[2:4])
    number = int(student_id[4:7])

    # 入学年度（20〜29）
    if year < 20 or year > 29:
        return False, "E03_YEAR"

    # 学科コード（01〜05）
    if dept < 1 or dept > 5:
        return False, "E04_DEPT"

    # 個人番号（001〜999）
    if number < 1 or number > 999:
        return False, "E05_NUMBER"

    return True, None


def main():
    summary = defaultdict(int)

    for line in sys.stdin:
        student_id = line.strip()

        # 空行は無視
        if student_id == "":
            continue

        is_valid, error_code = validate_student_id(student_id)

        if is_valid:
            print(f"{student_id}: VALID")
            summary["VALID"] += 1
        else:
            print(f"{student_id}: INVALID {error_code}")
            summary["INVALID"] += 1
            summary[error_code] += 1

    # 集計結果出力
    print("\n--- SUMMARY ---")
    print(f"VALID: {summary['VALID']}")
    print(f"INVALID: {summary['INVALID']}")

    for code in ["E01_LENGTH", "E02_NON_DIGIT", "E03_YEAR", "E04_DEPT", "E05_NUMBER"]:
        print(f"{code}: {summary[code]}")


if __name__ == "__main__":
    main()

