pub fn main() {
    const MAX_2N: usize = 123456 * 2;
    let mut prime_arr = [true; MAX_2N + 1];
    prime_arr[0] = false;
    prime_arr[1] = false;
    for i in 2..prime_arr.len() {
        if prime_arr[i] == false {
            continue;
        }

        for mul in 2.. {
            if i * mul >= prime_arr.len() {
                break;
            }

            prime_arr[i * mul] = false;
        }
    }

    let stdin = std::io::stdin();
    let mut buf = String::new();

    loop {
        buf.clear();
        stdin.read_line(&mut buf).unwrap();
        let n: i32 = buf.trim().parse().unwrap();

        if n == 0 {
            break;
        }

        let mut count = 0;
        for i in n+1..=2 * n {
            if prime_arr[i as usize] {
                count += 1;
            }
        }

        println!("{}", count);
    }
}
