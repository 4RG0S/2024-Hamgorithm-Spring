use std::io;
use std::collections::VecDeque;
fn calculate_height(n : usize, edges :&Vec<Vec<(usize, i32)>>, height: &mut Vec<usize>, parent: &mut Vec<usize>) -> Vec<i32> {
    let mut queue = VecDeque::new();
    let mut distance = vec![0;n+1];
    height[1] = 1;
    queue.push_back((1, 0));

    while !queue.is_empty() {
        let (cur, cur_distance) = queue.pop_back().unwrap();
        for (next, edge_distance) in &edges[cur] {
            if height[*next] == 0 {
                let next_distance = cur_distance + *edge_distance;
                queue.push_back((*next, next_distance));
                distance[*next] = next_distance;
                height[*next] = height[cur] + 1;
                parent[*next] = cur;
            }
        }
    }
    distance
}

fn lca(mut a: usize, mut b: usize, height: &Vec<usize>, parent: &Vec<usize>, distance : &Vec<i32>) -> i32 {
    let answer = distance[a] + distance[b];
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

    answer - distance[a]*2
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
        let edge: Vec<&str> = input.trim().split_whitespace().collect();
        
        let from = edge[0].parse::<usize>().unwrap();
        let to = edge[1].parse::<usize>().unwrap();
        let cur_distance = edge[2].parse::<i32>().unwrap();

        edges[from].push((to, cur_distance));
        edges[to].push((from, cur_distance));
    }
    let distance = calculate_height(n, &edges,&mut height, &mut parent);
    
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let m: usize = input.trim().parse().unwrap();
    for _ in 0..m {
        input.clear();
        io::stdin().read_line(&mut input).unwrap();
        let nodes: Vec<usize> = input.split_whitespace().map(|x| x.parse().unwrap()).collect();

        println!("{}", lca(nodes[0], nodes[1], &height, &parent, &distance));
    }
}
