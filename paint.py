#We have to estimate the cost of painting a property. Interior wall painting cost is Rs. 18 per sq.ft. and exterior wall painting cost is Rs. 12 per sq.ft. If a user enters zero as the number of walls then skip surface area values as user may don’t want to paint that wall and for any wrong input print "Invalid Input".

Input Format

Take input as
1. Number of interior walls 'n'
2. Number of exterior walls 'm'
3. Surface area of each interior wall in units of sq.ft.
4. Surface area of each exterior wall in units of sq.ft.

Constraints

0 <= n <= 10
0 <= m <= 10
n=int(input())
m=int(input())
t_cost=0
#Always look for constrain and apply it first and e=use exit function
if n<0 or n>10 or m<0 or m>10:
    print("Invalid Input")
    exit()
for i in range(n):
    tmp=float(input())
    t_cost = t_cost + tmp*18
for j in range(m):
    tmp=float(input())
    t_cost = t_cost + tmp*12 
print(f"Total Estimated Cost: {t_cost:.1f} INR")
