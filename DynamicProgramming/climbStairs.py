
#Source : https://leetcode.com/problems/climbing-stairs/
#Author : Yuan Wang
#Date   : 2018-07-05
'''
********************************************************************************** 
*You are climbing a stair case. It takes n steps to reach to the top.
*
*Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
*
*Note: Given n will be a positive integer.
*
*Example 1:
*
*Input: 2
*Output: 2
*Explanation: There are two ways to climb to the top.
*1. 1 step + 1 step
*2. 2 steps
*Example 2:
*
*Input: 3
*Output: 3
*Explanation: There are three ways to climb to the top.
*1. 1 step + 1 step + 1 step
*2. 1 step + 2 steps
*3. 2 steps + 1 step
**********************************************************************************/
'''
#Recursive solution, TLE
def climbStairsA(n):
	"""
	:type n: int
	:rtype: int
	"""
	if n == 1 or n == 0:
		return 1
	elif n == 2:
		return 2
	
	return climbStairs(n-1)+climbStairs(n-2)


#Dynamic Programming using list
def climbStairsB(n):
	"""
	:type n: int
	:rtype: int
	"""
	sample=[1,2]
	if n <= 2:
		return sample[n-1]
	else:
		for i in range(2,n):

			sample.append(sample[i-1]+sample[i-2])
	
	return sample[n-1]

#Dynamic Programming using dictionary
def climbStairsC(n):
	"""
	:type n: int
	:rtype: int
	"""
	dic={1:1,2:2}
	if n <= 2:
		return dic[n]
	else:
		for i in range(3,n+1):

			dic[i]=dic[i-1]+dic[i-2]
	
		return dic[n]
n=30
print(climbStairs(n))
