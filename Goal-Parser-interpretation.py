class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        "alGalooG"
        """
        i = 0
        s = ""
        while i < len(command):
            if command[i] == "(" and command[i+1] == ")":
                s = s + "o"
                i += 1
            elif command[i] != "(" and command[i] != ")":
                s = s + command[i]
            i += 1
        return s
solu = Solution()
print(solu.interpret("(al)G(al)()()G"))
