#include<stdio.h>
#include<ctype.h>
int main(){
    char c;
    FILE *fr,*fw;
    fr = fopen("./Assignment","r");
    fw = fopen("./onlytext.txt","w+");
    while((c = fgetc(fr)) != EOF ){
        if((c >= 'A' && c <= 'Z') ||(c >= 'a' && c <= 'z')){
            fputc(toupper(c),fw);
        }
    }
    fclose(fr);
    fclose(fw);
    return 0;
}
