pub fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    let numbers = input.split(" ").map(|s| s.trim().parse().unwrap()).collect::<Vec<i32>>();
    let a = numbers.get(0).unwrap();
    let b = numbers.get(1).unwrap();

    if a < b {
        println!("<");
    } else if a > b {
        println!(">");
    } else {
        println!("==");
    }
}
