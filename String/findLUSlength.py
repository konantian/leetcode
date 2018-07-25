'''
Source : https://leetcode.com/problems/longest-uncommon-subsequence-i/
Author : Yuan Wang
Date   : 2018-07-17

/*************************************************************************************** 
*Given a group of two strings, you need to find the longest uncommon subsequence of this 
*group of two strings. The longest uncommon subsequence is defined as the longest 
*subsequence of one of these strings and this subsequence should not be any subsequence 
*of the other strings.
*
*A subsequence is a sequence that can be derived from one sequence by deleting some 
*characters without changing the order of the remaining elements. Trivially, any string 
*is a subsequence of itself and an empty string is a subsequence of any string.
*
*The input will be two strings, and the output needs to be the length of the longest 
*uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.
*
*Example 1:
*Input: "aba", "cdc"
*Output: 3
*Explanation: The longest uncommon subsequence is "aba" (or "cdc"), 
*because "aba" is a subsequence of "aba", 
*but not a subsequence of any other strings in the group of two strings. 
****************************************************************************************/
 '''

def findLUSlength(a, b):
	"""
	:type a: str
	:type b: str
	:rtype: int
	"""
	if a == b:
		return -1
	m=len(a)
	n=len(b)
	return m if m > n else n

a="aba"
b="cdc"
print(findLUSlength(a,b))