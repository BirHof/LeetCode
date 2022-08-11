# 6. Zigzag Conversion

class Solution(object):
    def convert(self, s, numRows):
        L = len(s)
        out_str = [None]*L
        i_out = 0

        if numRows == 1 or L <= numRows:
            return s
        else:
            step_first = (numRows - 1) * 2

        steps = [0] * numRows
        for i in range(numRows):
            steps[i] = step_first - 2 * i
        # print(steps)

        for i in range(numRows):
            j = i
            if i == 0 or i == numRows - 1:
                while j < L:
                    out_str[i_out] = s[j]
                    i_out += 1
                    # print(s[j], end=' ')
                    j += steps[0]
            else:
                # print(s[j], end=' ')
                out_str[i_out] = s[j]
                i_out += 1
                while True:
                        j += steps[i]
                        if j < L:
                            #print(s[j], end=' ')
                            out_str[i_out] = s[j]
                            i_out += 1
                        else:
                            break
                        j += step_first - steps[i]
                        if j < L:
                            #print(s[j], end=' ')
                            out_str[i_out] = s[j]
                            i_out += 1
                        else:
                            break
            # print('')

        return ''.join(out_str)

if __name__ == '__main__':
    s = "PAYPALISHIRING"
    # s = "1234567890123456789"
    obj = Solution()
    print(s)
    print(obj.convert(s=s, numRows=1))
