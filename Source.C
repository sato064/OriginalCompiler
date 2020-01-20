#include <stdio.h>
int main(){

int abc;
int b;
int r;
int tmp;

scanf("%d",&abc);
scanf("%d",&b);

if(abc<b){
tmp=abc;
abc=b;
b=tmp;
}
r=abc%b;
while(r!=0){
abc=b;
b=r;
r=abc%b;
}

printf("%d",b);

}
