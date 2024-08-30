/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Interface.java to edit this template
 */
package midlewareDesktop;

import java.rmi.Remote;
import java.rmi.RemoteException;

/**
 *
 * @author leonardo
 */
public interface RmiInterfaceDesktop extends Remote {
    public boolean GravaMsgDesktop(String msg) throws RemoteException;

    /**
     *
     * @return
     */
    public String RecuperaMsgsDesktop() throws RemoteException;
    
}
