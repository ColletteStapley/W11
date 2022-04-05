# Queue's

[Introduction Page](0-Introduction.md)

## Introduction

Queue's are a handy data structure found in most languages. This tutorial is for the Python Lnaguage. 

## Types of Queues

Queues as a data structure are pretty straightforward. There are three main examples of a queue that may help explain what the Queue data structure is and how it works. This can be helpful in understanding the different uses of the queue data structure.

![Alt](/pictures/Queue%20Diagram.png "Queue")

### Cars in a Turn Lane

When there is a busy road and a packed turn lane, this is actually a great metaphore for a queue. Queues have a front and a back, and nothing can be iserted into the middle. Nothing can be added to the front. Cars can only join the turn lane from the back. 

<br>Think of it this way. There are three cars in the left turn lane at a light. The front car is blue, the middl car is black, and the last car is red. The blue car is called the <b>front</b> of the queue. The red car is the <b> back</b>. Cars can only join the line from the back, using what is called an <b>enqueue</b> operation. When that blue car turns, or is removed from the list, it is called a <b>dequeue</b> operation. When a <b>dequeue</b> operation happens, the rest of the items int he queue move forward, like the cars in the line moving forward to fill the empty space left by the departed Blue car. The white car is now the front of the line/ queue, and more cars can be added on behind the red car. 

### Vending Machines
There are plenty of easy examples of queues in life, like lines at a grocery store or food place. But there are plenty other examples too. Take a rolling shelf for example. Now this does not mean a shelf on wheels. This means a shelf with rows for rolling cans. It is controlled by gravity, and has rows of angled shelves. A can is added at the top of the sloped shelf, and it can only go down to the bottom of the slope. This makes it really hard to take the cans at the top of the stack first. You have to remove the can from the bottom where there is a spot for the can to be removed. When a can is removed, the rest of the cans fall/roll to fil the space.

### Git Hub

Git Hub is a great tool that most, if not all programmers are aquainted with. You have File in an online repository, or online storage place. Multiple peiple can have access to this file. WHen someone copies or <b>clones</b> the code to their computer, they have a private copy of the code. They can then edit the code all they want, and when they are satisfied, their changes can be pushed to the main file to be incorperated.   

<br> Though it is bad practice to push directly to main, this is the example we are working off of. When you have multiple people editing the same file on their personal computers, what happens when they push their changes? Queues solve this problem. The first person to push their changes to main gets them instantly updated. Then anyone who wants to push has to first pull the new additions to main to their personal computer. This adds the new data to your file while not getting rid of what you were trying to add. 

<br> Once the data from main has been incorporated into your existing files, you can push your changes back to main. This continues in a first-come first-serve type fashion. If someone pushes faster than you, then you have to pull their changes first before you can add your own. 

<br>Branches are super handy and actual are a much better solution to this problem, but it also involves extra work reincorporating all the changes made back into main. 

## Queue Commands

The commands for working with a queue are fairly simple. There are 4 main operations for the queue datastructure. 
 

Operation | Description | Code Example(Python) | Big O Notation
-------- | -------- | -------- |----------
<b>enqueue(value) | this is used to add a value to the back of the queue.| `my_queue.append(value)` | hi there
<b>dequeue() | Removes the item at the front of the queue. Two options: remove and return the front item or pop off index 0. | `value = my_queue[0], del my_queue[0]` <b>or</b> `value = my_queue.pop(0)` | hit there
<b>size() | This returns the size of the queue. | `length = len(my_queue)` | H there
<b>empty() | This returns true of the length of the queu is zero, aka if the queue is empty. | `if len(my_queue) == 0:` | thi there

## Example

hmmmm

## Problem to Solve

THIS ONE'S EVEN WORSE I FEEL LIKE I NEED SOMETHING THAT SHOWS HOW IT CAN BE USED IN MORE COMPLEX WAYS CUT I CAN'T THINK OF ANYTHING