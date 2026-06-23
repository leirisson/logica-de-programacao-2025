package logica_inicial;
import java.util.Scanner;


public class exercicio_2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Qual o seu nome: ");
        String nome = scanner.nextLine();

        System.out.print("Qual a sua idade: ");
        int idade = scanner.nextInt();

        System.out.print("Qual o seu sálario: ");
        double salario = scanner.nextDouble();


        System.out.println("Nome: " + nome);
        System.out.print("Idade: " + idade + "anos");
        System.out.printf("Sálario: R$ %.2f%n",  salario);
    }
}
