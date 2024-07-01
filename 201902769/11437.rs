use std::io;
use std::collections::VecDeque;
fn calculate_height(edges :&Vec<Vec<usize>>, height: &mut Vec<usize>, parent: &mut Vec<usize>) {
    let mut queue = VecDeque::new();
    
    height[1] = 1;
    queue.push_back(1);

    while !queue.is_empty() {
        let cur = queue.pop_back().unwrap();
        for i in &edges[cur] {
            if height[*i] == 0 {
                queue.push_back(*i);
                height[*i] = height[cur] + 1;
                parent[*i] = cur;
            }
        }
    }
}

fn lca(mut a: usize, mut b: usize, height: &Vec<usize>, parent: &Vec<usize>) -> usize {
    if height[a] < height[b] {
        std::mem::swap(&mut a, &mut b);
    }

    while height[a] != height[b] {
        a = parent[a];
    }

    while a != b {
        a = parent[a];
        b = parent[b];
    }

    return a;
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let n: usize = input.trim().parse().unwrap();
    let mut edges = vec![Vec::new();n+1];
    let mut height = vec![0;n+1];
    let mut parent = vec![0;n+1];

    for _ in 0..n-1 {
        input.clear();
        io::stdin().read_line(&mut input).unwrap();
        let edge: Vec<usize> = input
            .split_whitespace()
            .map(|x| x.parse().unwrap())
            .collect();
        
        edges[edge[0]].push(edge[1]);
        edges[edge[1]].push(edge[0]);
    }
    calculate_height(&mut edges,&mut height, &mut parent);

    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let m: usize = input.trim().parse().unwrap();
    for _ in 0..m {
        input.clear();
        io::stdin().read_line(&mut input).unwrap();
        let nodes: Vec<usize> = input.split_whitespace().map(|x| x.parse().unwrap()).collect();

        println!("{}", lca(nodes[0], nodes[1], &height, &parent));
    }
}
