use std::io::{self, Write};

struct UnionFind {
    parent: Vec<usize>,
    distance_to_parent: Vec<usize>,
}

impl UnionFind {
    fn new(n: usize) -> Self {
        UnionFind {
            parent: (0..n).collect(),
            distance_to_parent: vec![0; n],
        }
    }

    fn find(&mut self, x: usize) -> (usize, usize) {
        if self.parent[x] == x {
            return (x, 0);
        }
        let (grandparent, distance_to_grandparent) = self.find(self.parent[x]);
        self.parent[x] = grandparent;
        self.distance_to_parent[x] += distance_to_grandparent;
        (grandparent, self.distance_to_parent[x])
    }

    fn union(&mut self, x: usize, y: usize) {
        let (parent_x, distance_to_parent_x) = self.find(x);
        let (parent_y, distance_to_parent_y) = self.find(y);
        if parent_x == parent_y {
            return;
        }
        self.parent[parent_x] = parent_y;
        self.distance_to_parent[parent_x] = distance_to_parent_y + (x as isize - y as isize).abs() as usize % 1000;
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let t: usize = input.trim().parse().unwrap();
    let mut output = String::new();
    for _ in 0..t {
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        let n: usize = input.trim().parse().unwrap();
        let mut union_find = UnionFind::new(n);
        loop {
            let mut input = String::new();
            io::stdin().read_line(&mut input).unwrap();
            let command: Vec<&str> = input.trim().split_whitespace().collect();
            match command[0] {
                "O" => break,
                "E" => {
                    let i: usize = command[1].parse().unwrap();
                    let (parent, distance) = union_find.find(i - 1);
                    output += &format!("{}\n", distance);
                }
                "I" => {
                    let i: usize = command[1].parse().unwrap();
                    let j: usize = command[2].parse().unwrap();
                    union_find.union(i - 1, j - 1);
                }
                _ => unreachable!(),
            }
        }
    }
    io::stdout().write_all(output.as_bytes()).unwrap();
}
