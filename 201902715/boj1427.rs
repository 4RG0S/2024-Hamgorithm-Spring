pub fn main() {
    let mut buf = String::new();
    let stdin = std::io::stdin();
    stdin.read_line(&mut buf).unwrap();
    let mut numbers: Vec<u32> = buf.trim().chars().map(|c| c.to_digit(10).unwrap()).collect();
    numbers.sort_by(|a, b| b.cmp(a));
    let result = numbers.iter().map(|n| n.to_string()).collect::<Vec<String>>().join("");
    println!("{}", result);
}
