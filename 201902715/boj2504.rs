use std::process::exit;

#[derive(PartialEq, Clone, Copy)]
enum StackElement {
    Number(i32),
    NaN(char),
}

impl StackElement {
    fn unwrap_number(self) -> Option<i32> {
        match self {
            StackElement::Number(n) => Some(n),
            _ => None,
        }
    }

    fn unwrap_nan(self) -> Option<char> {
        match self {
            StackElement::NaN(c) => Some(c),
            _ => None,
        }
    }
}

pub fn main() {
    let mut buf = String::new();
    let stdin = std::io::stdin();

    stdin.read_line(&mut buf).unwrap();

    let mut stack: Vec<StackElement> = Vec::new();

    let open = ['[', '('];
    let close = [']', ')'];

    let mut sum = 0;

    for e in buf.trim().chars() {
        // println!("\n---\n{}: {}", e, sum);

        if open.contains(&e) {
            stack.push(StackElement::Number(sum));
            sum = 0;
            // is ([
            let element = StackElement::NaN(e);
            stack.push(element);
        } else if close.contains(&e) {
            // is )]
            let mut popped_element = stack.pop();

            let current;
            let target;

            if e == ')' {
                current = e;
                target = '(';
            } else {
                current = e;
                target = '[';
            }

            loop {
                if popped_element.is_none() {
                    println!("0");
                    exit(0);
                }
                let char_element = popped_element.unwrap().unwrap_nan();
                if char_element.is_some() {
                    if char_element.unwrap().eq(&target) {
                        if sum == 0 {
                            sum = 1;
                        }
                        sum = if current == ')' { sum * 2 } else { sum * 3 };
                        
                        let mut remain_num = stack.pop();
                        while remain_num.is_some() && remain_num.unwrap().unwrap_number().is_some() {
                            sum += remain_num.unwrap().unwrap_number().unwrap();
                            remain_num = stack.pop();
                        }
                        if remain_num.is_some() {
                            stack.push(remain_num.unwrap());
                        }
                        break;
                    } else {
                        println!("0");
                        exit(0);
                    }
                }

                let num_element = popped_element.unwrap().unwrap_number();
                if num_element.is_some() {
                    sum += num_element.unwrap();
                } else {
                    println!("0");
                    exit(0);
                }

                popped_element = stack.pop();
            }
        } else {
            // is number
            let element = StackElement::Number(e.to_string().parse::<i32>().unwrap());
            stack.push(element);
        }
    }

    let remain = stack.pop();
    if remain.is_some() && remain.unwrap().unwrap_nan().is_some() {
        println!("0");
        exit(0);
    }

    println!("{}", sum);
}
