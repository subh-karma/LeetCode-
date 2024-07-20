package assignment2;

import java.util.Vector;
import java.util.Iterator;

public class MyVector {
    public static void main(String[] args) {
        // Create a Vector
        Vector<Object> myVector = new Vector<Object>();

        // Print capacity of the Vector
        System.out.println("Initial capacity of myVector: " + myVector.capacity());

        // Check if the Vector is empty
        if (myVector.isEmpty()) {
            System.out.println("myVector is empty");
        } else {
            System.out.println("myVector is not empty");
        }

        // Add 4 objects to the Vector
        myVector.add(new Integer(10));
        myVector.add(new Float(3.14f));
        myVector.add("Hello");
        myVector.add(new StringBuffer("World"));

        // Display all elements of the Vector
        System.out.print("All elements in myVector: ");
        Iterator<Object> iterator = myVector.iterator();
        while (iterator.hasNext()) {
            System.out.print(iterator.next() + " ");
        }
        System.out.println();

        // Delete all elements in the Vector
        myVector.clear();

        // Check if the Vector is empty again
        if (myVector.isEmpty()) {
            System.out.println("myVector is empty");
        } else {
            System.out.println("myVector is not empty");
        }
    }
}


