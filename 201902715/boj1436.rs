pub fn main() {
    let mut buf = String::new();
    let stdin = std::io::stdin();
    stdin.read_line(&mut buf).unwrap();
    let n = buf.trim().parse::<i32>().unwrap();

    let mut count = 0;

    for num in 0..66610000 {
        if num.to_string().contains("666") {
            count += 1;
            if n == count {
                println!("{}", num);
                break;
            }
        }
    }
}
