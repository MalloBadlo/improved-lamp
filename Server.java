import java.io.*;
import java.net.*;

public class Server {

	private ServerSocket ss;


	public Server(ServerSocket ss){
		this.ss = ss;
	}

	public void startServer(){
		System.out.println("Server is now online");

		try{

			while(!ss.isClosed()){
				Socket socket = ss.accept();
				System.out.println("New client has connected");
				ClientHandler clienthandler = new ClientHandler(socket);

				Thread thread = new Thread(clienthandler);
				thread.start();
	
			}



		}catch(Exception e){
			System.out.println(e);
		}
	}


	public static void main(String[] args) throws IOException{
		ServerSocket ss = new ServerSocket(1234);
		Server server = new Server(ss);
		server.startServer();

	}
}