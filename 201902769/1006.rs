use std::io;

// 원이 아닌 평면일 경우
fn circulate(n: usize, w: i32, circle: &Vec<Vec<i32>>) -> i32 {
    // dp[i] = circle[0][i] 묶지 않는 i까지 배열의 최대 수
    let mut dp_1 = vec![0;n];
    // dp[i] = circle[1][i] 묶지 않는 i까지 배열의 최대 수
    let mut dp_2 = vec![0;n];
    // dp[i] = i까지 배열의 최대 수
    let mut dp_3 = vec![0;n];

    if circle[0][0] + circle[1][0] <= w {
        dp_3[0] = 1;
    }

    // dp_1[i]의 경우 : max(dp_3[i-1], dp_2[i-1] + 1)
    // dp_2[i]의 경우 : max(dp_3[i-1], dp_1[i-1] + 1)
    // dp_3[i]의 경우 : max(dp_1[i], dp_2[i], dp_3[i-1] + 1(위아래 경우), dp_3[i-2] + 2(좌우 2개))
    for i in 1..n {
        if i > 1 {
            dp_3[i] = dp_3[i-2];
        }
        
        if circle[0][i] + circle[0][i-1] <= w {
            dp_2[i] = i32::max(dp_3[i-1], dp_1[i-1] + 1);
            dp_3[i] += 1;
        }   
        else {
            dp_2[i] = dp_3[i-1];
        }

        if circle[1][i] + circle[1][i-1] <= w {
            dp_1[i] = i32::max(dp_3[i-1], dp_2[i-1] + 1);
            dp_3[i] += 1;
        }
        else {
            dp_1[i] = dp_3[i-1];
        }
        
        if circle[0][i] + circle[1][i] <= w {
            dp_3[i] = i32::max(dp_3[i], dp_3[i-1] + 1);
        }
        dp_3[i] = i32::max(dp_3[i], dp_3[i-1]);
        dp_3[i] = i32::max(dp_3[i], dp_2[i]);
        dp_3[i] = i32::max(dp_3[i], dp_1[i]);

    }

    // println!("{:?} {:?} {:?} {:?}", circle, dp_1, dp_2, dp_3);
    i32::max(i32::max(dp_1[n-1], dp_2[n-1]), dp_3[n-1])
}   

fn main() {
    let stdin = io::stdin();
    let mut input = String::new();

    stdin.read_line(&mut input).unwrap();
    let t: usize = input.trim().parse().unwrap();

    for _ in 0..t {
        input.clear();
        stdin.read_line(&mut input).unwrap();
    
        let v: Vec<i32> = input.split_whitespace().map(|x| x.parse().unwrap()).collect();
        let n = v[0] as usize;
        let w = v[1];

        let circle: Vec<Vec<i32>> = (0..2).map(|_| {
            input.clear();
            stdin.read_line(&mut input).unwrap();
            input.split_whitespace().map(|x| x.parse().unwrap()).collect()
        }).collect();

        let mut merge_count = 0;
        //원일 경우는 총 4가지.
        // 안묶일 경우
        merge_count = circulate(n, w, &circle);

        if n == 1 {
            println!("{:?}", n as i32 * 2 - merge_count );
            continue;
        }
        //circle[0][0] & circle[0][-1] 이 묶일 경우
        if circle[0][0] + circle[0][n-1] <= w {
            let mut cloned_circle = circle.clone();
            cloned_circle[0][0] = w + 1; // 사용하지 못하게 잠금
            cloned_circle[0][n-1] = w + 1; // 사용하지 못하게 잠금
            merge_count = i32::max(merge_count, circulate(n, w, &cloned_circle) + 1);
        }
        //circle[1][0] & circle[1][-1] 이 묶일 경우
        if circle[1][0] + circle[1][n-1] <= w {
            let mut cloned_circle = circle.clone();
            cloned_circle[1][0] = w + 1; // 사용하지 못하게 잠금
            cloned_circle[1][n-1] = w + 1; // 사용하지 못하게 잠금
            merge_count = i32::max(merge_count, circulate(n, w, &cloned_circle) + 1);
        }
        //둘 다 묶일 경우
        if circle[0][0] + circle[0][n-1] <= w && circle[1][0] + circle[1][n-1] <= w {
            let mut cloned_circle = circle.clone();
            cloned_circle[0][0] = w + 1; // 사용하지 못하게 잠금
            cloned_circle[0][n-1] = w + 1; // 사용하지 못하게 잠금
            cloned_circle[1][0] = w + 1; // 사용하지 못하게 잠금
            cloned_circle[1][n-1] = w + 1; // 사용하지 못하게 잠금
            merge_count = i32::max(merge_count, circulate(n, w, &cloned_circle) + 2);
        }
        println!("{:?}", n as i32 * 2 - merge_count );
    }
    
}