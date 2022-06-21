class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = dict()
        for i in range(len(s)):
            for j in range(len(s) - i):
                maxlen = 0
                start = j
                end = j + i

                if i == 0:
                    maxsub = (start, end)
                    dp[(start, end)] = 1
                elif i == 1:
                    if s[start] == s[end]:
                        maxlen = 1
                        maxsub = (start, end)
                        dp[(start, end)] = 2
                else:
                    if (start + 1, end - 1) in dp and s[start] == s[end]:
                        if maxlen < i:
                            maxlen = i
                            maxsub = (start, end)

                        dp[(start, end)] = dp[(start + 1, end - 1)] + 2

        return s[maxsub[0]:maxsub[1] + 1]

a = Solution()
print(a.longestPalindrome("eebzcrhbishfhmiminstjudrmgqbjgztrczaipwnyxywjtfvzhjblbxdjoxitjxhoxvrygpudzollkzyjspcrurtlxvopboqogpmeimnzpzlcnmmboizjtsehbraojzdmsihepphexnpmssqeimcipbzvjltywradlbwwqzozphflxzxmrnhhjmfrucswfzndchgrgabolcjwdvfetsuugpkizncpjdeclaopfjmdwmhlxcvncbprfxfompsbqdjlqplfrppzfdntfxwxspwgybvqpjkasvqhovlwprsyqdyocryqccrbsggohjjgzhxqxcmpsugnzclgcsrbpwvrxsxaejntmnpyoabkqpzqvodcobwjqxxcfmjdrteptnjlppljntpetrdjmfcxxqjwbocdovqzpqkbaoypnmtnjeaxsxrvwpbrscglcznguspmcxqxhzgjjhoggsbrccqyrcoydqysrpwlvohqvsakjpqvbygwpsxwxftndfzpprflpqljdqbspmofxfrpbcnvcxlhmwdmjfpoalcedjpcnzikpguustefvdwjclobagrghcdnzfwscurfmjhhnrmxzxlfhpzozqwwbldarwytljvzbpicmieqssmpnxehppehismdzjoarbhestjziobmmnclzpznmiempgoqobpovxltrurcpsjyzkllozdupgyrvxohxjtixojdxblbjhzvftjwyxynwpiazcrtzgjbqgmrdujtsnimimhfhsibhrczbee"))
