# Day 17 - 3Sum

## Problem

Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]] such that:

nums[i] + nums[j] + nums[k] = 0

The solution set must not contain duplicate triplets.

## Approach

1. Sort the array.
2. Fix one element.
3. Use two pointers to find the remaining two numbers.
4. Skip duplicates to avoid repeated triplets.

## Complexity

- Time Complexity: O(n²)
- Space Complexity: O(1)

## Platform

LeetCode #15 - 3Sum
