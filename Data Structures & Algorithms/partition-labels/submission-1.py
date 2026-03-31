class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # иду по строке, в мапе обновляю последний индекс когда встретил символ
        # потом опять иду по строке и смотрю в мапу, если он соответствует текущему индексу то формирую строку новую

        m = {}
        res = []

        for i, c in enumerate(s):
            m[c] = i

        start, max_idx = -1, 0
        for i, c in enumerate(s):
            idx = m[c]
            max_idx = max(max_idx, idx)

            if i == max_idx:
                res.append(i - start)
                start = i
                max_idx = i + 1

        return res