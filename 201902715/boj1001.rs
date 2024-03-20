pub fn main() {
    let mut input = String::new();
    std::io::stdin()
        .read_line(&mut input)
        .expect("error while getting input");

    let numbers = input.split(" ").map(|s| s.trim().parse::<i8>().unwrap()).collect::<Vec<i8>>();
    let a = numbers.get(0).unwrap();
    let b = numbers.get(1).unwrap();

    println!("{}", a - b);
}
