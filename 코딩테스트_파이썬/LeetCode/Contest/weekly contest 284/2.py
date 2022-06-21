from typing import List

class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        land =[[0 for i in range(n)] for j in range(n)]
        ret =0
        for i in dig:
            land[i[0]][i[1]] =1

        for artifact in artifacts:
            buried = True
            for i in range(artifact[0],artifact[2]+1):
                for j in range(artifact[1],artifact[3]+1):
                    if land[i][j] ==0:
                        buried = False

            if buried:
                ret+=1
        return ret


a = Solution()
a.digArtifacts(2,[[0,0,0,0],[0,1,1,1]],[[0,0],[0,1],[1,1]])