/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package midlewareWeb;

import java.io.IOException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import javax.swing.JOptionPane;

/**
 *
 * @author leonardo
 */
public class ChatServerWeb {
    private Registry reg;
    public ChatServerWeb(){
   
    }
    
    public void startServerWeb(){
        try{
            this.reg = LocateRegistry.createRegistry(8888);
            RmiInterfaceWeb objRmi = new RmiImplWeb();
            reg.rebind("ServidorChatWeb", objRmi);
        }catch(IOException e){
            JOptionPane.showMessageDialog(null, "erro no server: " + e.getMessage());
        }
    }

}
