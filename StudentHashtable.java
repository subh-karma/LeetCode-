package assignment2;

import java.util.Hashtable;
import java.util.Iterator;
import java.util.Map;

public class StudentHashtable {
	public static void main(String[] args) {
		// Create a Hashtable named Student
		Hashtable<Integer, String> studentHashtable = new Hashtable<Integer, String>();

		// Add records of 5 students to the Hashtable
		studentHashtable.put(1, "Alice");
		studentHashtable.put(2, "Bob");
		studentHashtable.put(3, "Charlie");
		studentHashtable.put(4, "John");
		studentHashtable.put(5, "Emily");

		// Display the elements of the Hashtable
		System.out.println("Elements in studentHashtable:");
		for (Map.Entry<Integer, String> entry : studentHashtable.entrySet()) {
			System.out.println("Roll No: " + entry.getKey() + ", Name: " + entry.getValue());
		}

		// Remove student with name "John"
		studentHashtable.values().remove("John");

		// Display the updated elements of the Hashtable
		System.out.println("Updated elements in studentHashtable:");
		Iterator<Map.Entry<Integer, String>> iterator = studentHashtable.entrySet().iterator();
		while (iterator.hasNext()) {
			Map.Entry<Integer, String> entry = iterator.next();
			System.out.println("Roll No: " + entry.getKey() + ", Name: " + entry.getValue());
		}
	}
}
