// 1. Abstract Base Class: defines the skeleton of the algorithm
abstract class CaffeineBeverage {

    // Template Method: marked 'final' so subclasses cannot change the step order
    public final void prepareRecipe() {
        boilWater();
        brew();
        pourInCup();
        addCondiments();
    }

    // Shared steps: implemented once in the base class
    private void boilWater() {
        System.out.println("Boiling water...");
    }

    private void pourInCup() {
        System.out.println("Pouring into cup...");
    }

    // Customizable steps: subclasses must provide their own implementation
    protected abstract void brew();
    protected abstract void addCondiments();
}

// 2. Concrete Subclass 1: overrides only the varying steps
class Tea extends CaffeineBeverage {
    @Override
    protected void brew() {
        System.out.println("Chai Pattiii...");
    }

    @Override
    protected void addCondiments() {
        System.out.println("Lebu Khabooo...");
    }
}

// 3. Concrete Subclass 2: overrides only the varying steps
class Coffee extends CaffeineBeverage {
    @Override
    protected void brew() {
        System.out.println("COFEEE bhalo...");
    }

    @Override
    protected void addCondiments() {
        System.out.println("Dudh-Modhu...");
    }
}

// 4. Client: calls the template method on each concrete subclass
public class Main2 {
    public static void main(String[] args) {
        Tea tea = new Tea();
        System.out.println("Making tea:");
        tea.prepareRecipe();

        System.out.println();
        System.out.println();
        System.out.println();

        Coffee coffee = new Coffee();
        System.out.println("Making coffee:");
        coffee.prepareRecipe();
    }
}
