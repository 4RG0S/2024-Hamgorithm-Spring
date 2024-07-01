pub fn main() {
    let mut buf = String::new();
    let stdin = std::io::stdin();
    stdin.read_line(&mut buf).unwrap();

    let n: i32 = buf.trim().parse().unwrap();
    let mut five_kilo = n / 5;

    while five_kilo >= 0 {
        let remain = n - (five_kilo * 5);
        if remain % 3 == 0 {
            println!("{}", five_kilo + (remain / 3));
            return;
        }
        five_kilo -= 1;
    }

    println!("-1");
}
