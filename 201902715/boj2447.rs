use std::io::BufWriter;
use std::io::Write;

fn make_star(start: (usize, usize), end: (usize, usize), star_arr: &mut [[bool; 2187]; 2187]) {
    // println!("{} {} -> {} {}", start.0, start.1, end.0, end.1);

    let length_of_1_3: usize = (end.0 - start.0 + 1) / 3;
    if length_of_1_3 <= 0 {
        return;
    }

    for i in start.0 + length_of_1_3..start.0 + length_of_1_3 * 2 {
        for j in start.1 + length_of_1_3..start.1 + length_of_1_3 * 2 {
            star_arr[i][j] = false;
        }
    }

    for i in 0..3 {
        for j in 0..3 {
            make_star(
                (start.0 + length_of_1_3 * i, start.1 + length_of_1_3 * j),
                (
                    start.0 + length_of_1_3 * (i + 1) - 1,
                    start.1 + length_of_1_3 * (j + 1) - 1,
                ),
                star_arr,
            )
        }
    }
}

pub fn main() {
    let mut buf = String::new();
    std::io::stdin().read_line(&mut buf).unwrap();
    let n: i32 = buf.trim().parse().unwrap();

    let mut star_arr = [[true; i32::pow(3, 7) as usize]; i32::pow(3, 7) as usize];
    make_star((0, 0), ((n - 1) as usize, (n - 1) as usize), &mut star_arr);

    let mut out = BufWriter::new(std::io::stdout().lock());

    for i in 0..n {
        for j in 0..n {
            if star_arr[i as usize][j as usize] {
                write!(out, "*").unwrap();
            } else {
                write!(out, " ").unwrap();
            }
        }
        writeln!(out, "").unwrap();
    }
}
