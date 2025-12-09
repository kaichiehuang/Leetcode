#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start
from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time -= 1
        return

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []

        #add own tweets
        for t in self.tweetMap[userId]:
            heapq.heappush(maxHeap, t)
        
        #add followee tweets
        for followee in self.followMap[userId]:
            for t in self.tweetMap[followee]:
                heapq.heappush(maxHeap, t)

        res = []
        while maxHeap and len(res) < 10:
            res.append(heapq.heappop(maxHeap)[1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        return
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        return 


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

