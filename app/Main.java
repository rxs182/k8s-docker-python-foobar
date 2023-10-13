import java.sql.Timestamp;

class Main {
    public static void main(String args[]) {
        while (true) {
            Timestamp ts = new Timestamp(System.currentTimeMillis());
            System.out.println("Java simulated process: " + ts.toString());
            try {
                Thread.sleep(3000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
    }
}