'''
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
'''

def reverseBits(self, n: int) -> int:
    res = 0
    for i in range(32):
        bit = (n >> i) & 1
        res = res | (bit << (31-i))
    return res

