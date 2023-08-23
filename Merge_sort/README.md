----------Divide and Conquer Strategy-----------

Using the Divide and Conquer technique, we divide a problem into subproblems. When the solution to each subproblem is ready, we 'combine' the results from the subproblems to solve the main problem.

Suppose we had to sort an array 'A'. 'A' subproblem would be to sort a sub-section of this array starting at index "p" and ending at index "r", denoted as A[p..r].

######Divide#######3

If "q" is the half-way point between "p" and "r", then we can split the subarray A[p..r] into two arrays A[p..q](first part of the array) and A[q+1, r](second part of the array).

#####Conquer########

In the conquer step, we try to sort both the subarrays A[p..q] and A[q+1, r]. If we haven't yet reached the base case, we again divide both these subarrays and try to sort them.

############Combine###############

When the conquer step reaches the base step and we get two sorted subarrays A[p..q] and A[q+1, r] for array A[p..r], we combine the results by creating a sorted array A[p..r] from two sorted subarrays A[p..q] and A[q+1, r].

-----------Merge Sort-----------------

The MergeSort function repeatedly divides the array into two halves until we reach a stage where we try to perform MergeSort on a subarray of size 1 i.e. p == r.

After that, the merge function comes into play and combines the sorted arrays into larger arrays until the whole array is merged.

---------The logic behind the problem---------

Have we reached the end of any of the arrays?
No:
Compare current elements of both arrays
Copy smaller element into sorted array
Move pointer of element containing smaller element
Yes:
Copy all remaining elements of non-empty array
