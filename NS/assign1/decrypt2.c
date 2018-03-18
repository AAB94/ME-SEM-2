#include<stdio.h>
#include<ctype.h>
#include<string.h>
int main(int argc, char **arg){
    if( argc < 3 ){
        printf("Error: ./decrypter KEY FILENAME");
        return -1;
    }
    char key[100];
    char filename[200];
    filename[0] = '.', filename[1] = '/';
    strcpy(key, arg[1]);
    strcat(filename, arg[2]);
    int i = 0, temp = 0, x, keylen = strlen(key);
    int count = 0;
    char c;
    FILE *fr,*fw;
    fr = fopen(filename,"r");
    fw = fopen("./final.txt","w");
    while((c=fgetc(fr)) != EOF){
        if( c >= 'a' && c <= 'z'){
            c = c - 'a';
            temp = (key[i] - 'A' + count) % 26;
            ++i;
            if( i % keylen == 0){
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
            if( i % keylen == 0){
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
