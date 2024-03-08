# Longest Palindromic Subsequence

## Overview
This project presents a Python solution to the "Longest Palindromic Subsequence" problem. The goal is to find the length of the longest subsequence in a given string that is also a palindrome.

## Problem Statement
Given a string `s`, find the longest palindromic subsequence's length in `s`. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

## Solution Approach
The solution utilizes dynamic programming to build a table `dp` where `dp[i][j]` represents the length of the longest palindromic subsequence within the substring `s[i:j+1]`. The approach systematically builds up the solution for all substrings, ensuring that the optimal substructure property of dynamic programming is utilized.

### Complexity Analysis
- **Time Complexity**: O(n^2), where `n` is the length of the string. The solution iterates over all possible substrings, updating the `dp` table based on previous computations.
- **Space Complexity**: O(n^2), due to the storage requirements of the 2D dynamic programming table.

## How to Run
To execute the solution, run the Python script with a Python interpreter:
```bash
python longest_palindromic_subsequence.py
```