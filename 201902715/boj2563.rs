pub fn main() {
    let mut buf = String::new();
    let stdin = std::io::stdin();

    stdin.read_line(&mut buf).unwrap();
    let n = buf.trim().parse::<i16>().unwrap();
    buf.clear();

    let mut papers = [0; 10000];

    for _ in 0..n {
        stdin.read_line(&mut buf).unwrap();
        let mut iter = buf.split_whitespace();
        let start_x = iter.next().unwrap().parse::<usize>().unwrap();
        let start_y = iter.next().unwrap().parse::<usize>().unwrap();
        buf.clear();

        for x in start_x..(start_x + 10) {
            for y in start_y..(start_y + 10) {
                let pos: usize = x * 100 + y;
                papers[pos] = 1;
            }
        }
    }

    let sum = papers.iter().fold(0, |acc, x| acc + x);
    println!("{}", sum);
}
