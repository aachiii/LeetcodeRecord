# 904. Fruit Into Baskets

## Question
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array `fruits` where `fruits[i]` is the **type** of fruit the `ith` tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have **two** baskets, and each basket can only hold a **single type** of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick **exactly one fruit** from **every** tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array `fruits`, return the _**maximum**_ number of fruits you can pick.

## Example

### Example 1
```text
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
```
### Example 2
```text
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
```
### Example 3
```text
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
```

### Code
```python
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        p1, p2 = 0, 0
        res = 0
        types = {}
        t = 0
        
        # check if it is a new fruit, and update the counter
        while p2 < len(fruits):
            if types.get(fruits[p2], 0) == 0:
                t += 1
            types[fruits[p2]] = types.get(fruits[p2], 0) + 1
            
            # too many different fruits, so start shrinking window
            while t > 2:
                types[fruits[p1]] -= 1
                if types[fruits[p1]] == 0:
                    t -= 1
                p1 += 1

            # set res to the max window size
            res = max(res, p2-p1+1)
            p2 += 1
        return res

```
* `Time Complexity`: O(n)
* `Takeaways`:  Start typing when your mind gets clear. :)
