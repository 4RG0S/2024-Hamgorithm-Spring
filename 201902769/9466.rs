use std::io::{self, BufRead};

fn find_cycles(parent: &Vec<usize>) -> usize {
    let n = parent.len();
    let mut visited = vec![false; n];
    let mut finished = vec![false; n];
    let mut count = 0;

    for i in 0..n {
        let mut now = i;
        let mut stack = vec![];

        while !visited[now] {
            visited[now] = true;
            stack.push(now);
            now = parent[now] - 1;
        }

        if !finished[now] {
            while let Some(top) = stack.pop() {
                finished[top] = true;
                count += 1;
                if top == now { break; }
            }
        }

        for &node in &stack {
            finished[node] = true;
        }
    }

    count
}


fn main() {
    let stdin = io::stdin();
    let handle = stdin.lock();

    let mut lines = handle.lines();

    let t: i32 = lines.next().unwrap().unwrap().trim().parse().unwrap();

    for _ in 0..t {
        let n: usize = lines.next().unwrap().unwrap().trim().parse().unwrap();

        let parent: Vec<usize> = lines
            .next()
            .unwrap()
            .unwrap()
            .trim()
            .split_whitespace()
            .map(|num| num.parse().unwrap())
            .collect();

        println!("{}", n - find_cycles(&parent));
    }
}
