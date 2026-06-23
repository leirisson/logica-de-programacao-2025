package logica_inicial;

import java.util.Scanner;

public class exercicio_3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double desconto = 0.10;
        double total = 0.0;
        double valor_desconto = 0.0;
        double totalComDesconto = 0.0;
        System.out.print("Qual o valor do produto: ");
        double valorProduto = scanner.nextDouble();

        System.out.print("Qual a quantidade do produto: ");
        int qtd_produto = scanner.nextInt();

        total = valorProduto * qtd_produto;
        valor_desconto = total * desconto;
        totalComDesconto = total - valor_desconto;

        System.out.printf("Preço unitário: R$ %.2f%n", valorProduto);
        System.out.println("Quantidade: " + qtd_produto);
        System.out.printf("Total sem desconto: R$ %.2f%n", total);
        System.out.printf("Desconto: R$ %.2f%n ", valor_desconto);
        System.out.printf("Total com desconto:  R$ %.2f%n ", totalComDesconto);
    }
}
