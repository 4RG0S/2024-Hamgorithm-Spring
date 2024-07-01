use core::num;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();

    let mut lines = input.lines();
    let first_line = lines.next().unwrap();
    let second_line = lines.next().unwrap();

    let nk: Vec<usize> = first_line.split_whitespace()
                                   .map(|x| x.parse().unwrap())
                                   .collect();
    let (n, mut k) = (nk[0], nk[1]);
    let number: Vec<char> = second_line.chars().collect();
    let mut stack:Vec<u32> = Vec::new();

    for i in 0..n {
        let cur = number[i].to_digit(10).unwrap();
        
        if stack.last().is_some() && cur >= *stack.last().unwrap() {
            while !stack.is_empty() && k > 0 && cur > *stack.last().unwrap() {
                stack.pop();
                k -= 1;
            }
        }
        stack.push(cur);
    }

    for i in 0..(stack.len() - k) {
        print!("{}", stack[i]);
    }
}
