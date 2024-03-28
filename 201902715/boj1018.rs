use std::cmp::min;

fn count_diff(chess_board: &Vec<Vec<char>>, start_of_row: i32, start_of_col: i32) -> i32 {
    let mut diff = 0;
    for row in start_of_row..start_of_row+8 {
        let mut current_color = if row % 2 == 0 { 'W' } else { 'B' };
        for col in start_of_col..start_of_col+8 {
            let color = chess_board[row as usize][col as usize];
            if !current_color.eq(&color) {
                diff += 1;
            }
            current_color = if current_color.eq(&'W') { 'B' } else { 'W' };
        }
    }

    min::<i32>(diff, 64-diff)
}

pub fn main() {
    let mut buf = String::new();
    let stdin = std::io::stdin();
    stdin.read_line(&mut buf).unwrap();

    let wh = buf.trim().split_whitespace().map(|x| x.parse::<i32>().unwrap()).collect::<Vec<i32>>();
    let h = wh[0];
    let w = wh[1];

    let mut chess_board: Vec<Vec<char>> = Vec::new();

    for _ in 0..h {
        buf.clear();
        stdin.read_line(&mut buf).unwrap();
        let line = buf.trim();
        let line: Vec<char> = line.chars().collect();
        chess_board.push(line);
    }

    let mut minimum_diff = 64;

    for start_of_row in 0..h-7 {
        for start_of_col in 0..w-7 {
            let diff = count_diff(&chess_board, start_of_row, start_of_col);
            if diff < minimum_diff {
                minimum_diff = diff;
            }
        }
    }

    println!("{}", minimum_diff);
}
