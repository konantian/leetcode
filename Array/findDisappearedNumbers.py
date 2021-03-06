'''
Source : https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
Author : Yuan Wang
Date   : 2018-06-08

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

Time complexity: O(n), Space complexity O(1)
'''

def findDisappearedNumbers(self, nums):
	"""
	:type nums: List[int]
	:rtype: List[int]
	"""
	n=len(nums)
	return list(set(range(1,n+1))-set(nums))