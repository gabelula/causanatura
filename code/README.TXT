SchemaSpyGUI by Joachim Uhl, admin@joachim-uhl.de
Version 0.99 (20090221)

http://www.joachim-uhl.de/projekte/schemaspygui/
http://schemaspygui.sourceforge.net/

Released unter GNU Lesser General Public License
http://www.gnu.org/licenses/lgpl.html
The Icons are from FamFamFam (Silk Icons) 
http://www.famfamfam.com/lab/icons/silk/ and 
licensed under a Creative Commons Attribution 2.5 License

Needed additional tools/applications

    * SchemaSpy http://schemaspy.sourceforge.net/ (<– please download and unpack it first. Also have a look at the SchemaSpy Homepage)
    * dot executable from Graphviz http://www.graphviz.org/ (make shure that the dot executable is in your PATH)
    * Java Runtime Environment 5 or 6 (JRE 1.5 or JRE 1.6)

Installation

Just unpack the downloaded .zip file. Copy either the schemaspy.jar into your SchemaSpyGUI folder or copy the SchemaSpyGUI files and folders into your SchemaSpy folder. 
If you are a windows user, click on schemaSpyGUI.bat. If you are working with Linux, try ./schemaSpyGUI.sh (don't forget to make it executable).

If SchemaSpyGUI will not start, then try 
java -jar schemaSpyGUI.jar
at the command line (within the folder where the schemaSpyGUI.jar resides).

Description

SchemaSpyGUI is a graphical user interface for the very useful tool SchemaSpy from John Currier. With SchemaSpy you can analyze the schema metadata of a database and generate a browser readable graphical representation of it.
SchemaSpy is a java-based command line tool. SchemaSpyGUI is also java-based and sits on top of it and provides a graphical interface for those of us which appreciate the comfort of windows and mouse based applications (like me ;-)). SchemaSpyGUI is distributed under the terms of the Lesser GNU Public License. Maybe the tool is useful for some of you. Feedback on problems and/or enhancements is appreciated and needed :-).

Features

    * Control SchemaSpy completely with a graphical user interface (GUI)
    * all parameters of SchemaSpy are supported (as far as i know, except the single sign on -sso and the no ads -noads flag)
    * you can save/load your parameter settings
    * you can start the schema output/HTML file with a single mouse click or let it start automatically after gathering the schema details
    * choose your path informations in a convenient way with a standard file chooser
    * While SchemaSpy is gathering information the output is displayed within the GUI. No need for shell/command line affairs
    * No display of your private password
    * works with Windows and Linux (feedback from Mac users is welcome!)



