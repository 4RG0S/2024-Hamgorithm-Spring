use std::{collections::HashMap, io::Write};

pub fn main() {
    let stdin = std::io::stdin();
    let stdout = std::io::stdout();
    let mut out = std::io::BufWriter::new(stdout.lock());

    let mut s = String::new();
    stdin.read_line(&mut s).unwrap();

    let alphabet = "abcdefghijklmnopqrstuvwxyz".chars().collect::<Vec<char>>();
    let mut position_map: HashMap<char, i32> = HashMap::new();

    for (i, c) in s.chars().enumerate() {
        if position_map.contains_key(&c) {
            continue;
        } else {
            position_map.insert(c, i as i32);
        }
    }

    for (i, c) in alphabet.iter().enumerate() {
        if position_map.contains_key(&c) {
            write!(out, "{}", position_map.get(&c).unwrap()).unwrap();
        } else {
            write!(out, "-1").unwrap();
        }
        
        if i < alphabet.len() - 1 {
            write!(out, " ").unwrap();
        }
    }
}
