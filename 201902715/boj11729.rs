use std::io::Write;
use std::io::BufWriter;

fn hanoi_move(n: i32, from: i32, to: i32, other: i32) -> Vec<(i32, i32)> {
    if n == 1 {
        return vec![(from, to)];
    }

    let move_1 = hanoi_move(n - 1, from, other, to);
    let move_2 = vec![(from, to)];
    let move_3 = hanoi_move(n - 1, other, to, from);

    [move_1, move_2, move_3].concat()
}

pub fn main() {
    let mut buf = String::new();
    std::io::stdin().read_line(&mut buf).unwrap();

    let k: i32 = buf.trim().parse().unwrap();
    let result_vec = hanoi_move(k, 1, 3, 2);

    let mut out = BufWriter::new(std::io::stdout().lock());
    writeln!(out, "{}", result_vec.len()).unwrap();
    for (from, to) in result_vec {
        writeln!(out, "{} {}", from, to).unwrap();
    }
}
