class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        rowglass ={}

        def dp(row,glass):
            water = 0
            if (row,glass) in rowglass:
                return rowglass[(row,glass)]
            if row ==0:
                return poured

            if glass == 0:
                tmp = dp(row-1,0)
                if tmp<1:
                    water =0
                else:
                    water = (tmp-1)*0.5

            elif glass == row:
                tmp = dp(row - 1, glass-1)
                if tmp<1:
                    water = 0
                else:
                    water = (tmp - 1) * 0.5

            else:
                tmp1 = dp(row-1,glass-1)
                tmp2 = dp(row-1,glass)

                if tmp1 <1 and tmp2 <1:
                    water = 0
                elif tmp1<1:
                    water = (tmp2-1)/2
                elif tmp2<1:
                    water = (tmp1-1)/2
                else:
                    water = (tmp1+tmp2-2)/2

            rowglass[(row,glass)] = water
            return water

        water = dp(query_row,query_glass)

        return min(water,1)



a = Solution()
print(a.champagneTower(5, 2, 1))
