use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
    let mut groups = HashMap::new();
    for s in strs {
        let mut chars: Vec<char> = s.chars().collect();
        chars.sort_unstable();
        let key = chars.into_iter().collect::<String>();

        if !groups.contains_key(&key) {
            groups.insert(key.clone(), Vec::new());
        }

        groups.get_mut(&key).unwrap().push(s);
    }

    groups.into_values().collect()
    } 
}
