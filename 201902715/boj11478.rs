use std::collections::HashSet;

pub fn main() {
    let stdin = std::io::stdin();
    let mut buf = String::new();

    stdin.read_line(&mut buf).unwrap();
    buf = buf.trim().to_string();

    let mut result: HashSet<String> = HashSet::new();
    
    for size_of_str in 1..=(buf.len()) {
        for start_idx in 0..=(buf.len() - size_of_str) {
            let sub_str = buf.get(start_idx..(start_idx + size_of_str)).unwrap();
            result.insert(sub_str.to_string());
        }
    }

    println!("{}", result.len());
}
