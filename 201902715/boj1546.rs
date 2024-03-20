pub fn main() {
    let stdin = std::io::stdin();

    let mut input = String::new();
    stdin.read_line(&mut input).unwrap();
    let n: f64 = input.trim().parse::<i16>().unwrap().into();

    input.clear();
    stdin.read_line(&mut input).unwrap();

    let scores = input.split(" ").map(|c| c.trim().parse::<f64>().unwrap());

    let max = scores
        .clone()
        .fold(0.0, |max, x| if x > max { x } else { max });

    let sum = scores
        .map(|score| score / max * 100.0)
        .fold(0.0, |acc, x| acc + x);

    let mean = sum / n;
    println!("{}", mean);
}
