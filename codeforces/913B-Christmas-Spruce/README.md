# 913B-Christmas-Spruce

**Problem:** [913B-Christmas-Spruce](https://codeforces.com/problemset/problem/913/B)

**time limit per test:** 1 second

**memory limit per test:** 256 megabytes

---

Consider a rooted tree. A rooted tree has one special vertex called the root. All edges are directed from the root. Vertex *u* is called a child of vertex *v* and vertex *v* is called a parent of vertex *u* if there exists a directed edge from *v* to *u*. A vertex is called a leaf if it doesn't have children and has a parent.

Let's call a rooted tree a spruce if its every non-leaf vertex has at least 3 leaf children. You are given a rooted tree, check whether it's a spruce.

The definition of a rooted tree can be found here.


**Input**

The first line contains one integer *n* — the number of vertices in the tree (3 ≤ *n* ≤ 1 000). Each of the next *n* - 1 lines contains one integer *p**i* (1 ≤ *i* ≤ *n* - 1) — the index of the parent of the *i* + 1-th vertex (1 ≤ *p**i* ≤ *i*).

Vertex 1 is the root. It's guaranteed that the root has at least 2 children.


**Output**

Print "Yes" if the tree is a spruce and "No" otherwise.


**Examples**

**Input**

```
4
1
1
1
```

**Output**

```
Yes
```

**Input**

```
7
1
1
1
2
2
2
```

**Output**

```
No
```

**Input**

```
8
1
1
1
1
3
3
3
```

**Output**

```
Yes
```


**Note**

The first example:

![image](https://espresso.codeforces.com/a028cc3eb93ff24e14e12c093bc7fd0e0d9f7a1a.png)

The second example:

![image](https://espresso.codeforces.com/e6c7b518972d13e2572004d8ce21cda77de4c938.png)

It is not a spruce, because the non-leaf vertex 1 has only 2 leaf children.

The third example:

![image](https://espresso.codeforces.com/9af8f35bd8ce5823176fec24fc464c670bf95c3e.png)
