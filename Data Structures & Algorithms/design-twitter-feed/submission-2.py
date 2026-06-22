import heapq
class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.user_tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweet_map[userId].append((-self.timestamp,tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # return 10 tweets
        ans = []
        tweets = []
        tweets += self.user_tweet_map[userId]

        if self.follow_map[userId]:
            for followee in self.follow_map[userId]:
                if followee != userId:
                    tweets += self.user_tweet_map[followee]

        heapq.heapify(tweets)

        while tweets and len(ans) < 10:
            ts, tweet = heapq.heappop(tweets)
            ans.append(tweet)

        return ans
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
