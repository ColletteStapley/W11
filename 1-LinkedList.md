# Linked Lists

[Introduction Page](0-Introduction.md)

## Introduction

Linked lists take the memory of a dynamic array and scatter it across the system. This allows the list to hold a lot of values. The problem is, how on earth does this keep an order if the values aren't held together? By linking them, like chains. They may be in different spots in memory, but each value, aka <b>Node</b> has a pointer to the value in front of it and a pointer to the value behind it. Then, this list itself has a <b>Head</b> pointer and a <b>Tail</b> pointer, that mark the front and back of the list.  

## Chains and Links

As was briefly explained above a linked list is like a chain. Each link holds a location in memory with the desired data. Then, each link is attatched to two other links. On in "front" and one in "back". Normal chains don't have a front/back orientation, but linked list's do. So One link, or Node holds the memory location, and two pointers to two other links/nodes. In order to add anything into the list/chain, you need to create the link/node,  and change the points for all that need changing. 

## Insert/Remove 

Inserting and removing from lists can be a bit complicated at first, expecially since the terms prev, next, head, and tail, can be a bit confusing unless you understand the structure. 

<br> The prev and next pointers are pretty self explanetory on their own: Next points to the next node, and prev points to the previous node. It's when Head and Tail come it that it gets a bit backwards. Based on the order of the next's and prev's, you'd expect the front of the list to have the empty next pointer. But it isn't. The node that has an empty prev. pointer is where the head is. Vice Versa, the node with an empty next pointer is where the tail is.

Example:

![Alt](/pictures/LL%20start.png "Queue Start")

<br>

### For Inserting into the Front of the List / the Head
###### <b>Note:</b> be sure to check that the list isn't empty before adding(`self.head is None`). If so, just set the head and tail pointers to the new node

1. Create a new node (`new_node = LinkedList.Node(value)`)
2. Set the <b>next</b> pointer of the new node to the current head node (`new_node.next = self.head`)
3. Set the <b>prev</b> pointer of the current head to the new node (`self.head.prev = new_node`)
4. Set the <b>tail</b> pointer to the new Node (`self.head = new_node`)

Example: 

![Alt](/pictures/LL%20Add%20Head.png "Queue Add to Head")

### For Inserting into the Back of the List / the Tail
###### <b>Note:</b> be sure to check that the list isn't empty before adding(`self.tail is None`). If so, just set the head and tail pointers to the new node
1. Create a new node (`new_node = LinkedList.Node(value)`)
2. Set the <b>prev</b> pointer of the new node to the current tail node (`new_node.prev = self.tail`)
3. Set the <b>next</b> pointer of the current tail to the new node (`self.head.next = new_node`)
4. Set the <b>tail</b> pointer to the new Node (`self.tail = new_node`)

Example: 

![Alt](/pictures/LL%20Add%20Tail.png "Queue to Tail")

<br>

### For Inserting into the Middle
###### <b>Note:</b> insertion comes after the chosen node. We'll call it `current` down below. If either the <b>head</b> or <b>tail</b> come back as none, then set both head and tail to th enew node.
1. Create a new Node (`new_node = LinkedList.Node(value)`)
2. Set the <b>prev</b> of your new node to the current node (`new_node.prev = current`)
3. Set the <b>next</b> of the new node to the next node after `current` (`new_node.next = current.next`)
4. Set the <b>prev</b> of the <b>next</b> node after `current` to the new node (`current.next.prev = new_node`)
5. Set the <b>next</b> of `current` to the new node (`current.next = new_node`)

Example:

![Alt](/pictures/LL%20Insert.png "Queue Insert")

<br>

### Removing from the Head / Front of the list
1. Set the <b>prev</b> of the second node to nothing (`self.head.next.prev = None`)
2. Set the <b>head</b> to be the second node (`self.head = self.head.next`)

Example:

![Alt](/pictures/LL%20Remove%20Head.png "Queue Remove Head")

<br>

### Removing from the Tail / back of the List
1. Set the <b>next</b> of the second to last node to nothing (`self.tail.prev.next = None`)
2. Set the <b>tail</b> to be the second to last node (`self.tail = self.tail.prev`)

Example:

![Alt](/pictures/LL%20Remove%20Tail.png "Queue Remove Tail")

<br>


### Removing from the Middle
###### <b>Note:</b> We are using the name `current` here again. `current` is the node we are removing.
1. Set the <b>prev</b> of the node after `current` to the node before `current` (`current.next.prev = current.prev`)
2. Set the <b>next</b> of the node before `current` to the node after `current` (`current.prev.next = current.next`)

Example:

![Alt](/pictures/LL%20Remove.png "Queue Remove from Middle")

<br>

## All Commands

Operation | Description | Code Example(Python) | Big O Notation
-------- | -------- | -------- |----------
<b>insert_head(value) | This adds the value before the Head | `my_deque.appendleft(value)` | O(1) - Just nead to adjust the head pointer
<b>insert_tail(value) | This adds the value after the tail | `my_deque.append(value)` | O(1) - Only need to adjust the the tail pointer
<b>insert(i, value) | This adds the value after the specified "i" node | `my_deque.insert(i, value)` | O(n) - The actual adding the value isn't complicated, but a loop is needed to find the right place
<b>remove_head() | Removes the Head/first item | `value = my_deque.popleft()` | O(1) - Only need to adjust the head pointer when you remove it
<b>remove_tail(index) | This removes the last item/the tail | `value = my_deque.pop()` | O(1) - Only need to adjust the tail pointer when you remove it
<b>remove(i) | This removes the "i" node | `my_deque.append(value)` | O(n) - Needs a loops to find the right node, but updating the head and tail pointers is simple
<b>size() | This returns the size of the linked list | `length = len(my_deque)` | O(1) - The size is maintained within the linked list class
<b>empty() | This returns true of the length of the linked list is zero, aka if the list is empty. | `if len(my_deque) == 0:` | O(1) - Only needs to compare the length with 0


## Example
Now, knowing what you know about linked lists, we are going to try to iterate through one till you find a specific value.

First, you are given an Stub function, like this.
``` Python 
def find_Value(self, data):
    # Nothing here yet. ADD CODE!
```
Next, we need to tell the function where we are going to start. We need to tell it a specific function to look at first. The best option is either the head or the tail, either works. Just remember this choice in the next step. 
``` Python 
def go_forward(self, data):
    # sets up current
    current = self.head
```
Now we need to do the actual loop. There are multiple ways to do this, but this example uses a while loop. What you do inside the loop is up to you, but As an example we chose to print each value until the right one is found.
``` Python 
def go_forward(self, data):
    # sets up current
    current = self.head

    # loops until the the desired link(containing data) is reached
    while current is not data:
            # do something here with the link
            print(current)
            # set pointer to the next link
            current = current.next
```
Now, keep in mind, that if you started with tial rather than head here, the last line would be `current = current.prev` instead.

## Problem to Solve

Your Problme, should you choose to solve it, is this:
you have a Chain full of links that are labeled with numbers. Your job is to write a function to find all the duplicate numbers in the list and print out just the duplicate numbers. Don't worry about how many duplicates there are, we just want to know which ones have duplicates.

* [Linked List Problem](/Python/Linked%20List%20Problem.py)
* [Linked List Solution](/Python/Linked%20List%20Solution.py)