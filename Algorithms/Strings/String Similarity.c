#include<stdio.h>
#include<string.h>
#define MAX 100001

/*Z-Algorithm*/
long compute_z(char str[]){
   long sum=0;
   int n = strlen(str);
   int z[n];
 
   sum = z[0] = n;
   long L = 0, R = 0;
   for (long i = 1; i < n; i++) {
      if (i > R) {
         L = R = i;
         while (R < n && str[R-L] == str[R]) R++;
         z[i] = R-L; R--;
      }
 
      else {
 
         int k = i-L;
         if (z[k] < R-i) z[i] = z[k];  //B = R-i
         else {
            L = i;
            while (R < n && str[R-L] == str[R]) R++;
            z[i] = R-L; R--;
         }
      }
      sum+=z[i];
   }
   return sum;
}

int main(){
    int T;
    scanf("%d",&T);
    
    int i;
    char str[T][MAX];
    for(i=0;i<T;i++){
        scanf("%s",&str[i]);
        printf("%lu\n",compute_z(str[i]));
    }
}