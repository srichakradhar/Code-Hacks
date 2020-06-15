
class first_positive {
    public int solution(int[] A) {
        // write your code in Java SE 8
        int maxlen = 0;
        for (int i: A) {
            if(i > maxlen) {
                maxlen = i;
            }
        }
        
        if( maxlen == 0 )
        return 1;
        
        int[] unseen = new int[maxlen];
        for (int i = 0; i < maxlen; i++) {
            unseen[i] = i + 1;
        }
        
        for (int i: A) {
            unseen[i - 1] = 0;
        }
        
        for (int i: unseen) {
            if ( i > 0) {
                return i;
            }
        }
        
        return 1;
    }

    public static void main(String args[]){
        int[] a = {1, 2, 3}
        System.out.println(solution(a));
    }
}
