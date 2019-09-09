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
		while (i < pattern.length() - 1) { // 这里不需要计算本身的最长匹配前后缀
			if (pattern.charAt(i) == pattern.charAt(len)) {
				// 新字符与上次前缀的后一个字符匹配，公共前缀的长度加一
				len++;
				prefixTable[i + 1] = len; // 这里为了不需要移位，将前缀表中的i+1的元素对应原始pattern的第i+1个子串（i从0开始）
				i++;
			} else {
				if (len > 0) { // 不匹配且前面一个子串具有公共前后缀存在
					len = prefixTable[len]; // 这里比较关键，将最长公共前缀的位置移到prefixTable[len]
				} else {
					// 不匹配，且前面的子串没有公共前后缀，那么prefixTable[i+1]必然为0
					prefixTable[i + 1] = 0;
					i++;
				}
			}

		}
		return prefixTable;
	}
}