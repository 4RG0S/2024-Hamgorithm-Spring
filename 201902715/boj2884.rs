pub fn main() {
    let mut buf = String::new();
    std::io::stdin().read_line(&mut buf).unwrap();

    let numbers = buf
        .split(" ")
        .map(|s| s.trim().parse::<i8>().unwrap())
        .collect::<Vec<i8>>();
    let mut h = numbers.get(0).unwrap().clone();
    let mut m = numbers.get(1).unwrap().clone();

    m -= 45;
    if m < 0 {
        h -= 1;
        m += 60;
    }
    if h < 0 {
        h += 24;
    }

    println!("{} {}", h, m);
}
