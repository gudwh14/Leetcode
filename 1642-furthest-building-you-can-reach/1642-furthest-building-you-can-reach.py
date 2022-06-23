class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        Q = []
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i - 1]

            if diff > 0:
                heapq.heappush(Q, -diff)
                bricks -= diff

            # 벽돌이 없고 사다리가 남아있을경우 가장 많이 사용한 벽돌을 사다리로 교체
            if bricks < 0:
                if ladders > 0:
                    bricks += -heapq.heappop(Q)
                    ladders -= 1
                # 벽돌도 없고 사다리가 없으면 종료
                else:
                    return i - 1
        return len(heights) - 1