from typing import List
import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        maxjump = []
        now = heights[0]
        ans = 0
        use_bricks = 0
        for h in heights[1:]:
            if now >= h:
                ans += 1
            else:
                jump = h - now
                if ladders == 0:
                    use_bricks += jump
                elif len(maxjump) < ladders:
                    heapq.heappush(maxjump, jump)
                else:
                    if maxjump[0] < jump:
                        tmp = heapq.heappop(maxjump)
                        use_bricks += tmp
                        heapq.heappush(maxjump, jump)
                    else:
                        use_bricks += jump

                if use_bricks <= bricks:
                    ans += 1
                else:
                    return ans
            now = h

        return ans

