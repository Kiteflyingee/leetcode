import java.util.ArrayList;

/**
 * kmp算法实现
 * 
 * @author devkite
 *
 */

public class Kmp {
	public static void main(String[] args) {
		Kmp kmp = new Kmp();
		long start = System.currentTimeMillis();
		String mainString = "ABABABCABAABDSDS";
		String pattern = "ABABCABAA";
		int[] prefixTable = kmp.preSufTable(pattern);

		// 输出prefix table
		for (int i = 0; i < prefixTable.length; i++) {
			System.out.print(prefixTable[i] + "\t");
		}
		System.out.println();
		kmp.kmpSearch(mainString, pattern, prefixTable);
		System.out.println("耗时:" + (System.currentTimeMillis() - start) + "ms");
	}

	public void kmpSearch(String mainString, String pattern, int[] prefixTable) {
		/**
		 * KMP匹配
		 */
		int j = 0;
		for (int i = 0; i < mainString.length();) {
			if (j == pattern.length() - 1 && pattern.charAt(j) == mainString.charAt(i)) {
				System.out.println("Found,位置:" + (i - j));
				j = prefixTable[j];
			}
			if (mainString.charAt(i) == pattern.charAt(j)) {
				i++;
				j++;
			} else {
				j = prefixTable[j];
				if (j == -1) {
					i++;
					j++;
				}
			}
		}

	}

	public int[] preSufTable(String pattern) {
		/**
		 * 求出模式串中的各个子串的最长公共前后缀的长度，不包括自己本身从-1开始
		 */
		int[] prefixTable = new int[pattern.length()];
		int len = 0; // 记录当前子串的最长公共前后缀的长度
		int i = 1;
		prefixTable[0] = -1;
		while (i < pattern.length() - 1) {
			if (pattern.charAt(i) == pattern.charAt(len)) {
				// 如果当前字符匹配成功，则最长公共前缀加一，并计算模式串的下一个子串
				len++;
				prefixTable[i + 1] = len;
				i++;
			} else {
				// 如果当前字符匹配失败，如果len存在大于0 的话，将len跳转到最长公共前缀的起点
				if (len > 0) {
					len = prefixTable[len];
				} else {
					prefixTable[i + 1] = len;
					i++;
				}
			}

		}
		return prefixTable;
	}
}