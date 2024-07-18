package assignment2;

import java.util.LinkedList;
import java.util.Iterator;

public class ColorsLinkedList {
    public static void main(String[] args) {
        // Create a LinkedList of Colors
        LinkedList<String> colorsList = new LinkedList<String>();
        colorsList.add("Red");
        colorsList.add("Green");
        colorsList.add("Blue");
        colorsList.add("Yellow");

        // Display all colors using an Iterator
        System.out.print("All colors in colorsList: ");
        Iterator<String> iterator = colorsList.iterator();
        while (iterator.hasNext()) {
            System.out.print(iterator.next() + " ");
        }
        System.out.println();

        // Add two new colors at the beginning of the list
        colorsList.addFirst("Orange");
        colorsList.addFirst("Purple");

        // Remove the last color from the list
        colorsList.removeLast();

        // Display the updated list
        System.out.print("Updated colorsList: ");
        for (String color : colorsList) {
            System.out.print(color + " ");
        }
        System.out.println();
    }
}


