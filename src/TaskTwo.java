import java.util.Scanner;

public class TaskTwo {
    void taskTwo() {
        /*
        Не використовуючи операторів циклу, вводити й друкувати числа,
        поки не буде введений 0. Обчислити їх суму, кількість, середнє арифметичне.
         */
        Scanner scan = new Scanner(System.in);

        System.out.println("Вводьте числа (0 — для завершення):");

        Result result = input(scan, 0, 0);
        printResults(result);
    }

    Result input(Scanner scan, int sum, int count){
        int num = scan.nextInt();
        System.out.println("Введено: " + num);
        if (num == 0){
            return new Result(sum, count);
        } else {
            return input(scan, sum + num, count + 1);
        }
    }

    private static void printResults(Result result) {
        System.out.println("\nСума: " + result.sum);
        System.out.println("Кількість: " + result.count);

        if (result.count > 0) {
            double average = (double) result.sum / result.count;
            System.out.printf("Середнє арифметичне: %.2f\n", average);
        } else {
            System.out.println("Середнє арифметичне: не визначено (числа не вводились)");
        }
    }

    private static class Result {
        int sum;
        int count;

        Result(int sum, int count) {
            this.sum = sum;
            this.count = count;
        }
    }
}


