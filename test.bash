#!/bin/bash
# SPDX-FileCopyrightText: 2025 rinron777
# SPDX-License-Identifier: BSD-3-Clause

set -e

output=$(cat <<EOF | python3 count.py
2303007
2310001
23A3001
2303999
2303008
EOF
)

# 個別判定
echo "$output" | grep -q "2303007: VALID"
echo "$output" | grep -q "2310001: INVALID E04_DEPT"
echo "$output" | grep -q "23A3001: INVALID E02_NON_DIGIT"
echo "$output" | grep -q "2303999: INVALID E04_DEPT"
echo "$output" | grep -q "2303008: VALID"

# 集計チェック
echo "$output" | grep -q "VALID: 2"
echo "$output" | grep -q "INVALID: 3"
echo "$output" | grep -q "E02_NON_DIGIT: 1"
echo "$output" | grep -q "E04_DEPT: 2"

echo "All tests passed."

