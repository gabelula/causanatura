package schemaspygui;

import java.io.*;
import java.io.InputStreamReader;

//Catches every error output from SchemaSpy
/**
 *
 * @author joachim uhl; mailto:admin@joachim-uhl.de; http://www.joachim-uhl.de/projekte/schemaspygui/
 */
public class RunSchemaSpy implements Runnable {

    private SchemaSpyGUIApp gui;
    private String command;
    private String displ_command;

    public RunSchemaSpy(SchemaSpyGUIApp gui, String run_command, String display_command) {
        this.gui = gui;
        this.command = run_command;
        this.displ_command = display_command;
    }

    public void run( ) {

        try {
             gui.setOutputText("This is the command (password not displayed!) SchemaSpyGUI has generated:" +"\n");
             gui.setOutputText(displ_command +"\n");
             gui.setOutputText("\n");
             Process d = Runtime.getRuntime().exec(command);

             ErrStreamOut errOut = new ErrStreamOut(d, gui);
             InputStreamOut inOut = new InputStreamOut(d, gui);

             Thread terrOut = new Thread(errOut);
             Thread tinOut = new Thread(inOut);

             terrOut.setName("terrOut");
             terrOut.start();
             tinOut.setName("tinOut");
             tinOut.start();

        } catch ( Exception ioe ) {
                System.err.println( "IO error: " + ioe );
                ioe.printStackTrace();
        }
    }

}
class ErrStreamOut implements Runnable {

    private Process p;
    private SchemaSpyGUIApp gui;

    public ErrStreamOut(Process d, SchemaSpyGUIApp gui) {
        this.p = d;
        this.gui = gui;
    }

    public void run() {
        try {
            BufferedReader in = new BufferedReader(new InputStreamReader(p.getErrorStream()));
            String s;
            while ((s = in.readLine()) != null) {
                gui.setOutputText(s +"\n");
            }
            int exitVal = p.waitFor();
            gui.setOutputText("E=" + exitVal);
            in.close();
        } catch (Exception e) {
           e.printStackTrace();
        }
    }
}

//Catches every "normal" output from SchemaSpy
class InputStreamOut implements Runnable {
    
    private Process p;
    private SchemaSpyGUIApp gui;
    
    public InputStreamOut(Process d, SchemaSpyGUIApp gui) {
        this.p = d;
        this.gui = gui;
    }
    
    public void run() {
        try {
            BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
            //String s;
            int c;
            /*while ((s = in.readLine()) != null)
                {GuiSchema.setText(s +"\n");}
            int exitVal = p.waitFor();
            GuiSchema.setText("" +exitVal);
            */
            while ((c = in.read()) != -1) {
                /*String aChar = new Character((char)c).toString();
                GuiSchema.setText(aChar);*/
                gui.setOutputText(String.valueOf(Character.toChars(c)));
            }
            int exitVal = p.waitFor();
            gui.setOutputText("I=" + exitVal);
            in.close();
            // Launch the result when finish if checked and No Errors
            if (exitVal == 0 && gui.getAutoLaunchInfo()) {gui.startShowOutput();}
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
