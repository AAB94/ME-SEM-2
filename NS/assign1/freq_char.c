#include<stdio.h>
int main(){
    FILE *fr = fopen("./onlytext.txt","r");
    int arr[26] = {0},c;
    while((c=fgetc(fr)) != EOF){
        arr[c - 'A'] = arr[c - 'A'] + 1; 
    }
    fclose(fr);
    int i,max = -1,j;
    for(i = 0; i < 26; ++i){
        if(max < arr[i]){
            j = i;
            max = arr[i];
        }
    }
    for( i = 0;i<26; ++i){
        printf("%c %d\n",i+'A',arr[i]);
    }
    return 0;
}
