Largest Number

This Python code recursively finds the largest number in a given list.

The code works by comparing the first and last elements of the list at each recursive step:
- If the first element is larger, the function calls itself again on the list excluding the last element.
- Otherwise, it calls itself again on the list excluding the first element.
- The recursion continues until the list is reduced to a single element — the largest number.

Finally, the result is printed to the console.
