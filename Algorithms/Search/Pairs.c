#include <stdio.h>

typedef enum { false, true } bool;

bool binary_search(int a[],int n,int m,int l,int u);
int pairs(int a_size, int* a, int k);
void mergeSort(int arr[],int low,int mid,int high);
void partition(int arr[],int low,int high);

int main(){
   
    int res;
   
    int _a_size,_k,i;
    scanf("%d %d", &_a_size,&_k);
    int _a[_a_size];
    for(i = 0; i < _a_size; i++) { 
        int _a_item;
        scanf("%d", &_a_item);
        
        _a[i] = _a_item;
    }
    
    /*Merge Sort*/
    partition(_a,0,_a_size-1);
    
    /*Find pairs*/
    res=pairs(_a_size,_a,_k);
    printf("%d\n",res);    
    
    return 0;
}

int pairs(int a_size, int* a, int k) {
    int ans=0;    
    
    int i,ele;
    /*Create diff array*/
    int diff[a_size];
    for(i = 0; i < a_size-1; i++) { 
        diff[i] = a[i] - a[i+1];
    }
    
    /*Check k with diff*/
    for(i = 0; i < a_size-1; i++) { 
        if(i>0 &&(a[i]-a[a_size-1])<k)
            break;
        if(diff[i]>k)
            continue;
        else if(diff[i]==k)
            ans++;
        else {
            ele = a[i] - k;
            if(binary_search(a,a_size,ele,0,a_size-1))
                ans++;
        }
    }

    return ans;
}

bool binary_search(int a[],int n,int m,int l,int u){

     int mid;

     if(l<=u){
          mid=(l+u)/2;
          if(m==a[mid]){
              return true;
          }
          else if(m>a[mid]){
              // key is in lower subset
              return binary_search(a,n,m,l,mid-1);
          }
          else{
              // key is in upper subset
              return binary_search(a,n,m,mid+1,u);
          }
     }
     else
       return false;
}

void partition(int arr[],int low,int high){

    int mid;

    if(low<high){
         mid=(low+high)/2;
         partition(arr,low,mid);
         partition(arr,mid+1,high);
         mergeSort(arr,low,mid,high);
    }
}

void mergeSort(int arr[],int low,int mid,int high){

    int i,m,k,l,temp[100000];

    l=low;
    i=low;
    m=mid+1;

    while((l<=mid)&&(m<=high)){

         if(arr[l]>arr[m]){
             temp[i]=arr[l];
             l++;
         }
         else{
             temp[i]=arr[m];
             m++;
         }
         i++;
    }

    if(l>mid){
         for(k=m;k<=high;k++){
             temp[i]=arr[k];
             i++;
         }
    }
    else{
         for(k=l;k<=mid;k++){
             temp[i]=arr[k];
             i++;
         }
    }
   
    for(k=low;k<=high;k++){
         arr[k]=temp[k];
    }
}
