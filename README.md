# Super30 Python Loop Task 1

## Objective

Build strong fundamentals in iteration using for, range(),
strings, lists, tuples, sets, and dictionaries.

## Questions and Approach

### Q1. Print Numbers from 1 to 100

Used a for loop with range() to iterate from 1 to 100.

### Q2. Print Even Numbers

Used a for loop and the modulus operator.
Numbers divisible by 2 are printed.

### Q3. Print Odd Numbers

Used a for loop and checked whether each number is not
divisible by 2.

### Q4. Multiplication Table

Accepted an integer from the user and used a loop to
generate its multiplication table from 1 to 20.

Sample Input:
5

Sample Output:
5 x 1 = 5
5 x 2 = 10
...
5 x 20 = 100

### Q5. Sum from 1 to n

Used a loop and an accumulator variable called total
to calculate the sum without using sum().

Sample Input:
5

Sample Output:
Sum: 15

### Q6. Factorial

Used a loop and a factorial variable to multiply all
numbers from 1 to the given number.

Sample Input:
5

Sample Output:
Factorial: 120

### Q7. Divisible by 3

Iterated through the given list and printed only the
numbers whose remainder after division by 3 is zero.

### Q8. Language Length

Iterated through the list of languages and used len()
to print the length of each language.

### Q9. Dictionary Key and Value

Used dictionary.items() to iterate through every key
and its corresponding value.

### Q10. Count Vowels

Iterated through the user-provided string and checked
whether each character belongs to the vowel collection.

Sample Input:
Hello World

Sample Output:
Number of vowels: 3

### Q11. Reverse String

Used a for loop to construct the reversed string.
The slicing operator [::-1] and reversed() were not used.

Sample Input:
Python

Sample Output:
nohtyP

### Q12. Largest Number

Started with the first list element as the largest value
and compared every remaining number using a loop.
max() was not used.

## Concepts Practiced

- for loop
- range()
- strings
- lists
- dictionaries
- conditional statements
- modulus operator
- user input
- loops and accumulators


PS E:\super30-python-loop-task-1> py "01_print_1_to_100.py"
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
PS E:\super30-python-loop-task-1> py "02_even_numbers.py"
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
100
PS E:\super30-python-loop-task-1> py "03_odd_numbers.py"
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
51
53
55
57
59
61
63
65
67
69
71
73
75
77
79
81
83
85
87
89
91
93
95
97
99
PS E:\super30-python-loop-task-1> py "04_multiplication_table.py"
Enter a number: 4
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40
4 x 11 = 44
4 x 12 = 48
4 x 13 = 52
4 x 14 = 56
4 x 15 = 60
4 x 16 = 64
4 x 17 = 68
4 x 18 = 72
4 x 19 = 76
4 x 20 = 80
PS E:\super30-python-loop-task-1> py "05_sum_1_to_n.py"
Enter n: 7
Sum: 28
PS E:\super30-python-loop-task-1> py "06_factorial.py"
Enter n: 5
Sum: 15
PS E:\super30-python-loop-task-1>  py "06_factorial.py"
Enter a number: 5
Factorial: 120
PS E:\super30-python-loop-task-1> py "07_divisible_by_3.py"
12
9
33
42
15
PS E:\super30-python-loop-task-1> py "08_language_lengths.py"
PS E:\super30-python-loop-task-1> py "08_language_lengths.py"
Python -> 6
Java -> 4
C++ -> 3
JavaScript -> 10
Go -> 2
PS E:\super30-python-loop-task-1> py "09_dictionary_key_value.py"
name : Rahul
age : 22
course : Data Science
city : Bangalore
PS E:\super30-python-loop-task-1> py "10_count_vowels.py"
Enter a string: hello
Number of vowels: 2
PS E:\super30-python-loop-task-1> py "11_reverse_string.py"
Enter a string: python
Original string: python
Reversed string: nohtyp
PS E:\super30-python-loop-task-1> py "12_largest_number.py"
Largest number: 89
