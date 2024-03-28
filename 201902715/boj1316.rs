use std::collections::HashSet;

fn is_group_word(word: &str) -> bool {
    let mut previous_word: Option<char> = None;
    let mut visited_word_set: HashSet<char> = HashSet::new();

    for ch in word.chars() {
        if visited_word_set.contains(&ch) {
            return false;
        }

        if previous_word.is_none() {
        } else if previous_word.unwrap().eq(&ch) {
            continue;
        } else {
            visited_word_set.insert(previous_word.unwrap());
        }
        previous_word = Some(ch);
    }

    return true;
}

pub fn main() {
    let stdin = std::io::stdin();

    let mut buf = String::new();
    stdin.read_line(&mut buf).unwrap();
    let n = buf.trim().parse::<i16>().unwrap();
    let mut count = 0;

    for _ in 0..n {
        buf.clear();
        stdin.read_line(&mut buf).unwrap();
        if is_group_word(&buf) {
            count += 1;
        }
    }

    println!("{}", count);
}
