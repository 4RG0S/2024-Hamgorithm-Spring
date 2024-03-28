fn next(buf: &String, start_idx: usize) -> usize {
    let croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="].to_vec();
    
    let mut candidates = croatia.clone();
    for i in start_idx..buf.len() {
        let ch = buf.chars().nth(i).unwrap();
        let mut new_candidates = Vec::new();

        for candidate in candidates {
            if candidate.starts_with(ch) {
                new_candidates.push(candidate.get(1..).unwrap());
            }
        }

        candidates = new_candidates;

        if candidates.len() == 0 {
            return start_idx + 1;
        }

        if candidates.len() == 1 {
            if (*candidates.get(0).unwrap()).eq("") {
                return i + 1;
            }
        }
    }

    return start_idx + 1;
}

pub fn main() {
    let stdin = std::io::stdin();
    let mut buf = String::new();

    stdin.read_line(&mut buf).unwrap();
    buf = buf.trim().to_string();

    let mut count = 0;
    let mut i = 0;
    while i < buf.len() {
        i = next(&buf, i);
        count += 1;
    }

    println!("{}", count);
}
