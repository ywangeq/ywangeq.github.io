---
layout:     post
title:      Leecode 1254
subtitle:   封闭岛屿的个数
date:       2020-01-11
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - Leecode_medium
    - dfs
    - python
---


有一个二维矩阵 grid ，每个位置要么是陆地（记号为 0 ）要么是水域（记号为 1 ）。

我们从一块陆地出发，每次可以往上下左右 4 个方向相邻区域走，能走到的所有陆地区域，我们将其称为一座「岛屿」。

如果一座岛屿 完全 由水域包围，即陆地边缘上下左右所有相邻区域都是水域，那么我们将其称为 「封闭岛屿」。

请返回封闭岛屿的数目。

- 思路 先把边界上的水全填成陆地，让后再去判断剩下的

```
class Solution:
    def closedIsland(grid):
        if not grid or not grid[0]:
            return 0
        row = len(grid)
        col = len(grid[0])

        def dfs(i,j):
            grid[i][j]=1
            for x,y in [(0,1),(0,-1),(-1,0),(1,0)]:
                nx,ny =x+i,y+j
                if 0<=nx<row and 0<=ny<col and grid[nx][ny]==0:
                    dfs(nx,ny)
            return
        
        for i in range(row):
            if  grid[i][0]==0:
                dfs(i,0)
            if grid[i][col-1]==0:
                dfs(i,col-1)

        for j in range(col):
            if grid[0][j]==0:
                dfs(0,j)
            if grid[row-1][j]==0:
                dfs(row-1,j)


        count =0
        for i in range(1,row-1):
            for j in range(1,col-1):
                if grid[i][j]==0:
                    count+=1
                    dfs(i,j)
        return count




```