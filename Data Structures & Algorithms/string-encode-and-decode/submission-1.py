class Solution:

    def encode(self, strs: List[str]) -> str:
        preamble = \
            f"{len(strs)};{';'.join([str(len(s)) for s in strs])};"
        
        return preamble + "".join(strs)

    def decode(self, s: str) -> List[str]:
        split = s.split(";")
        n = int(split[0])
        lens = []
        for i in range(n):
            lens.append(int(split[i+1]))
        res = []
        pos = sum([len(str(x))+1 for x in lens]) + len(str(n)) + 1
        for l in lens:
            res.append(s[pos:pos+l])
            pos = pos+l
        return res
