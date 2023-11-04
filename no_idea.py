"""There is an array of n integers. There are also disjoint 2 sets, A and B, 
each containing m integers. You like all the integers in set A and dislike 
all the integers in set B. Your initial happiness is 0. For each i integer in 
the array, if i E A, you add 1 to your happiness. If i E B, you add -1 to your
happiness. Otherwise, your happiness does not change. Output your final 
happiness at the end.
Note: Since
A and B are sets, they have no repeated elements. 
However, the array might contain duplicate elements. 

Input Format
The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain integers, A and B, respectively.

Output Format
Output a single integer, your total happiness.

Sample Input
3 2
1 5 3
3 1
5 7

Sample Output
1

"""
n, m = input().split()
n = input().split()
A = set(input().split())
B = set(input().split())
happiness = 0
for n in n:
    if n in A:
        happiness += 1
    elif n in B:
        happiness -= 1
    else:
        continue
print(happiness)