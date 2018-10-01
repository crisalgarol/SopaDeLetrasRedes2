import java.io.*;
import java.net.*;

//Cliente con sockets bloqueantes

public class C_eco{
    
    private static Socket cl;

    public static void main(String[] args) {
        
        String host = "127.0.0.1";
        int pto = 7881;

        while(true){
            try{
                    cl = new Socket(host, pto);
                    System.out.print("Escribe un comando: ");

                    BufferedReader br1 = new BufferedReader(new InputStreamReader(System.in));
                    PrintWriter pw = new PrintWriter(new OutputStreamWriter(cl.getOutputStream())); //Se le agrega el printwriter para formatear el getOutPutStream
                    BufferedReader br2 = new BufferedReader(new InputStreamReader(cl.getInputStream()));

                        String msj = br1.readLine();
                        pw.println(msj);
                        pw.flush(); //Hacer que se envie en ese momento 

                        if(msj.compareToIgnoreCase("salir") == 0){
                            System.out.println("Termina la aplicacion");
                            //System.exit(0);
                        }else{
                            String eco = br2.readLine();
                            System.out.println("Eco recibido: " + eco + "\n");
                        }

                        br2.close();
                        pw.close();
                        cl.close();                    

                }catch(Exception e){
                    e.printStackTrace();
                }
        }
        
    }   


}
