# def quickSort(lst, left, right):
# 	if left < right:
# 		middle = partition(lst, left, right)
# 		quickSort(lst, 0, middle-1)
# 		quickSort(lst, middle+1, right)
# 	return lst

# def partition(lst, left, right):
# 	temp = lst[left]
# 	while left < right:
# 		while left < right and lst[right] >= lst[left]:
# 			right -= 1
# 		lst[left] = lst[right]
# 		while left < right and lst[left] <= lst[right]:
# 			left += 1
# 		lst[right] = lst[left]
# 	lst[left] = temp
# 	return left

# a = [1,6,8,4,3,6,9,3]
# print(quickSort(a, 0, len(a)-1))

# class Node:
# 	def __init__(self, value = None, lchild = None, rchild = None):
# 		self.value = value
# 		self.lchild = lchild
# 		self.rchild = rchild

# def preOrder(root):
# 	if root == None:
# 		return
# 	print(root.value)
# 	preOrder(root.lchild)
# 	preOrder(root.rchild)

import requests

url = 'https://account.douban.com/login'

data = dict(
	source = None,
	redir = 'https://www.douban.com',
	form_email = 'test',
	form_password = 'test123')

response = requests.post(url, data)
print(response)