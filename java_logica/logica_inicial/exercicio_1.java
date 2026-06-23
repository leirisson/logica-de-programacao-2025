package logica_inicial;
import java.util.Scanner;

public class exercicio_1 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o primeiro número: ");
        int a = scanner.nextInt();

        System.out.print("Digite o segundo número: ");
        int b = scanner.nextInt();

        int resultado = a + b;
        System.out.println("Resultado: " + resultado);

        scanner.close();
    }
}