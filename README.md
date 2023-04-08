# Basic-Python-Programs

<i>Our Python Code Repository is a community-driven platform for sharing high-quality Python programs. With contributions from members of the community, our repository contains a collection of Python codes for others to learn from and use. We welcome contributions from anyone who wants to share their code and follow our guidelines. Our moderators review all pull requests to ensure the quality and consistency of our repository. Join our community and contribute to creating a valuable resource for Python developers worldwide.</i></br>
## How to Contribute

1. Fork the repository to your GitHub account.
2. Clone the repository to your local machine.
3. Create a new branch for your changes.
4. Make changes and commit them to your branch.
5. Push your branch to your forked repository.
6. Open a pull request to the original repository.

## Guidelines for Contributions

- Ensure the use of descriptive variable and function names.
- Write meaningful code comments to describe a function.</br>
Example-
```python
def binary_search(target, lst):
    """
    Performs binary search on a sorted list to find the index of a target element.

    Args:
        target (int): The target element to find in the list.
        lst (list): The sorted list to search in.

    Returns:
        int: The index of the target element in the list, or -1 if it is not found.
    """
    count_iterations = 0  # Counter for the number of iterations required to perform the search
    start_index = 0  # The starting index of the search range
    end_index = len(lst) - 1  # The ending index of the search range

    # Perform binary search until the target element is found or the search range is exhausted
    while start_index <= end_index:
        count_iterations += 1
        mid_index = (start_index + end_index) // 2  # Calculate the midpoint index of the search range
        if target < lst[mid_index]:
            end_index = mid_index - 1  # Adjust the search range to the lower half
        elif target > lst[mid_index]:
            start_index = mid_index + 1  # Adjust the search range to the upper half
        else:
            return mid_index  # The target element is found at the midpoint index

    return -1  # The target element is not found in the list
```
- Write precise commit messages so that other fellow contributors understand what you are trying to do.
- Please describe any test cases that failed or were enhanced, and any improvements to time/space complexity, when modifying existing code in your commit message.</br>
Ex- if you have modified mid_index calculation to mid_index=start+(end-start)//2 in order to avoid integer overflowing
```python
mid_index=start+(end-start)//2
```
Commit message for the same would be:
```Mid integer overflowing avoided```</br>
Extended (optional) description could be:
```The benefit of this formula is that it avoids integer overflow when calculating the midpoint index for large values of start and end.
In the formula mid = (start + end) / 2, if start and end are large integers, adding them may exceed the maximum value that can be stored in an integer variable, leading to integer overflow and potentially incorrect results.
```

- Include documentation for new features.

<h4>If you have any questions or need help with contributing to the project, please reach out to us via GitHub issues</h4>

<i><h3>We welcome any feedback, suggestions, or contributions to our project. Please feel free to reach out to us if you have any questions or would like to contribute.</h3></i>
