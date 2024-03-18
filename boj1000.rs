pub fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("error while getting input");

    let mut sum = 0;
    for string_num in input.split(" ") {
        let num: i8 = string_num.trim().parse().expect("error while parsing number");
        sum += num;
    }

    println!("{}", sum);
}
