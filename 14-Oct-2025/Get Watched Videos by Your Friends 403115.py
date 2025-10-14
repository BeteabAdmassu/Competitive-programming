# Problem: Get Watched Videos by Your Friends - https://leetcode.com/problems/get-watched-videos-by-your-friends/description/

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n = len(friends)
        seen = set()
        seen.add(id)
        queue = deque([(id, 0)])
        levels = []

        while queue:
            curr_id, curr_lev = queue.popleft()
            if curr_lev == level:
                levels.append(curr_id)
                continue
            
            if curr_lev > level:
                continue

            for i in friends[curr_id]:
                if i not in seen:
                    seen.add(i)
                    queue.append((i, curr_lev + 1))

        all = []

        for i in levels:
            all.extend(watchedVideos[i])
        
        counts = Counter(all)

        res = sorted(counts.items(), key=lambda item:(item[1], item[0]))
        return [x for x, y in res]