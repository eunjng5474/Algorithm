class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
		int[] left = {3, 0};
		int[] right = {3, 2};    
        
        for (int i=0; i<numbers.length; i++) {
            if(numbers[i] == 1 || numbers[i] == 4 | numbers[i] == 7) {
                answer += "L";
                left[0] = numbers[i]/3;
                left[1] = 0;
            }
            else if(numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9) {
                answer += "R";
                right[0] = numbers[i]/3 - 1;
                right[1] = 2;
            }
            else {
            	if(numbers[i] == 0) {
            		numbers[i] = 10;
            	}
            	int leftDist = Math.abs(numbers[i]/3 - left[0]) + Math.abs(left[1] - 1);
            	int rightDist = Math.abs(numbers[i]/3 - right[0]) + Math.abs(right[1] - 1);
            	if(leftDist < rightDist) {
            		answer += "L";
            		left[0] = numbers[i]/3;
            		left[1] = 1;
            	} else if (leftDist > rightDist) {
            		answer += "R";
            		right[0] = numbers[i]/3;
            		right[1] = 1;
            	} else {
            		if(hand.equals("left")) {
            			answer += "L";
                		left[0] = numbers[i]/3;
                		left[1] = 1;
            		} else {
            			answer += "R";
            			right[0] = numbers[i]/3;
                		right[1] = 1;
            		}
            	}
            }
        }

        return answer;
    }
}