/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package midlewareDesktop;

/**
 *
 * @author leonardo
 */
public class Emoji {

    public Emoji() {}

    public static String transformToEmoji(String text) {
        if (text != null) {
            text = text.replace(":-)", "&#128522;"); 
            text = text.replace(":-(", "&#128542;");  
            text = text.replace(":-/", "&#128533;");  
            text = text.replace("S2", "&#65039;"); 
            text = text.replace("sefuder", "&#128076;");  
            text = text.replace("bomd+", "&#128588;"); 
        }
        else {
            return "";
        }
        return text;
    }
}