
public class main {

	public static String encrypt(String text, String key) {
		String solution = "";
		text = text.toUpperCase();
		
		for(int i = 0, j = 0; i < text.length(); i++) {
			char c = text.charAt(i);
			if(c < 'A' || c > 'Z') {
				continue;
			}
			solution += (char) ((c + key.charAt(j) - 2 * 'A') % 26 + 'A');
			j = ++j % key.length();
		}
		return solution;
	}
	
	public static String decrypt(String text, String key) {
		String solution = "";
		text = text.toUpperCase();
		for(int i = 0, j = 0; i < text.length(); i++) {
			char c = text.charAt(i);
			if(c < 'A' || c > 'Z') {
				continue;
			}
			solution += (char) ((c - key.charAt(j) + 26) % 26 + 'A');
			j = ++j % key.length();
		}
		return solution.toLowerCase();
	}
	
	public static void main(String[] args) {
		String key = "VIGENERECIPHER"; 
		
		String message = "Hello this is a test";
		String message2 = "gabrielPaulCorella";
		String message3 = "universityOfDelaware";
		String message4 = "youDee";
		String message5 = "password";
		
		String encryptedMes = encrypt(message,key);
		String encryptedMes2 = encrypt(message2,key);
		String encryptedMes3 = encrypt(message3,key);
		String encryptedMes4 = encrypt(message4,key);
		String encryptedMes5 = encrypt(message5,key);
		
		System.out.println("**************** Tests ****************");
		
		System.out.println("String Message 1: " + message);
		System.out.println("Encrypted Message: " + encryptedMes);
		System.out.println("Decrypted Message: "+ decrypt(encryptedMes,key)+ "\n");
		
		System.out.println("String Message 2: " + message2);
		System.out.println("Encrypted Message: " + encryptedMes2);
		System.out.println("Decrypted Message: "+ decrypt(encryptedMes2,key)+ "\n");
		
		System.out.println("String Message 3: " + message3);
		System.out.println("Encrypted Message: " + encryptedMes3);
		System.out.println("Decrypted Message: "+ decrypt(encryptedMes3,key)+ "\n");
		
		System.out.println("String Message 4: " + message4);
		System.out.println("Encrypted Message: " + encryptedMes4);
		System.out.println("Decrypted Message: "+ decrypt(encryptedMes4,key)+ "\n");
		
		System.out.println("String Message 5: " + message5);
		System.out.println("Encrypted Message: " + encryptedMes5);
		System.out.println("Decrypted Message: "+ decrypt(encryptedMes5,key) + "\n");
		
		
	}
	
}
