# multi-drone-quiz (Problem #1)

## Problem Statement

Given a MxN grid and coordinates where the obstacles are present, task it to compute the grid in which each cell stores the euclidean distance to closest obstacle.

## Naive Solution (Brute Force)

In each cell, we can compare the distances of each obstacle and keep the minimum.

**Time complexity: $ O(M^2*N^2) $**

Given $ T $ as the number of obstacles, the time complexity for the problem is $ O(M*N*T) $ . However, since $ T $ is of complexity $ O(M*N) $, the overall time complexity of the problem is $ O(M^2 * N^2) $.

## Optimal solution (using distance transforms)

Distance transforms are widely used in image processing for characterizing morphology of objects. This approach is used in this context to convert the obstacle information into euclidean distance information in the grid.

So, we initially develop the grid with 0s in the position of obstacles and some random big value in rest of the cells (explanation given later stage).

We want to compute the euclidean distance to nearest obstacle from each cell, which is characterised by $ D_f(x, y) = min_{x', y'} ((x-x')^2 + (y-y')^2 + f(x', y')) $, where $ f(x', y') $ is the grid function which returns the current value of grid at cell $ (x', y') $.

Here, $ f(x', y') $ will define if the euclidean distance should be taken from this cell $ (x', y') $, i.e., if the value of this function is some high random value, then it won't be considered when compared to the $ D_f $ value obtained from another cell whose value is 0. This is why we chose some high random value for non-obstacle cells, so that those cells are not considered when computing euclidean distance to a particular cell.

We can reduce the above expression to following,

$ D_f(x, y) = min_{x'} ((x-x')^2 + min_{y'} ((y-y'^2) + f(x', y'))) $

$ D_f(x, y) = min_{x'} ((x-x')^2 + D_{f|x'}(y)) $, where $ D_{f|x'} (y) $ is 1D distance transform.

Hence, we first perform distance transform on all columns and then all rows with updated grid values, or vice versa (first rows and then columns)

For D distance transform, the expression $ D_f (x) = min_{x'} ((x-x')^2 + f(x')) $ is like taking the lower envelop of group of parabolas defined at $ (x', f(x')) $

Hence, we first compute the lower envelop of the group of parabolas, and use this information to compute the distance transform. 

Hence, after computing the distance transforms for all columns, we will have minimum distances of obstacles to every cell in each column (independently). We use this information and do another round of distance of transform on all rows independently, which will provide euclidean distances to nearest obstacles from each cell.

**Time complexity: O(M*N), where M is number of rows and N is number of columns**

The time complexity of 1D distance transform is $ O(N) $, given N is the length of array. Hence, for first of distance transforms (on all columns) is $ O(N*M) $ and then second round of distance transforms is of complexity $ O(M*N) $. Hence, total complexity is $ O(2*M*N) = O(M*N) $ which is a lot of improvement over naive approach.
