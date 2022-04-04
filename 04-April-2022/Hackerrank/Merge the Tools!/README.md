# Problem -> Merge the Tools!

Consider the following:

- A string,s, of length n where s = c0c1c2...cn-1.
- An integer,k, where k is a factor of n.
  We can split s into (n/k) substrings where each subtring,ti, consists of a contiguous block of k characters in s. Then, use each ti to create string ui such that:

- The characters in ui are a subsequence of the characters in ti.
- Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once. In other words, if the character at some index j in ti occurs at a previous index <j in ti, then do not include the character in string ui.
  Given s and k, print (n/k) lines where each line i denotes string ui.

### Example

```
s = 'AAABCADDE'
k = 3

There are three substrings of length '3' to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, so u1='A'. The second substring has all distinct characters, so u2='BCA'. The third substring has  different characters, so u3='DE'. Note that a subsequence maintains the original order of characters encountered. The order of characters in each subsequence shown is important.
```

### Function Description

Complete the merge_the_tools function in the editor below.

merge_the_tools has the following parameters:

- string s: the string to analyze
- int k: the size of substrings to analyze

### Prints

Print each subsequence on a new line. There will be (n/k) of them. No return value is expected.

### Input Format

The first line contains a single string, s.
The second line contains an integer, k , the length of each substring.

### Constraints

- 1<=n<=10\*\*4, where n is the length of s.
- It is guaranteed that n is a multiple of k.

### Sample Input

```
STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3

```

### Sample Output

```
AB
CA
AD
```

### Explanation

Split s into (n/k)=(9/3)=3 equal parts of length k=3 . Convert each ti to ui by removing any subsequent occurrences of non-distinct characters in ti:

```
- t0 ='AAB' --> u0 = 'AB'
- t1 ='CAA' --> u1 = 'CA'
- t2 ='ADA' --> u2 = 'AD'
```

Print each ui on a new line.
