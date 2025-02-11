public class Main {
    public static int coinSums(int target, int[] coins) {
        int[] dp = new int[target + 1];
        dp[0] = 1; // 0원을 만드는 방법은 1가지

        for (int coin : coins) {
            for (int i = coin; i <= target; i++) {
                dp[i] += dp[i - coin];
            }
        }

        return dp[target];
    }

    public static void main(String[] args) {
        int target = 200;
        int[] coins = {1, 2, 5, 10, 20, 50, 100, 200};

        System.out.println(coinSums(target, coins));
    }
}
