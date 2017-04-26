/*
 * Main.java
 *
 * Created on 26. Juli 2007, 06:10
 *
 * To change this template, choose Tools | Template Manager
 * and open the template in the editor.
 */

package schemaspygui;

/**
 *
 * @author joachim uhl; mailto:admin@joachim-uhl.de;
 * http://www.joachim-uhl.de/projekte/schemaspygui/
 */
public class Main {
    
    /** Creates a new instance of Main */
    public Main() {
    }
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                SchemaSpyGUIApp gui = new SchemaSpyGUIApp();
                //gui.setLocation(25,25);
                // Center the GUI
                gui.setLocationRelativeTo(null);
                gui.setVisible(true);
            }
        });
    }
}
