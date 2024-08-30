/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package midlewareDesktop;

import java.io.IOException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import javax.swing.JOptionPane;

/**
 *
 * @author leonardo
 */
public class ChatServerDesktop {
    private Registry reg;
    public ChatServerDesktop(){
   
    }
    
    public void startServerDesktop(){
        try{
            this.reg = LocateRegistry.createRegistry(7777);
            RmiInterfaceDesktop objRmi = new RmiImplDesktop();
            reg.rebind("ServidorChatDesktop", objRmi);
        }catch(IOException e){
            JOptionPane.showMessageDialog(null, "erro no server: " + e.getMessage());
        }
    }

}