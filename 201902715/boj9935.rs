pub fn main() {
    let mut string = String::new();
    let mut bomb = String::new();
    let stdin = std::io::stdin();

    stdin.read_line(&mut string).unwrap();
    let string = string.trim();

    stdin.read_line(&mut bomb).unwrap();
    let bomb = bomb.trim();
    let last_ch_of_bomb = bomb.chars().rev().next().unwrap();

    let mut stack: Vec<char> = Vec::new();
    let mut buf: Vec<char> = Vec::new();

    for ch in string.chars() {
        stack.push(ch);
        if ch.eq(&last_ch_of_bomb) {
            let mut reversed_bomb = bomb.chars().rev();
            loop {
                let current_cmp = reversed_bomb.next();
                if current_cmp.is_none() {
                    buf.clear();
                    break;
                } else {
                    let current_cmp = current_cmp.unwrap();
                    let last_elem_of_stack = stack.pop();
                    if last_elem_of_stack.is_none() {
                        break;
                    } else {
                        let last_elem_of_stack = last_elem_of_stack.unwrap();
                        buf.push(last_elem_of_stack);
                        if !last_elem_of_stack.eq(&current_cmp) {
                            break;
                        }
                    }
                }
            }
            while !buf.is_empty() {
                stack.push(buf.pop().unwrap());
            }
        }
    }

    if stack.is_empty() {
        print!("FRULA");
    } else {
        for ch in stack {
            print!("{}", ch);
        }
    }
}
