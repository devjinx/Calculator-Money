#include <stdio.h>
#include <unistd.h>
void main()
{
    //money is var and this programe can work with type some number that I mean put a number for money you want to keep
int money;
    //printf is show in cui or terminal
    //scanf is input to keep in var 
    //var = money in this programe
   printf("Press your money you wanna keep");
   scanf("%d",&money);
   //now / = Division
   printf("Your money you wanna keep is %d \n",money);
   //this line show money you shouble to keep
   printf("Money You should to keep of 1 Month is %d \n",money/12);
   printf("Thank for use this programe");
   //pause for read in cui or terminal for 30sec
   sleep(30);
   //after is end and out
   }