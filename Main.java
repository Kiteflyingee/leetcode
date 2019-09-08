import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = "";
        while((line=sc.nextLine())!=null){
            String[] str = line.split(" ");
            double n = Double.parseDouble(str[0]);
            int m = Integer.parseInt(str[1]);

            double sum = n;
            for(int i=1; i<m; i++){
                n = Math.sqrt(n);
                sum += n;
            }
            System.out.printf("%.2f", sum);
            System.out.println();
        }
        sc.close();
    }
}