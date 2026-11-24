// 1. Product Interface: shared blueprint for all objects the factory creates
interface Pizza {
    void prepare();
}

// 2. Concrete Products: specific classes to instantiate
class CheesePizza implements Pizza {
    @Override
    public void prepare() {
        System.out.println("Preparing Cheese Pizza with mozzarella and tomato sauce.");
    }
}

class PepperoniPizza implements Pizza {
    @Override
    public void prepare() {
        System.out.println("Preparing Pepperoni Pizza with sliced pepperoni.");
    }
}

class VeggiePizza implements Pizza {
    @Override
    public void prepare() {
        System.out.println("Preparing Veggie Pizza with peppers, onions, and olives.");
    }
}

// 3. Simple Factory: creates and returns the right instance based on input
class PizzaFactory {
    public Pizza createPizza(String type) {
        if (type.equalsIgnoreCase("cheese")) {
            return new CheesePizza();
        } else if (type.equalsIgnoreCase("pepperoni")) {
            return new PepperoniPizza();
        } else if (type.equalsIgnoreCase("veggie")) {
            return new VeggiePizza();
        }
        throw new IllegalArgumentException("Unknown pizza type: " + type);
    }
}

// 4. Client: requests the object from the factory instead of using 'new' directly
class PizzaStore {
    private PizzaFactory factory;

    public PizzaStore(PizzaFactory factory) {
        this.factory = factory;
    }

    public Pizza orderPizza(String type) {
        // Delegates object creation to the factory
        Pizza pizza = factory.createPizza(type);
        pizza.prepare();
        return pizza;
    }
}

public class Main1 {
    public static void main(String[] args) {
        PizzaFactory factory = new PizzaFactory();
        PizzaStore store = new PizzaStore(factory);

        store.orderPizza("cheese");
        store.orderPizza("pepperoni");
    }
}