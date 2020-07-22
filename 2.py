'''
最好一样
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 131072KB；其他语言 655360KB
题目描述：
给出一个序列包含n个正整数的序列A，然后给出一个正整数x，你可以对序列进行任意次操作的，每次操作你可以选择序列中的一个数字，让其与x做按位或运算。你的目的是让这个序列中的众数出现的次数最多。

请问众数最多出现多少次。

输入
输入第一行仅包含两个正整数n和x，表示给出的序列的长度和给定的正整数。(1<=n<=100000,1<=x<=1000)

接下来一行有n个正整数，即这个序列，中间用空格隔开。(1<=a_i<=1000)

输出
输出仅包含一个正整数，表示众数最多出现的次数。


样例输入
5 2
3 1 3 2 5
样例输出
3

提示
样例解释
例如如果序列中所有数字都不修改时，众数为3，3出现的次数为2，如果我们把两个3都做如题操作，序列会变为1，1，1，2，5，此时众数为1，出现次数为3，所以我们选择后者方案，输出众数出现的次数，即3。
'''
# 5 2
# 3 1 3 2 5
import collections
while 1:
    s1 = input()
    if s1 == "":
        break
    n, x = int(s1.split(" ")[0]), int(s1.split(" ")[1])

    s2 = input()
    a = s2.split(" ")
    nums = []
    for item in a:
        nums.append(int(item))
    counter = collections.Counter(nums)

    res = 0
    # 特判
    if x == 1:
        for k, v in counter.items():
            res = max(res, v)
        print(res)
        continue

    for num in nums:
        if num | x != num:
            counter[num | x] = counter.get(num | x, 0) + 1

    for k, v in counter.items():
        res = max(res, v)
    print(res)

'''
# 祝桑代码 AC
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(){
 int dp[30000];
 memset(dp, 0, sizeof(dp));
 int n=0, x = 0;
 scanf("%d %d", &n, &x);
 int inputs[n];
 for(int i=0; i<n; i++){
  scanf("%d", &inputs[i]);
 }
 for(int i=0; i<n; i++){
  dp[inputs[i]]++;
  if((inputs[i] | x)!=inputs[i])
   dp[inputs[i]|x]++;
 }
 int maxnums = dp[0];
 for(int i=0; i<30000; i++){
  if(dp[i]>maxnums){
   maxnums = dp[i];
  }
 }
 printf("%d\n", maxnums);
 return 0;
}
'''