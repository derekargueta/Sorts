import sys
import math
sys.setrecursionlimit(50)

test_list = [12, 9, 3, 7, 14, 11, 6, 2, 10, 5]

######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
########################################################## Bubble Sort ###############################################################
######################################################################################################################################
def bubble_sort(my_list):

	# repeat the algorithm for the number of items in the list
	for outer in range(0, len(my_list)):

		# iterate through all of the items in the list
		for inner in range(0, len(my_list)-1):

			# if the number in front(to the right) is bigger, then we must swap the numbers
			if my_list[inner] > my_list[inner+1]:

				# use this 'cup' as temporary storage
				cup = my_list[inner]

				# now that my_list[inner] is safely stored, we can replace it with the value in my_list[inner+1]
				my_list[inner] = my_list[inner+1]

				# and now that the value at my_list[inner+1] is safely stored in my_list[inner], we can empty the cup here
				my_list[inner+1] = cup

	return my_list

######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################## SELECTION SORT ##############################################################
######################################################################################################################################

def selection_sort(my_list):
	num_elems = len(my_list)
	for i in range(0, num_elems-1):
		smallest = i
		for j in range(i, num_elems):
			if my_list[j] < my_list[smallest]:
				smallest = j
		cup = my_list[i]
		my_list[i] = my_list[smallest]
		my_list[smallest] = cup

	return my_list


######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################## INSERTION SORT ##############################################################
######################################################################################################################################

def insertion_sort(my_list):
	num_elems = len(my_list)
	for i in range(1, num_elems-1):
		key = my_list[i]
		j = i - 1
		while j > 0 and my_list[j] > key:
			my_list[j + 1] = my_list[j]
			j = j - 1
		my_list[j + 1] = key
	return my_list


######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
########################################################## MERGE SORT ################################################################
######################################################################################################################################
def merge(my_list, start_index, current_index, end_index):

	if abs(end_index - start_index) < 2:
		return my_list

	# the number of items in the first half of the array
	n1 = current_index - start_index + 1

	# the number of items in the second half of the array
	n2 = end_index - current_index

	# a temporary array that holds all of the items in the first half of the array
	temp_array_A = my_list[start_index:current_index]

	# a temporary array that holds all of the items in the second half of the array
	temp_array_B = my_list[current_index:end_index]

	# set some initial values for indexes before we iterate through the arrays
	# k is the value in the for loop, representing the index in the overall complete array
	# i is the index of the temporary array temp_arr_1
	# j is the index of the temporary array temp_arr_2
	index_A = index_B = 0

	# iterate through the complete array
	for k in range(start_index, end_index):

		# if we have already used all of array A, then just go to array B
		if index_A >= len(temp_array_A):

			my_list[k] = temp_array_B[index_B]

			# advance in array B
			index_B = index_B + 1

		# vice versa, if we have already used all of array B, then just go to array A
		elif index_B >= len(temp_array_B):

			my_list[k] = temp_array_A[index_A]

			# advance in array A
			index_A = index_A + 1

		else:	# if we have not used all of either array, then we must make comparisons to see which value is smaller

			# if the value in array A is smaller than the value in array B, then use the value in array A
			if temp_array_A[index_A] <= temp_array_B[index_B]:

				my_list[k] = temp_array_A[index_A]

				# advance in array A
				index_A = index_A + 1

			# vice versa, if the value in array B is smaller than the value in array A, then use the value in array B
			else:

				my_list[k] = temp_array_B[index_B]

				# advance in array B
				index_B = index_B + 1

	return my_list

def merge_sort(my_list, start_index, end_index):

	# base case: break the recursion if we are down to a single element
	if start_index >= end_index - 1:
		return my_list

	# otherwise, meaning the array partition has two or more elements in it still
	else:

		# find the halfway index
		current_index = (start_index + end_index) / 2

		# recursively call the sort on the left half
		merge_sort(my_list, start_index, current_index)

		# recursively call the sort on the right half
		merge_sort(my_list, current_index, end_index)

		# once the recursive merge_sort functions are done, then the array is ready for merging together
		return merge(my_list, start_index, current_index, end_index)
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
########################################################## QUICK SORT ################################################################
######################################################################################################################################


def partition(my_list, start_index, end_index):

	# initially set the pivot point as the starting index
	pivot = start_index

	# iterate through all of the other elements in the array
	for u in range(start_index, end_index):

		# if the current item is less than the last item, then swap with the item at the pivot point
		if my_list[u] <= my_list[end_index]:

			# same technique for swapping as with the bubble sort
			cup = my_list[pivot]
			my_list[pivot] = my_list[u]
			my_list[u] = cup

			# increment the pivot point
			pivot = pivot + 1

	cup = my_list[pivot]
	my_list[pivot] = my_list[end_index]
	my_list[end_index] = cup

	return pivot

def quicksort(my_list, start_index, end_index):

	# base case: if the partition only has 1 element, then stop the recursion
	if start_index >= end_index-1:

		return my_list

	else:

		# determine a pivot point
		pivot = partition(my_list, start_index, end_index)

		# recursively sort the left side
		quicksort(my_list, start_index, pivot-1)

		# recursively sort the right side
		quicksort(my_list, pivot, end_index)

		return my_list

######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################

print bubble_sort(test_list)
print selection_sort(test_list)
print insertion_sort(test_list)
print merge_sort(test_list, 0, len(test_list))
print quicksort(test_list, 0, len(test_list)-1)
