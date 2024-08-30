/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
/**
 *
 * @author leonardo
 */
package midlewareWeb;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.logging.Level;
import java.util.logging.Logger;

public class RmiImplWeb extends UnicastRemoteObject implements RmiInterfaceWeb {

    public RmiImplWeb() throws RemoteException {
        super();
    }

    @Override
    public boolean GravaMsgWeb(String msg) throws RemoteException {
        FileWriter writer;
        try {
            writer = new FileWriter("/home/leonardo/NetBeansProjects/ClientDesktopMiddleware/src/main/java/repositorioMsgs/chatweb.txt", true);
            writer.write(msg);
            writer.close();

        } catch (IOException ex) {
            Logger.getLogger(RmiImplWeb.class.getName()).log(Level.SEVERE, null, ex);
            return false;
        }
        return true;
    }

    @Override
    public String RecuperaMsgsWeb() throws RemoteException {
        FileReader reader;
        String msg = "";
        try {
            reader = new FileReader("/home/leonardo/NetBeansProjects/ClientDesktopMiddleware/src/main/java/repositorioMsgs/chatweb.txt");
            BufferedReader bufferReader = new BufferedReader(reader);

            while (bufferReader.ready()) {
                msg = bufferReader.readLine();
            }
            reader.close();
        } catch (FileNotFoundException ex) {
            Logger.getLogger(RmiImplWeb.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(RmiImplWeb.class.getName()).log(Level.SEVERE, null, ex);
        }
        return msg;
    }
}
