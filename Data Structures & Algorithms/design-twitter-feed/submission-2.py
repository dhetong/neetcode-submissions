class Twitter:

    def __init__(self):
        self.followers = defaultdict(list)
        self.posts = defaultdict(list)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.posts[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        post_list = []
        heapq.heapify(post_list)
        for uid in self.followers[userId]:
            for post in self.posts[uid]:
                heapq.heappush(post_list, post)
                if len(post_list) > 10:
                    heapq.heappop(post_list)
        for post in self.posts[userId]:
            heapq.heappush(post_list, post)
            if len(post_list) > 10:
                heapq.heappop(post_list)
        res = []
        while post_list:
            res.append(heapq.heappop(post_list)[1])
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return
        else:
            if followeeId in self.followers[followerId]:
                return
            self.followers[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return
        else:
            if followeeId not in self.followers[followerId]:
                return
            self.followers[followerId].remove(followeeId)
