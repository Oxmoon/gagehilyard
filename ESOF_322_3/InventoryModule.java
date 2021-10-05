package com.mycompany.assignment3;

/**
 *
 * @author ghily
 */
public class InventoryModule {
    SortMethod sortMethod;
    
    public InventoryModule(){
    }
    
    public void sort(){
        if (this.sortMethod != null){
            sortMethod.sort();
        }
        else{
            System.out.println("No Sort Method.");
        }
    }
    
    public void setSortStrategy(SortMethod sm) {
        sortMethod = sm;
    }
}
