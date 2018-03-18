#include<stdio.h>
#include<ctype.h>

int main(){
    char key[] = {'E','D','G','A','R','C','O','D','D'};
    int i = 0, temp = 0, x;
    int count = 0;
    char c;
    FILE *fr,*fw;
    fr = fopen("./Assignment","r");
    fw = fopen("./final.txt","w");
    while((c=fgetc(fr)) != EOF){
        if( c >= 'a' && c <= 'z'){
            c = c - 'a';
            temp = (key[i] - 'A' + count) % 26;
            ++i;
            if( i % 9 == 0){
                i = 0;
                ++count;
            }
            x = c - temp;
            if( x < 0 ){
                x = 26 + x;
            }
            c = x + 'a';   
            fputc(c,fw);
        }
        else if( c >= 'A' && c <= 'Z'){
            c = c - 'A';
            temp = (key[i] - 'A' + count) % 26;
            ++i;
            if( i % 9 == 0){
                i = 0;
                ++count;
            }
            x = c - temp;
            if( x < 0 ){
                x = 26 + x;
            }
            c = x + 'A';
            fputc(c,fw);
        }
        else{
            fputc(c,fw);
        }
    }
    fclose(fr);
    fclose(fw);     
    return 0;
}
