class Solution {
    public int getSum(int a, int b) {

        int temp = a & b;
        a = a ^ b;
        b = temp;
        while (b!= 0){
            temp = a & b << 1;
            a = a ^ (b << 1);
            b = temp;
        }

        return a;
    }
}