/*
증가하는 방향이,
짝수 애들은 1/n --> n/1로 가고
홀수 애들은 n/1 --> 1/n으로 간다.

시작하는 1/n 혹은 n/1은 (1 + 2 + ... + n-1) + 1 번째 숫자이다.

n (n - 1) / 2
*/

enum Direction {
    Up,
    Down,
}

fn get_direction(n: i32) -> Direction {
    if n % 2 == 0 {
        Direction::Down
    } else {
        Direction::Up
    }
}

fn get_start_number(n: i32) -> (i32, i32) {
    if n % 2 == 0 {
        (1, n)
    } else {
        (n, 1)
    }
}

fn sum_to_n_minus_1(n: i32) -> i32 {
    n * (n - 1) / 2
}

pub fn main() {
    let mut buf = String::new();
    let stdin = std::io::stdin();

    stdin.read_line(&mut buf).unwrap();

    let x: i32 = buf.trim().parse().unwrap();

    let mut most_close_n = -1;
    let mut most_close_distance = std::i32::MAX;
    let mut n = 1;

    loop {
        let sum = sum_to_n_minus_1(n);
        let distance = x - sum - 1;
        if distance < 0 {
            break;
        }

        if distance < most_close_distance {
            most_close_distance = distance;
            most_close_n = n;
        } else {
            break;
        }

        n += 1;
    }

    let direction = get_direction(most_close_n);
    let distance = x - sum_to_n_minus_1(most_close_n) - 1;

    // println!("{} {}", most_close_n, distance);

    let mut result = get_start_number(most_close_n);

    for _ in 0..distance {
        match direction {
            Direction::Up => {
                result.0 -= 1;
                result.1 += 1;
            }
            Direction::Down => {
                result.0 += 1;
                result.1 -= 1;
            }
        }
    }

    println!("{}/{}", result.0, result.1);
}
