import java.util.Arrays;
import java.util.Scanner;
 
public class FibonacciSequence {

	private static int result;
	private static int seqLength;
	private static int[] Sequence;
	private static Scanner scan;

	public static void main(String[] args) {
		FibonnaciSequence();
	}
	public static void FibonnaciSequence() {
		System.out.println("how long should the sequence be?");
		scan = new Scanner(System.in);
		seqLength = scan.nextInt();
		Sequence = new int[seqLength];
		Sequence[0] = 0;
		Sequence[1] = 1;
		 for (int index = 2; index < seqLength; index++){
			 result = Sequence[index-1]+Sequence[index-2];
		 	Sequence[index] = result;
		 };
		System.out.println(Arrays.toString(Sequence));
	}

}
