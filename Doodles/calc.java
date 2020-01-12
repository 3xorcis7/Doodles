import java.util.*;

 // Compiler version JDK 11.0.2

 class Dcoder
 {
   public static void main(String args[])
   { 
    Scanner scan = new Scanner(System.in);
    System.out.println("Addition = 1, Subtraction = 2,");
    System.out.println("Multiplication = 3, Division = 4");
    int calculation = scan.nextInt();
    
    if (calculation ==1){
      System.out.print("First number: ");
      int first = scan.nextInt();
      System.out.print("Second number: ");
      int second = scan.nextInt();
      int sum = first + second;
      System.out.println("Sum = " + sum);
    }
    if (calculation ==2){
      System.out.print("First number: ");
      int first = scan.nextInt();
      System.out.print("Second number: ");
      int second = scan.nextInt();
      int sum = first - second;
      System.out.println("Sum = " + sum);
    }
    if (calculation ==3){
      System.out.print("First number: ");
      int first = scan.nextInt();
      System.out.print("Second number: ");
      int second = scan.nextInt();
      int sum = first * second;
      System.out.println("Sum = " + sum);
    }
    if (calculation ==4){
      System.out.print("First number: ");
      int first = scan.nextInt();
      System.out.print("Second number: ");
      int second = scan.nextInt();
      double sum = first / second;
      System.out.println("Sum = " + sum);
    }
   }
 }