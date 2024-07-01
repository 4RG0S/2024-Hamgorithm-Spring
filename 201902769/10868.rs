use std::io::{BufRead, Write};

fn build_tree(arr: &[i32], tree: &mut Vec<i32>, node: usize, start: usize, end: usize) {
    if start == end {
        tree[node] = arr[start];
    } else {
        let mid = (start + end) / 2;
        build_tree(arr, tree, 2 * node + 1, start, mid);
        build_tree(arr, tree, 2 * node + 2, mid + 1, end);
        tree[node] = tree[2 * node + 1].min(tree[2 * node + 2]);
    }
}

fn search(tree: &Vec<i32>, cur: usize, start: usize, end: usize, left: usize, right: usize) -> i32 {
    if right < start || end < left {
        return i32::MAX;
    }
    
    if left <= start && end <= right {
        return tree[cur];
    }
    
    let mid = (start + end) / 2;
    let left_min = search(tree, 2*cur + 1, start, mid, left, right);
    let right_min = search(tree, 2*cur + 2, mid+1, end, left, right);
    
    i32::min(left_min, right_min)
}

fn main() {
    let reader = std::io::BufReader::new(std::io::stdin());
    let mut writer = std::io::BufWriter::new(std::io::stdout());

    let mut lines = reader.lines();
    let nm: Vec<usize> = lines.next().unwrap().unwrap().split_whitespace().map(|x| x.parse().unwrap()).collect();
    let (n, m) = (nm[0], nm[1]);

    let mut arr: Vec<i32> = vec![0;n];
    for i in 0..n {
        let cur: i32 = lines.next().unwrap().unwrap().trim().parse().unwrap();
        arr[i] = cur;
    }

    let mut tree: Vec<i32> = vec![0; n*4];
    build_tree(&arr, &mut tree, 0, 0, n-1);
    for _ in 0..m {
        let nodes: Vec<usize> = lines.next().unwrap().unwrap().split_whitespace().map(|x| x.parse().unwrap()).collect();
        writeln!(writer, "{}", search(&tree, 0, 0, n - 1, nodes[0] - 1, nodes[1] - 1)).unwrap();
    }
    writer.flush().unwrap();
}
