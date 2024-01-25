import java.util.Scanner;

public class AlarmClock {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int alarm_hour = input.nextInt();
        int alarm_min = input.nextInt();
        int alarm_total = alarm_hour*60 + alarm_min;
        int curr_hour = 0;
        int curr_min = 0;
        int curr_total = curr_hour*60 + curr_min;
        int false_alarms=-1;
        do{
            false_alarms++;
            curr_hour = input.nextInt();
            curr_min = input.nextInt();
            curr_total = curr_hour*60 + curr_min;
        } while (curr_total < alarm_total);
        System.out.println("false alarms: "+false_alarms);
        input.close();
    }
}