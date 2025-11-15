class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s

        rows = []
        for rr in range(numRows):
            rows.append("")

        row_now = 0
        going_down = True

        for letter in s:
            tmp = ""
            for xx in rows[row_now]:
                tmp += xx
            tmp += letter
            rows[row_now] = tmp

            if going_down:
                row_now += 1
                if row_now == numRows - 1:
                    going_down = False
            else:
                row_now -= 1
                if row_now == 0:
                    going_down = True

        final_ans = ""
        for one_row in rows:
            for ch in one_row:
                final_ans += ch

        return final_ans
