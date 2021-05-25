# Challenge Summary
<!-- Description of the challenge -->
Write a function called zipLists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list. Try and keep additional space down to O(1). You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Whiteboard Process
<!-- Embedded whiteboard image -->
![](../../../img/Zip.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Create new list and append current element for each list.
## Solution
<!-- Show how to run your code, and examples of it in action -->
1.After receiving tow list check if the list is not empty.

2.append the the current element from the first list in a new list.

3.append the current element from the second list.

4.current = next for both lists 

5. Loop again until the end of the tow lists 
