use std::io;

fn main() {
    let mut input = String::new();
    let mut matrix: Vec<Vec<i32>> = Vec::new();
    
    io::stdin().read_line(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    
    for _ in 0..n {
        input.clear();
        io::stdin().read_line(&mut input).unwrap();
        let row: Vec<i32> = input.trim().split_whitespace()
                                 .map(|x| x.parse().unwrap())
                                 .collect();
        matrix.push(row);
    }

    let max_value = simulate(&mut matrix, 0);
    println!("{}", max_value);
}

fn simulate(matrix: &mut Vec<Vec<i32>>, depth: usize) -> i32 {
    if depth == 5 {
        return max_matrix(matrix.to_vec());
    }
    
    let mut max_val = 0;
    let dirs = vec![(0, 1), (0, -1), (1, 0), (-1, 0)]; // right, left, down, up
    
    for dir in dirs {
        let mut temp_matrix = matrix.clone();
        move_matrix(&mut temp_matrix, dir);
        max_val = i32::max(max_val, simulate(&mut temp_matrix, depth + 1));
    }
    
    max_val
}

fn max_matrix(matrix: Vec<Vec<i32>>) -> i32 {
    let mut max_value = 0;
    for i in 0..matrix.len() {
        for j in 0..matrix.len() {
            max_value = i32::max(max_value, matrix[i][j]);
        }
    }
    max_value
}

fn move_matrix(matrix: &mut Vec<Vec<i32>>, direction: (i32, i32)) {
    let n = matrix.len();
    match direction {
        (0, 1) => {
            for row in matrix.iter_mut() {
                row.reverse();
                compress_and_merge(row);
                row.reverse();
            }
        }
        (0, -1) => {
            for row in matrix.iter_mut() {
                compress_and_merge(row);
            }
        }
        (1,0) => {
            for j in 0..n {
                let mut col: Vec<i32> = (0..n).map(|i| matrix[i][j]).collect();
                col.reverse();
                compress_and_merge(&mut col);
                col.reverse();
                for i in 0..n {
                    matrix[i][j] = col[i];
                }
            }
        }
        (-1,0) => {
            for j in 0..n {
                let mut col: Vec<i32> = (0..n).map(|i| matrix[i][j]).collect();
                compress_and_merge(&mut col);
                for i in 0..n {
                    matrix[i][j] = col[i];
                }
            }
        }
        _ => panic!()
    }
}

fn compress_and_merge(row: &mut Vec<i32>) {
    let mut stack: Vec<i32> = Vec::new();
    let mut isMerged = false;
    for &val in row.iter() {
        if val != 0 {
            if let Some(last) = stack.last_mut() {
                if *last == val && !isMerged {
                    *last *= 2;
                    isMerged = true;
                    continue;
                }
            }
            stack.push(val);
            isMerged = false;
        }
    }
    row.fill(0);
    for (i, &val) in stack.iter().enumerate() {
        row[i] = val;
    }
}
