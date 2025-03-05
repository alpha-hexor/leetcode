# Title: kth-missing-positive-number
## Question
<p>Given an array <code>arr</code> of positive integers sorted in a <strong>strictly increasing order</strong>, and an integer <code>k</code>.</p><br><br><p>Return <em>the</em> <code>k<sup>th</sup></code> <em><strong>positive</strong> integer that is <strong>missing</strong> from this array.</em></p><br><br><p>&nbsp;</p><br><p><strong class=\"example\">Example 1:</strong></p><br><br><pre><br><strong>Input:</strong> arr = [2,3,4,7,11], k = 5<br><strong>Output:</strong> 9<br><strong>Explanation: </strong>The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5<sup>th</sup>&nbsp;missing positive integer is 9.<br></pre><br><br><p><strong class=\"example\">Example 2:</strong></p><br><br><pre><br><strong>Input:</strong> arr = [1,2,3,4], k = 2<br><strong>Output:</strong> 6<br><strong>Explanation: </strong>The missing positive integers are [5,6,7,...]. The 2<sup>nd</sup> missing positive integer is 6.<br></pre><br><br><p>&nbsp;</p><br><p><strong>Constraints:</strong></p><br><br><ul><br>\t<li><code>1 &lt;= arr.length &lt;= 1000</code></li><br>\t<li><code>1 &lt;= arr[i] &lt;= 1000</code></li><br>\t<li><code>1 &lt;= k &lt;= 1000</code></li><br>\t<li><code>arr[i] &lt; arr[j]</code> for <code>1 &lt;= i &lt; j &lt;= arr.length</code></li><br></ul><br><br><p>&nbsp;</p><br><p><strong>Follow up:</strong></p><br><br><p>Could you solve this problem in less than O(n) complexity?</p><br>

## Notes

For i th position the no. of missing elements are arr[i] - i -1 
Result: After binary search the result will be right + k+1 
Logic:
    if no. of missing elements at mid < k i.e we need more elements we will move
    left to mid +1 


