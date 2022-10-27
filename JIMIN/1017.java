class Solution {
    public int solution(int num1, int num2) {
        int answer = -1;
        answer = num1 % num2;
        System.out.println(answer);
        return answer;
    }

    public static void main(String args[]){
       Solution sol = new Solution();
       sol.solution(3, 2);
    }
}
