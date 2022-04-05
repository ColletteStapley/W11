# Tree's

[Introduction Page](0-Introduction.md)

## Introduction

Tree's. Something we see all the time, and is actually pretty useful as a data structure. But how can a tree be used as a data structure? Simple, using the Binary search sytem. You take value, compare it to another value, and decide if it's larger or not. If it's larger, it goies down the right branch. If there is another value there, then the comparison happens again. Each branch connects a value to another value, in a seemingly complex but actually simple sytem. Each value has three branches, the previous value already compared against, the left branch for smaller values, and the right branch for larger values. 

## Binary Tree's

Binary Search Tree's, aka BST is the exactly what it sounds like. Using a well-known structure of a tree, and the use of numbers to build a unique data structure. It, like most data structures, is built of nodes. Each node has a key, or value, and this key is used to build the tree. The pieces you need to know are as follows: The root, parent, child, and leaf/leaves.

![Alt](/pictures/Tree%20diagram.png "Tree")

Root - The Root is where we start with a tree. Think of it like the trunk of the tree. It holds everything together. The root is the first node of the structure that you look at. It is what the whole structure is built off of. 

Parent - From the root, starting each subtree, is a parent node. Each parent node has a left branch and a right branch, and a third branch going backwards in the tree.. The difference between the parent node and the root is that the root doesn't have the third, backwards branch.

Child - The child node is any node that comes after a parent node. The interesting part is that a child node can also be a parent node. It just depends on which node you are looking at. Child nodes have their own branches; left, right, and backwards.

Leaf/Leaves - The leaves are special child nodes. The difference is that the leaves have no children themselves. They are the end of the branch. If you wanted to further travers the tree, you'd have to backtrack.

## Commands

Common BST Operation | Description | Code? | Big O Notation
----- | ----- | ----- | -----
<b>insert(valule) | Insert a Value into the tree | `code here` | O(log n) - Recursively Search the Subtrees to find the next avaliable spot
<b>remove(value) | Remove a value from the tree | `code here` | O(log n) - Recursively search the subtrees to find the value and remove it, require cleanup of affected nodes
<b>Contains(value) | Determine if a value is in the tree | `code here` | O(log n) - Recursively search the subtrees to find the value
<b>traverse_forward | visit all objects from smallest to largest | `code here` | O(n) - Recursively travese the left subtree, then the right subtree
<b>traverse_reverse | Visit all objecst from largest to smallest | `code here` | O(n) - Recursively traverse the right subtree, then the left subtree
<b>height(node) | Determine ht eheight of a node. If the height of the tree is needed, the root node is provided. | `code here` | O(n) - Recursively find the height of the left and right subtrees and then return the maximun height (plus one to accound for the root)
<b>size() | Return the size of the BST | `code here` | O(1) - The size is maintained within the BST class
<b> empty() | Returns true if the root node is empty, same as size = 0 | `code here` | O(1) - The comparison of the root node of the size


## Example

Now, to solve a simple problem with a tree. I'm going to have you 

## Problem to Solve

I don't know if this will be better or worse than the previous one.