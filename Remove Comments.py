class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        in_block = False
        new_line = ""

        for line in source:
            i = 0
            while i < len(line):
                if not in_block and i + 1 < len(line) and line[i] == '/' and line[i + 1] == '*':
                    in_block = True
                    i += 2
                elif in_block and i + 1 < len(line) and line[i] == '*' and line[i + 1] == '/':
                    in_block = False
                    i += 2
                elif not in_block and i + 1 < len(line) and line[i] == '/' and line[i + 1] == '/':
                    break
                elif not in_block:
                    new_line += line[i]
                    i += 1

                else:
                    i += 1

            if not in_block and new_line:
                result.append(new_line)
                new_line = ""

        return result
