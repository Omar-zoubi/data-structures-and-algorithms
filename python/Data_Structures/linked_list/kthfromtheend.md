# Challenge Summary
<!-- Description of the challenge -->

We have to Write a method for the Linked List class which takes a number, k, as a parameter. Return the node’s value that is k from the end of the linked list. You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges

## Whiteboard Process
<!-- Embedded whiteboard image -->
![](../img/Untitled (10).jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
First I manage to calculate the length by looping over the linked-list,
then Looping in range (0,length-k) to reach index (length-k-1) and then return its value.

***Checked if the parameter value (k) is larger than the length or less than Zero, if True  return ERORR MESSAGE***


## Solution
<!-- Show how to run your code, and examples of it in action -->
1. Looping throw the Linked-list to find it's length.

2. checking if the parameter value (k) is larger than the length or less than Zero, if True  return ERORR MESSAGE

3.Looping in range (0,length-k) to reach index (length-k-1) and then return its value.


[Pull Request](https://github.com/Omar-zoubi/data-structures-and-algorithms/pull/28)
