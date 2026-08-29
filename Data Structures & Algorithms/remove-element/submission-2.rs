impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut k = 0;
        for i in 0..nums.len() {
            if nums[i] != val {
                nums.swap(i, k);
                k += 1;
            }
        }
        k as i32
    }
}
