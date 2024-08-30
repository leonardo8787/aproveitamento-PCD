/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Interface.java to edit this template
 */
package midlewareWeb;

import java.rmi.Remote;
import java.rmi.RemoteException;

/**
 *
 * @author leonardo
 */
public interface RmiInterfaceWeb extends Remote {
    public boolean GravaMsgWeb(String msg) throws RemoteException;

    /**
     *
     * @return
     */
    public String RecuperaMsgsWeb() throws RemoteException;
    
}
