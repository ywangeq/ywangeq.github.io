---
layout:     post
title:      Leecode 双周赛
subtitle:   5314 跳跃游戏IV
date:       2020-02-09
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - Leecode_hard
    - 周赛
    - python
    - bfs
---

给你一个整数数组 arr ，你一开始在数组的第一个元素处（下标为 0）。

每一步，你可以从下标 i 跳到下标：

i + 1 满足：i + 1 < arr.length
i - 1 满足：i - 1 >= 0
j 满足：arr[i] == arr[j] 且 i != j
请你返回到达数组最后一个元素的下标处所需的 最少操作次数 。

注意：任何时候你都不能跳到数组外面。
输入：arr = [100,-23,-23,404,100,23,23,23,3,404]
输出：3
解释：那你需要跳跃 3 次，下标依次为 0 --> 4 --> 3 --> 9 。下标 9 为数组的最后一个元素的下标。

```
from collections import defaultdict
class Solution:
    def minJumps(self,arr):
        d = defaultdict(list)
        n = len(arr)
        for i in range(n):
            d[arr[i]].append(i)
        
        vis =[0]*n
        vis[0]=1
        q = [(0,0)]
        while q:
            i,k = q.pop(0)
            for j in d[arr[i]+[i-1,i+1]]:
                if j < 0 or j >=n or vis[j]:
                    continue
                if j==n-1:
                    return k+1
                vis[j]=1
                q.append((j,k+1))
            d[arr[i]]=[]# 同值不再走
        return 0
```