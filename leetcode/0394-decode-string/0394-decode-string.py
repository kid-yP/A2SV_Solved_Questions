class Solution:
    def decodeString(self, s: str) -> str:
        liben = []

        for ch in s:
            if ch == ']':
                temp = ""
                while liben and liben[-1] != '[':
                    temp = liben.pop() + temp
                liben.pop()

                rob = ""
                while liben and liben[-1].isdigit():
                    rob = liben.pop() + rob
                liben.append(int(rob) * temp)             
            else:
                liben.append(ch)
        return "".join(liben)