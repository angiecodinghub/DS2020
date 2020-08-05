# NTU_DS2020

* Homework 1:<br/>
  This programming assignment asks you to read in a series of commands and execute it using **stack** and **queue**.<br/>
  However, you should be able to implement stacks and queues with **O(1)**.<br/>
  Input | Output
  ------| ------
  PUSH 10 | >> Node(00010)
  PUSH 9 | >> Node(00010) >> Node(00009)
  POP | >> Node(00009)
  PUSH 8 | >> Node(00009) >> Node(00008)
  PUSH 7 | >> Node(00009) >> Node(00008) >> Node(00007)
  PUSH 6 | >> Node(00009) >> Node(00008) >> Node(00007) >> Node(00006)
  POP | >> Node(00008) >> Node(00007) >> Node(00006)
  POP | >> Node(00007) >> Node(00006)
* Homework 2:<br/>
  Implement **regular expression matching**. Rules for pattern are as below:<br/>
  a. '.' Matches any single character.<br/>
  b. '*' Matches zero or more of the preceding element.<br/>
  It is worth noting that the pattern should match the entire input text.<br/>
  Input | Output
  ------| ------
  text = ”ab”, pattern = ”.*” | true
* Homework 3:<br/>
  You're going to implement a **BS Tree**. Your BS Tree needs to have the following functions:<br/>
  1. insert()<br/>
  The key in each node must be greater than any key stored in the left sub-tree, and less than any key stored in the right sub-tree. <br/>
  1. delete() <br/>
  The function remove a node which key equals to the input value. If the given key value is not in the current tree, don't modify the tree.<br/>
  1. preorder() <br/>
  Print the current tree in the preorder traversal sequence. <br/>
  1. inorder() <br/>
  Print the current tree in the inorder traversal sequence. <br/>
* Homework 4: <br/>
  You're going to implement a **min heap**. Your min heap needs to have the following functions: <br/>
  1. insert() <br/>
  The key in each node is less than every child nodes. <br/>
  1. delMin() <br/>
The function will pop out the smallest node in the heap, and maintain the heap structure within the rest elements. <br/>
* Homework 5: <br/>
  You are going to implement a **hash table**. Your hash table needs to have the following functions: <br/>
  1. Insert n <br/>
  Please insert the item n into the hash table. <br/>
  1. Look k<br/>
  Please print out all the items of the kth slot. If there are no items, please output Null. <br/>
  1. Delete n <br/>
  If n is in the hash table, delete n. If n is not in the hash table, please output Error. <br/>
  1. Search n <br/>
  If n is in the hash table, output Yes. If not, output No. <br/>
  1. End <br/>
  end of input.
