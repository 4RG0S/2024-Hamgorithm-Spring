fn is_sorted(n: usize, cards: &[usize], p: &[usize]) -> bool {
    cards.iter().enumerate().all(|(idx, &card)| card % 3 == p[idx])
}

fn shuffle(n: usize, cards: &mut [usize], s: &[usize]) {
    let mut new_cards = vec![0; n];
    for i in 0..n {
        new_cards[i] = cards[s[i]];
    }
    cards.copy_from_slice(&new_cards);
}

fn check_cycle(n: usize, init_state: &[usize], cards: &[usize], s: &[usize]) -> bool {
    init_state.iter().enumerate().all(|(i, &val)| val == cards[s[i]])
}

fn minimum_shuffles(n: usize, p: &[usize], s: &[usize]) -> i32 {
    let mut cards: Vec<usize> = (0..n).collect();
    let init_state = cards.clone();
    let mut count = 0;

    while !is_sorted(n, &cards, p) {
        if count > 0 && check_cycle(n, &init_state, &cards, s) {
            return -1;
        }

        shuffle(n, &mut cards, s);
        count += 1;
    }

    count
}

fn main() {
    let mut n = String::new();
    let mut p = String::new();
    let mut s = String::new();
    
    std::io::stdin().read_line(&mut n).unwrap();
    let n: usize = n.trim().parse().unwrap();

    std::io::stdin().read_line(&mut p).unwrap();
    let p: Vec<usize> = p.trim().split_whitespace()
                         .map(|x| x.parse().unwrap())
                         .collect();

    std::io::stdin().read_line(&mut s).unwrap();
    let s: Vec<usize> = s.trim().split_whitespace()
                         .map(|x| x.parse().unwrap())
                         .collect();

    let result = minimum_shuffles(n, &p, &s);
    println!("{}", result);
}
