'''
Given a boat with maximum number of people's weight to carry. Identify minimum number of boat trips to carry all people given weight distribution in list
Sort the list and use 2 pointers to compare weight vs boat maximum weight carry value
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
'''
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats=0
        boatlist=[]
        l,r=0,len(people)-1
        people.sort()
        while l<=r:
            #as long as heavier AND lighter person can fit
            #maximize the number of people in each boat before considering single-person boats

            if people[l]+people[r]<=limit:
                boatlist.append([people[l],people[r]])
                l+=1
                r-=1
            #if the limit exceeds, consider the heavier person alone
            else:
                boatlist.append([people[r]])
                r-=1

            boats+=1
        print(boatlist)
        return boats
        
