# Array Probelms

## [Problem 1:](two_sum.py) **Two Sum**

Given an array a of n numbers and a target value t, find two numbers whose sum is t.
- Example input: `a=[5, 3, 6, 8, 2, 4, 7], t=10`
- Should return: `[3, 7]` or `[6, 4]` or `[8, 2]`

---

## [Problem 2:](k_largest_values.py) **K Largest Values**
Given an array a of n numbers and a count k find the k largest values in the array a.
- Example input: `a=[5, 1, 3, 6, 8, 2, 4, 7], k=3`
- Should return: `[6, 8, 7]`

---

## [Problem 3:](two_array_two_sum.py) **Two Array Two Sum**
Given two arrays a and b of numbers and a target value t, find a number from each array whose sum is closest to t.
- Example input: `a=[9, 13, 1, 8, 12, 4, 0, 5],  b=[3, 17, 4, 14, 6],  t=20`
- Should return: `[13, 6]` or `[4, 17]` or `[5, 14]`

---

## [Problem 4:](twitter.py) **Twitter Follow Suggestions**
You’re working an internship at Twitter and are tasked to improve suggestions for accounts to follow, which already works great for established accounts because it uses content from your tweets and other accounts you follow to suggest new ones. However, when a new user signs up none of this information exists yet, but Twitter still wants to make some follow suggestions. Your team asked you to implement a function that accepts a new user’s handle and an array of many other users’ handles, which could be very long – Twitter has over 330 million active accounts! You need to calculate a similarity score between a pair of handles by looking at the letters each contains, scoring +1 for each letter in the alphabet that occurs in both handles but scoring –1 for each letter that occurs in only one handle. Your function should return k handles from the array that have the highest similarity score to the new user’s handle.

- Example input: 

```python
handles = ['DogeCoin', 'YangGang2020', 'HodlForLife', 'fakeDonaldDrumpf', 'GodIsLove', 'BernieOrBust']
suggest('iLoveDogs', handles, k=2)
```

- Should return: `['GodIsLove', 'DogeCoin']`