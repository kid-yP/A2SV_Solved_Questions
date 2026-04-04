# 2065C2-Skibidus-and-Fanum-Tax-hard-version

**Problem:** [2065C2-Skibidus-and-Fanum-Tax-hard-version](https://codeforces.com/problemset/problem/2065/C2)

**time limit per test:** 2 seconds

**memory limit per test:** 256 megabytes

---

This is the hard version of the problem. In this version, m ≤q 2⋅ 10⁵.

Skibidus has obtained two arrays a and b, containing n and m elements respectively. For each integer i from 1 to n, he is allowed to perform the operation at most once:

 
-  Choose an integer j such that 1 ≤q j ≤q m. Set a_i := b_j - a_i. Note that a_i may become non-positive as a result of this operation. 
Skibidus needs your help determining whether he can sort a in non-decreasing order^{\text{∗}} by performing the above operation some number of times.

^{\text{∗}}a is sorted in non-decreasing order if a_1 ≤q a_2 ≤q … ≤q a_n.


**Input**

The first line contains an integer t (1 ≤q t ≤q 10⁴) — the number of test cases.

The first line of each test case contains two integers n and m (1 ≤q n ≤q 2 ⋅ 10⁵, 1 ≤q m ≤q 2⋅ 10⁵).

The following line of each test case contains n integers a_1, a_2, …, a_n (1 ≤q a_i ≤q 10⁹).

The following line of each test case contains m integers b_1, b_2, …, b_m (1 ≤q b_i ≤q 10⁹).

It is guaranteed that the sum of n and the sum of m over all test cases does not exceed 2 ⋅ 10⁵.


**Output**

For each test case, if it is possible to sort a in non-decreasing order, print "YES" on a new line. Otherwise, print "NO" on a new line.

You can output the answer in any case. For example, the strings "yEs", "yes", and "Yes" will also be recognized as positive responses.


**Example**

**Input**

```
5
1 3
5
9 1 1000000000
3 2
1 4 3
3 4
4 3
2 4 6 5
6 1 8
5 2
6 4 5 4 5
4 1000
3 1
9 8 7
8
```

**Output**

```
YES
NO
YES
NO
YES
```


**Note**

In the first test case, [5] is already sorted.

In the second test case, it can be shown that it is impossible.

In the third test case, we can set a_2:=b_1-a_2=6-4=2 and a_3:=b_3-a_3=8-6=2. The sequence [2,2,2,5] is in nondecreasing order.

In the last case, we can apply operations on each index. The sequence becomes [-1,0,1], which is in nondecreasing order.
