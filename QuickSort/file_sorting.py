'''
Question: The Hedge Fund File Sorter.
Imagine you are interning at a top hedge fund, Citadel, and one of your
tasks is to optimize the process of sorting critical trade files. These files
are represented as an array of numbers, where each number corresponds to the
trade volume of a particular stock.

Your mentor hands you the following challenge:
    1. The files need to be sorted in ascending order, but since time is money,
    your algorithm must be efficient and use the "divide-and-conquer" approach.
    2. The sorting process should prioritize a random trade volume as the
    pivot to ensure fairness in comparisons.

Here is an example dataset of trade volumes:
    [34, 7, 23, 32, 5, 62]

Tasks:
1. Explain how you would sort this dataset using the Quick Sort algorithm.
    -> Write the steps clearly as if explaining to someone unfamiliar with the
algorithm.

2. Write Python code to implement the Quick Sort algorithm.
    -> Make sure your code reflects the randomized pivot selection process.

3. Optimization scenario:
    -> After implementing the solution, your mentor informs you that the
    dataset size can grow to over a million elements.
    -> How would you ensure your algorithm remains efficient for such a large
    dataset?
    -> Would you consider other algorithms for sorting in this case? Why or
    why not?

'''
