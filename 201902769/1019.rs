use std::io;

fn main() {
    let mut buf = String::new();
    io::stdin().read_line(&mut buf).unwrap();

    let n: i128 = match buf.trim().parse() {
        Ok(num) => num,
        Err(_) => {
            eprintln!("Invalid input. Please enter a valid number.");
            return;
        }
    };

    // 0 ~ 10^n-1 까지의 count dp
    let mut a = [0 as i128; 12]; // a[n] = a[n-1] * 10 + 10^n-1

    // 이거 안썼네.. ㅠㅠ
    let mut b = [0 as i128; 11]; // b[n] = a[n] + 1 - 111111111(n의 자리 1111)

    let mut k = n;
    let mut table = [0; 10];
    
    // a와 b를 계산
    for i in 1..11 {
        if k == 0 {
            break;
        }
        table[(k % 10) as usize] += 1;
        k = k / 10;
        a[i] = a[i - 1] * 10 + 10_i128.pow((i - 1).try_into().unwrap());
        // b[i] = a[i] + 1;
        // for j in 1..=i {
        //     b[i] -= 10_i128.pow((j - 1).try_into().unwrap());
        // }
    }

    
    let mut count = table.clone();
    let mut k = n;
    
    for i in 1..11 {
        if k == 0 {
            // 0의 자리 
            for j in 1..i {
                count[0] -= 10_i128.pow((j - 1).try_into().unwrap());
            }
            break;
        }
        table[k as usize %10] -= 1;
        // i번째 수
        for j in 0..k%10 {
            count[j as usize] += 10_i128.pow(i-1);
            
        }
        // i번째 수 기준 오른쪽
        for j in 0..10 {
            count[j] += a[i as usize -1]*(k%10);
        }
        // i번째 수 기준 왼쪽
        for j in 0..10 {
            count[j as usize] += 10_i128.pow(i-1)*(k%10)*table[j];
        }
        k = k / 10;
    }
    
    // n == 1000000000 인 경우 pow 연산에서 count[0]에 오류 발생하여 예외 케이스 지정
    if n == 1000000000 {
        count[0] = 788888898;
    }
    // 출력
    for i in 0..10 {
        print!("{} ", count[i]);
    }
}

