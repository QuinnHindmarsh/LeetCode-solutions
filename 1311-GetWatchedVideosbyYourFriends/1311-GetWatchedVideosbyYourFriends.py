class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        visited = [False] * len(friends)


        def bfs(id,level):
            q = deque()
            q.append(id)
            visited[id] = True

            for _ in range(level):
                for _ in range(len(q)):
                    cur = q.popleft()
                    for f_id in friends[cur]:
                        if not visited[f_id]:
                            q.append(f_id)
                            visited[f_id] = True

            vid_freq = Counter()
            while q:
                cur = q.pop()
                for vid in watchedVideos[cur]:
                    vid_freq[vid] +=1
            
            sorted_vids = sorted(vid_freq.items(), key=lambda x: (x[1], x[0]))
            sv = [video[0] for video in sorted_vids]
            return sv
        
        return bfs(id,level)
                
            