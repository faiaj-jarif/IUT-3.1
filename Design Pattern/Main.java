// 1. Strategy Interface: defines the common action
interface PaymentMethod {
    void pay(double amount);
}

// 2. Concrete Strategies: each class holds one specific algorithm
class CreditCardPayment implements PaymentMethod {
    private String cardNumber;

    public CreditCardPayment(String cardNumber) {
        this.cardNumber = cardNumber;
    }

    @Override
    public void pay(double amount) {
        System.out.println("Paid $" + amount + " using Credit Card: " + cardNumber);
    }
}

class MobileBankingPayment implements PaymentMethod {
    private String phoneNumber;

    public MobileBankingPayment(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    @Override
    public void pay(double amount) {
        System.out.println("Paid $" + amount + " via Mobile Banking: " + phoneNumber);
    }
}

class CashPayment implements PaymentMethod {
    @Override
    public void pay(double amount) {
        System.out.println("Paid $" + amount + " in Cash.");
    }
}

class HabiJabi implements PaymentMethod {
    @Override
    public void pay(double amount) {
        System.out.println("Habi jabi: " + amount);
    }
}

// 3. Context Class: delegates the work to whichever strategy is set
class ShoppingCart {
    private PaymentMethod paymentMethod;

    // Lets the client swap the strategy at runtime
    public void setPaymentMethod(PaymentMethod paymentMethod) {
        this.paymentMethod = paymentMethod;
    }

    public void checkout(double totalAmount) {
        paymentMethod.pay(totalAmount);
    }
}

// 4. Client: chooses the strategy dynamically
public class Main {
    public static void main(String[] args) {
        ShoppingCart cart = new ShoppingCart();

        PaymentMethod ccp = new CreditCardPayment("1234-5678-9012");

        // First purchase: pay by credit card
        cart.setPaymentMethod(ccp);
        cart.checkout(150.00);

        System.out.println();
        System.out.println();


        // Second purchase: switch strategy at runtime without changing ShoppingCart
        PaymentMethod mbp = new MobileBankingPayment("01700-000000");
        cart.setPaymentMethod(mbp);
        cart.checkout(85.50);


        System.out.println();
        System.out.println();

        cart.setPaymentMethod(new HabiJabi());
        cart.checkout(420);
    }
}