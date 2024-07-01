use std::io::{self, Read};
use std::collections::VecDeque;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    
    let mut lines = input.lines();
    let first_line = lines.next().unwrap();
    let mut dimensions = first_line.split_whitespace();
    let n: usize = dimensions.next().unwrap().parse().unwrap();
    let m: usize = dimensions.next().unwrap().parse().unwrap();

    let mut map: Vec<Vec<char>> = Vec::new();

    for line in lines {
        let chars: Vec<char> = line.chars().collect();
        map.push(chars);
    }

    println!("{}", find_max_distance(n, m, &map));
}

fn find_max_distance(n: usize, m: usize, map: &[Vec<char>]) -> i32 {
    let mut max_distance = 0;

    for i in 0..n {
        for j in 0..m {
            if map[i][j] == 'L' {
                max_distance = max_distance.max(bfs(n, m, i, j, &map));
            }
        }
    }
    max_distance
}

fn bfs(n: usize, m: usize, x: usize, y: usize, map: &[Vec<char>]) -> i32 {
    let mut queue = VecDeque::new();
    let mut visited = vec![vec![false; m]; n];
    let directions = [(-1, 0), (1, 0), (0, -1), (0, 1)];
    queue.push_back((x, y, 0));
    visited[x][y] = true;
    
    let mut local_max = 0;
    
    while let Some((x, y, dist)) = queue.pop_front() {
        for &(dx, dy) in directions.iter() {
            let nx = x as i32 + dx;
            let ny = y as i32 + dy;
            if nx >= 0 && ny >= 0 && nx < n as i32 && ny < m as i32 {
                let nx = nx as usize;
                let ny = ny as usize;
                if !visited[nx][ny] && map[nx][ny] == 'L' {
                    visited[nx][ny] = true;
                    queue.push_back((nx, ny, dist + 1));
                    local_max = local_max.max(dist + 1);
                }
            }
        }
    }
    local_max
}
