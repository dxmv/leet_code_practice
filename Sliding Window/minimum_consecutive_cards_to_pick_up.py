# 2260. Minimum Consecutive Cards to Pick Up

class Solution:
    # Time: O(n), Memory: O(n) - Hash Table Method
    def minimumCardPickup(self, cards: List[int]) -> int:
        mp={}
        i=0
        min_cards=float('inf')
        while i<len(cards):
            current=cards[i]
            if current in mp:
                if not min_cards:
                    min_cards=i-mp[current]+1
                else:
                    min_cards=min(min_cards,i-mp[current]+1)
                mp[current]=i   
            else:
                mp[current]=i
            i+=1
        return min_cards if min_cards!=float('inf') else -1