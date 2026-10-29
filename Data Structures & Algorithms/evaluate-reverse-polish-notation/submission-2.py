class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        vals = []

        for v in tokens:
            if v not in {"+", "-", "/", "*"}:
                vals.append(int(v))
            else:
                lft= vals.pop()
                rt = vals.pop()

                match v:
                    case "+":
                        toPush = rt + lft
                    case "*":
                        toPush = rt * lft
                    case "-":
                        toPush = rt - lft
                    case "/":
                        toPush = int(rt / lft)
                vals.append(toPush)
        return vals.pop()
        
                        
        