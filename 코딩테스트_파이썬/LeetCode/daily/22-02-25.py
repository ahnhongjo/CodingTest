class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_list = list(map(int,version1.split(".")))
        version2_list = list(map(int,version2.split(".")))

        version1_len = len(version1_list)
        version2_len = len(version2_list)

        if version1_len > version2_len:
            for i in range(version1_len-version2_len):
                version2_list.append(0)
        else:
            for i in range(version2_len-version1_len):
                version1_list.append(0)

        for i in range(max(version1_len,version2_len)):
            if version1_list[i] > version2_list[i]:
                return 1
            elif version2_list[i] > version1_list[i]:
                return -1

        return 0




a = Solution()

a.compareVersion("1.0","1.0.0")