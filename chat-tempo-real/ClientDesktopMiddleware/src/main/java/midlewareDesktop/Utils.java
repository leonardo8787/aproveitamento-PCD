/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

package midlewareDesktop;

/**
 *
 * @author leonardo
 */
public class Utils {
    
    public static String nick;
    public static String color;
    
    public static void setColor(String  new_color) {
        color = new_color;
    }
    
    public static String getColor() {
        return color;
    }

    public static void setNick(String new_nick) {
        nick = new_nick;
    }

    public static String getNick() {
        return nick;
    }

}