import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        taskOne();
        taskTwo();
        taskThree();
    }

    static void taskOne() {
        /*
         Скласти програму, яка б повідомляла, що Джон народився у 1940 р.,
         запитувала, який тепер рік, і видавала вік Джона.
        */

        Scanner scan = new Scanner(System.in);
        System.out.println("Завдання 1: \n");

        int johnBirth = 1940;
        System.out.println("Джон народився у " + johnBirth + " р.");

        System.out.print("Введіть який зараз рік: ");
        int currentYear = scan.nextInt();
        int johnAge = currentYear - johnBirth;

        System.out.println("Вік Джона: " + johnAge);
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