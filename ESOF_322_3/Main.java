package com.mycompany.assignment3;

import java.util.Scanner;

/**
 * Assignment #3 ESOF 322
 * @author Gage Hilyard/ghily
 */
public class Main {
    public static void main(String[] args) {
        //Example of the Strategy Pattern. Exercise from Head First Design Patterns
        /*To demonstrate runtime changes I made just one Inventory instance
        * that can change its sorting algorithm on the fly
        */
        Scanner user = new Scanner(System.in);
        
        InventoryModule Inventory1 = new InventoryModule();
        
        //loop to test runtime
        Boolean loop = true;
        System.out.println("Sorting algorithms: bubble, merge, insertion, quick.");
        System.out.println("Type 'sort' to sort and type 'quit' to end.");
        System.out.println("Please enter sort algorithm: ");
        while(loop != false){
            String selection = user.nextLine();
            
            //pick sorting algo
            switch (selection.toLowerCase()) {
                case "bubble":
                    Inventory1.setSortStrategy(new BubbleSort());
                    break;
                case "merge":
                    Inventory1.setSortStrategy(new MergeSort());
                    break;
                case "insertion":
                    Inventory1.setSortStrategy(new InsertionSort());
                    break;
                case "quick":
                    Inventory1.setSortStrategy(new QuickSort());
                    break;
                case "quit":
                    //end runtime
                    loop = false;
                    break;
                case "sort":
                    //perform sorting algorithm
                    Inventory1.sort();
                    break;
                default:
                    System.out.println("Invalid input.");
                    break;
            }
        }
    }
}
