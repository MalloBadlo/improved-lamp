import java.io.*;
import java.net.*;
import java.util.Scanner;

public class Client {

	private String username;
	private Socket s;
	private BufferedReader br;
	private PrintWriter out;
	private static Scanner sc = new Scanner(System.in);

	public Client(String username){

		this.username = username;
		try{
		s = new Socket("localhost",1234);
		br = new BufferedReader(new InputStreamReader(s.getInputStream()));
		out = new PrintWriter(s.getOutputStream(),true);
		}catch(IOException e){}
		sendUser();

	}

	public void listenMessage(){
		new Thread(new Runnable(){
			
			@Override
			public void run(){
				while(s.isConnected()){
					try{
					System.out.println(br.readLine());
				}catch(IOException e){closeEverything(s,bw,out)}
				}
			}

		}).start();
	}

	public void sendMessage(){
		while(s.isConnected()){
			String msg = sc.nextLine();
			out.println(msg);
		}
	}

	public void sendUser(){

			out.println(username);

	}

	public void closeEverything(Socket socket, BufferedReader br, PrintWriter out){
		try{

			if (br != null)
				br.close();

			if (out != null)
				out.close();

			if (socket != null)
				socket.close();



		}catch(IOException e){e.printStackTrace();}
	
	}


	public static void main(String[] args) {

		System.out.print("Set username:@");
		String username = sc.nextLine();
		Client c = new Client(username);
		c.listenMessage();
		c.sendMessage();
	}

}