import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        TaskTwo taskTwo = new TaskTwo();
        taskTwo.taskTwo();
    }

    static void taskOne() {
        /*
         Ввести 3 числа, вибрати й надрукувати найменше з них.
        */

        Scanner scan = new Scanner(System.in);
        System.out.println("Завдання 1: \n");
        int[] nums = new int[3];

        System.out.print("Введіть перше число: ");
        nums[0] = scan.nextInt();

        System.out.print("Введіть друге число: ");
        nums[1] = scan.nextInt();

        System.out.print("Введіть третє число: ");
        nums[2] = scan.nextInt();

        int min = nums[0];

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < min) {
                min = nums[i];
            }
        }

        System.out.println("Найменше число: " + min);

    }
    static  void taskTwo() {
        /*
        Скласти програму, яка вводила б 2 числа в форматі f,
        знаходила їх суму, добуток і виводила б результат на екран.
         */

        Scanner scan = new Scanner(System.in);
        System.out.println("Завдання 2: \n");
        System.out.print("Введіть перше число в форматі f: ");
        float firstNumber = scan.nextFloat();
        System.out.print("Введіть друге число в форматі f: ");
        float secondNumber = scan.nextFloat();

        float sum = firstNumber + secondNumber;
        float product =  firstNumber * secondNumber;

        System.out.printf("Сума чисел: %.2f\n", sum);
        System.out.printf("Добуток чисел: %.2f\n", product);
    }

    static void taskThree() {
        /*
        Скласти програму для виводу шапки i одного рядка машинограми
         */

        ArrayList<String[]> typewriter = new ArrayList<>();
        System.out.println("Завдання 3: \n");

        typewriter.add(new String[]{"Код матеріалу", "Назва матеріалу", "Ціна матеріалу"});

        typewriter.add(new String[]{"001", "Цвяхи", "5.50"});
        typewriter.add(new String[]{"002", "Молоток", "120.00"});
        typewriter.add(new String[]{"003", "Пилка", "75.25"});


        for (String[] row : typewriter) {
            if (row == typewriter.get(2)) {break;}
            for (String info : row) {
                System.out.printf("%-20s ", info);
            }
            System.out.println();
        }
    }
}