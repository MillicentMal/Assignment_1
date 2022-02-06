First assignment for the DSA course at ALU. 

**Question One**

State the Big O-notation and implement the algorithm that perform the following operations: 

The algorithm takes as input a list of numbers which may contain duplicates. It returns true if all elements of the list occur an odd number of times. Otherwise it returns false. For example, on the list {1, 3, 2, 2, 5, 2} it returns true, but on the list {1, 3, 2, 2, 5, 2, 5} it returns false because 5 occurs an even number of times. [5]

**Question Two**

Design and implement an algorithm that takes: a list containing n distinct natural numbers and a number k ≤ n and calculates the sum of the k largest numbers in the array. For example, if the list is {3, 7, 5, 12, 6} and k = 3, then the algorithm should return 25= (12+7+6).

Implement the algorithm in python [5]
**Question Three**

A Burglar breaks into a house with a bag that can carry a maximum of 20 kg. He found a safe with 8 gold pellets with the following weights and their corresponding values in US$:

5kg - $2500
3kg -$1700
1kg-$1200
6kg-$3000
8kg-$4100
4kg-$2000
11kg-$7000
12kg-$7500
 

Using the 0-1 Knapsack Algorithm , which combination of pellets would bring about the highest profit, provided the weight does not exceed 20kgs. Print the combination of the pellets and the total value accrued by that combination. [5]

**Question Four**

An UndoableList is a linear , singly linked list without dummy nodes. It contains integers in increasing sorted order and supports the usual find , insert and delete operations, plus two new operations called undo and redo . The undo operation allows us to change the list back to a previous version, by reversing the last edit operation. We can call undo n times to reverse the last n edit operations. If there is no previous edit operation (because the list is new, or because all edit operations have been undone), undo does nothing. A redo operation cancels the previous undo operation and is used to update the list back to the next more recent version. As an example, consider a list L containing 2, 5, and 7, denoted as [2,5,7]. The following shows the sequence of operations executed and the list after each operation.

Insert (6) // [2,5,6,7]
delete (5) // [2,6,7]
undo // [2,5,6,7], delete (5) cancelled.
Undo // [2,5,7], insert (6) cancelled.
Redo // [2,5,6,7], last undo cancelled, re-apply insert (6).
insert (4) // [2,4,5,6,7]
redo // [2,4,5,6,7], nothing to redo
delete (3) // [2,4,5,6,7], 3 is not in the list, L remains unchanged.
Undo // [2,4,5,6,7], delete (3) cancelled.
Undo // [2,5,6,7], insert (4) cancelled.
Undo // [2,5,7], insert (6) cancelled ( delete (5) has been cancelled by line 3).
redo // [2,5,6,7], reapply insert (6).
redo // [2,4,5,6,7] reapply insert (4).
You are to add all five methods in class UndoableList listed below using the scheme described  above:

UndoableList( ) : Constructor for an UndoableList object. [5]
undo(): Revert the list back to the previous version by canceling the last edit operation. If no previous version exists , it has no effect on the list. [5]
redo(): Reapply the operation cancelled by the last undo operation. It has no effect on the most recent version of the list. [5]
insert(int v): Inserts value v into the list, maintaining sorted order. [5]
delete(int v): Deletes the first occurrence of value v from the list. If v does not exist in the list, do nothing. [5]