import java.net.*;
import java.io.*;
import java.util.concurrent.*;

public class ClientHandler implements Runnable {

	 Socket socket;
	 BufferedReader br;
	 PrintWriter out;
	 public static ArrayBlockingQueue<ClientHandler> clientList = new ArrayBlockingQueue<>(10);
	 String username;
	 boolean avaible;
	 ClientHandler guest;

	public ClientHandler(Socket socket){
	try{
		guest = null;
		this.socket = socket;
		br = new BufferedReader(new InputStreamReader(socket.getInputStream()));
		out = new PrintWriter(socket.getOutputStream(), true);
		username = br.readLine();
		clientList.add(this);
		avaible = true;
		out.println("Hello " + username + ", welcome !");
		this.init();


	}catch(IOException e ){}
}
	
	
	public void init(){
		out.println("Connecting with a client...");
			 guest = findSomeone();
			if (guest != null){
				out.println("You're connected with: " + guest.username );
				Thread.currentThread().start();
			}
								
	}



	@Override
	public void run(){
		
		
		
			
			//new Thread(new Runnable(){

				//@Override
				//public void run(){
				while(guest.socket.isConnected()){
					try{
						String msg = br.readLine();
						talk(msg,guest);

					}catch(Exception e){
						closeEverything(socket,br,out);
						break;	
						
					}
			}
		//		}
		//	}).start(); 

		
		
		
		


	}

	private void talk(String msg, ClientHandler guest){
			guest.out.println(username + ": " + msg);
			

	}

	

	private ClientHandler findSomeone(){
	
		do{

		for (ClientHandler ch : clientList)
			if (ch.avaible && !(ch.username.equals(this.username))){
				guest = ch;
				guest.avaible = false;
				break;
			}

		}while(guest == null);
		return guest;
	}

	

	private void closeEverything(Socket socket, BufferedReader br, PrintWriter out){
		removeClient();
		try{
		if (socket != null)
			socket.close();

		if (br != null)
			br.close();

		if (out != null)
			out.close();
	}catch (IOException e){System.out.println(e);}

	}

	private void removeClient(){
		clientList.remove(this);
		guest.out.println("SERVER: " + username + " has left the chat");
		guest.avaible = true;
		
	}
}