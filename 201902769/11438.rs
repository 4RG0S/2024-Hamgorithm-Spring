use std::io::{self, Write, BufRead, BufReader, BufWriter};
use std::collections::VecDeque;

fn calculate_height(edges: &Vec<Vec<usize>>, n: usize) -> (Vec<Vec<usize>>, Vec<usize>) {
    let mut parent: Vec<Vec<usize>> = vec![vec![1; ((n as f64).log2().ceil() as usize) + 2]; n + 1];
    let mut height: Vec<usize> = vec![0; n + 1];

    let mut queue = VecDeque::new();
    height[1] = 1;
    queue.push_back(1);

    while let Some(cur) = queue.pop_front() {
        for &next in &edges[cur] {
            if height[next] == 0 {
                parent[next][0] = cur;
                height[next] = height[cur] + 1;
                queue.push_back(next);
            }
        }
    }

    for i in 1..parent[0].len() {
        for j in 1..=n {
            if parent[j][i - 1] != 0 {
                let temp = parent[j][i - 1];
                parent[j][i] = parent[temp][i - 1];
            }
        }
    }

    (parent, height)
}

fn lca(mut a: usize, mut b: usize, parent: &Vec<Vec<usize>>, height: &Vec<usize>) -> usize {
    if height[a] < height[b] {
        std::mem::swap(&mut a, &mut b);
    }

    let log_n = parent[0].len() - 1;
    for i in (0..=log_n).rev() {
        if height[a] - height[b] >= 1 << i {
            a = parent[a][i];
        }
    }

    if a == b {
        return a;
    }

    for i in (0..=log_n).rev() {
        if parent[a][i] != parent[b][i] {
            a = parent[a][i];
            b = parent[b][i];
        }
    }

    parent[a][0]
}


fn main() {
    let stdin = io::stdin();
    let reader = BufReader::new(stdin);
    let stdout = io::stdout();
    let mut writer = BufWriter::new(stdout);

    let mut lines = reader.lines();
    let n: usize = lines.next().unwrap().unwrap().trim().parse().unwrap();
    let mut edges: Vec<Vec<usize>> = vec![Vec::new(); n + 1];

    for line in lines.by_ref().take(n - 1) {
        let edge: Vec<usize> = line.unwrap().split_whitespace().map(|x| x.parse().unwrap()).collect();
        edges[edge[0]].push(edge[1]);
        edges[edge[1]].push(edge[0]);
    }

    let (parent, height) = calculate_height(&edges, n);
    let m: usize = lines.next().unwrap().unwrap().trim().parse().unwrap();

    for line in lines.take(m) {
        let nodes: Vec<usize> = line.unwrap().split_whitespace().map(|x| x.parse().unwrap()).collect();
        writeln!(writer, "{}", lca(nodes[0], nodes[1], &parent, &height)).unwrap();
    }

    writer.flush().unwrap();
}
