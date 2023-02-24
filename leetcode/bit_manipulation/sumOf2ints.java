package leetcode.bit_manipulation;

public class sumOf2ints {

    public static void main(String args[]) {
        sumOf2ints s = new sumOf2ints();
        int x = s.getSum(2, 3);
        System.out.println(x);

    }

    public int getSum(int a, int b) {
        while (b != 0)// will continue till there is no carry
        {
            int temp = a ^ b;// this is the sum ignoring the carry
            b = (a & b) << 1;// this is the carry, we shit it by 1 since we want to add as carry to the next
            // bit
            a = temp;
        }
        return a;
    }
}
