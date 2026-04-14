class Twitter:

    def __init__(self):
        self.mp = {}
        self.f = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # todo: limit by 10, hax heap?
        self.time += 1
        if not self.mp.get(userId):
            self.mp[userId] = set() # todo: max heap by time

        t = (self.time, tweetId)
        self.mp[userId].add(t)
        while len(self.mp[userId]) > 10:
            min_item = min(self.mp[userId], key=lambda x: x[0])
            self.mp[userId].remove(min_item)

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for follow in self.f.get(userId, []):
            if follow == userId: continue
            tweets = self.mp[follow]
            for t in tweets:
                res.append(t)

        for t in self.mp.get(userId, []):
            res.append(t)

        res = sorted(res, key=lambda x: -x[0])
        res = list(map(lambda x: x[1], res))

        return res[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if not self.f.get(followerId):
            self.f[followerId] = set()

        if not followeeId in self.f.get(followerId):
            self.f[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId in self.f[followerId]:
            self.f[followerId].remove(followeeId)
