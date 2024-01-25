import java.util.Scanner;

public class VowelAge {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        String name = input.nextLine();
        String age = input.nextLine();
        int a = Integer.parseInt(age);
        int i;
        int l=name.length();
        char ch;
        int c=0;
        for (i=0; i<l; i++){
            ch=name.toLowerCase().charAt(i);
            if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u')
            c++;
        }
        if (a < 18){
            System.out.println("Hello "+name+", you have "+c+" vowels, and you are a minor");
        }else {
            System.out.println("Hello "+name+", you have "+c+" vowels, and you are an adult");
        }
        input.close();
    }
}