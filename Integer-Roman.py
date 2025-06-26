class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        Input: num = 3749
        Output: "MMMDCCXLIX"
        """
        s = str(num)
        x = len(s)
        i = 0
        z = 0
        st = ""
        if x == 4:
            T = int(s[z])
            while i < T:
                st = st + "M"
                i += 1
            z = z+1
            x = 3
            i = 0 
        if x == 3:
            H = int(s[z])
            if H == 4:
                st = st + "CD"
            elif H == 5:
                st = st + "D"
            elif H == 9:
                st = st + "CM"
            elif H > 5 :
                st = st + "D"
                H -= 5
                while i < H:
                    st = st + "C"
                    i += 1
            elif H <= 3:
                while i < H:
                    st = st + "C" 
                    i +=1
            x = 2
            i = 0
            z = z+1
        if x == 2:
            LH = int(s[z])
            if LH == 4:
                st = st + "XL"
            elif LH == 5:
                st = st + "L"
            elif LH == 9:
                st = st + "XC"
            elif LH > 5 :
                st = st + "L"
                LH -= 5
                while i < LH:
                    st = st + "X"
                    i += 1 
            elif LH <= 3:
                while i < LH:
                    st = st + "X" 
                    i +=1
            x = 1
            i = 0 
            z = z+1
        if x == 1:
            LT = int(s[z])
            if LT == 4:
                st = st + "IV"
            elif LT == 5:
                st = st + "V"
            elif LT == 9:
                st = st + "IX"
            elif LT > 5 :
                st = st + "V"
                LT -= 5
                while i < LT:
                    st = st + "I"
                    i += 1 
            elif LT <= 3:
                while i < LT:
                    st = st + "I" 
                    i +=1
        return st
solu = Solution()
print(solu.intToRoman(33))
            
        
