
| Data Structures      | Algorithms                 | Concepts                   |
|:---------------------|:---------------------------|:---------------------------|
| Linked Lists         | Breadth First Search       | Bit Manipulation           |
| Binary Trees         | Depth First Search         | Singleton Design Pattern   |
| Tries                | Binary Search              | Factory Design Pattern     |
| Stacks               | Merge Sort                 | Memory (Stack vs. Heap)    |
| Queues               | Quicksort                  | Recursion                  |
| Vectors / ArrayLists | Tree Insert / Find / e.t.c | Big-O Time                 |
| Hash Tables          |                            |                            |



For each of the topics above, make sure you understand how to use and implement them and, where applicable, what the space and time complexity is.


### Powers of 2 Table


| Power of 2  | Exact Value (X)    | Approx. Value  | X Bytes into MB, GB, e.t.c. |
|:------------|:-------------------|:---------------|:----------------------------|
| 7           | 128                |                |                             |
| 8           | 256                |                |                             |
| 10          | 1024               | 1 thousand     | 1 K                         |
| 16          | 65,536             |                | 64 K                        |
| 20          | 1,048,576          | 1 million      | 1 MB                        |
| 30          | 1,073,741,824      | 1 billion      | 1 GB                        |
| 32          | 4,294,967,296      |                | 4 GB                        |
| 40          | 1,099,511,627,776  | 1 trillion     | 1 TB                        |


Using this table, you could easily compute, for example, that a hash table mapping every 32-bit integer to a boolean value could fit in memory on a single machine.


### Step 1: Ask Questions

- What are the data types? 
- How much data is there?
- What assumptions do you need to solve the problem? 
- Who is the user?


### Step 2: Design an Algorithm

- What are its space and time complexity?
- What happens if there is a lot of data?
- Does your design cause other issues? For example, if you're creating a modified version of a binary search tree, did your design impact the time for insert, find, or delete?
- If there are other issues or limitations, did you make the right trade-offs? For which scenarios might the trade-off be less optimal?
- If they gave you specific data (e.g., mentioned that the data is ages, or in sorted order), have you leveraged that information? Usually there's a reason that an interviewer gave you specific information.


### Step 3: Pseudocode

### Step 4: Code

- Use Data Structures Generously
- Don't Crowd Your Coding

### Step 5: Test
