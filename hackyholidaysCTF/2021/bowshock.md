# Bowshock

[50 points]
BowShock

Can you find out how to minimize bow shock and prevent everything from turning into dust?
---

we are given a jar file, I decompiled it with jd_gui

```java
import java.util.InputMismatchException;
import java.util.Scanner;

class BowShock {
  public static int totalInput;
  
  public static int getInput() {
    int i;
    System.out.println("Set the amount of plasma to the correct amount to minimize bow shock: ");
    Scanner scanner = new Scanner(System.in);
    while (true) {
      try {
        i = scanner.nextInt();
        break;
      } catch (InputMismatchException inputMismatchException) {
        System.out.print("Invalid input. Please reenter: ");
        scanner.nextLine();
      } 
    } 
    totalInput += i;
    return i;
  }
  
  public static void bowShock() {
    System.out.println("And all was dust in the wind.");
    System.exit(-99);
  }
  
  public static void main(String[] paramArrayOfString) {
    System.out.println("Oh damn, so much magnetosphere around here!");
    if (getInput() != 333)
      bowShock(); 
    System.out.println("We survive another day!");
    if (getInput() != 942)
      bowShock(); 
    if (getInput() != 142)
      bowShock(); 
    System.out.println("Victory!");
    System.out.println("CTF{bowsh0ckd_" + totalInput + "}");
  }
}

```

reading the code, it is clear the flag will be "CTF{bowsh0ckd_" + (333+942+142) + "}"
giving us a flag of CTF{bowsh0ckd_1417}