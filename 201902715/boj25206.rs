fn grade_to_score(grade: &str) -> f64 {
    match grade.trim() {
        "A+" => 4.5,
        "A0" => 4.0,
        "B+" => 3.5,
        "B0" => 3.0,
        "C+" => 2.5,
        "C0" => 2.0,
        "D+" => 1.5,
        "D0" => 1.0,
        "F" => 0.0,
        _ => panic!(),
    }
}

pub fn main() {
    let stdin = std::io::stdin();
    let mut buf = String::new();

    let mut time_sum = 0.0;
    let mut score_sum = 0.0;

    for _ in 0..20 {
        buf.clear();
        stdin.read_line(&mut buf).unwrap();
        let split = buf.split(" ").collect::<Vec<&str>>();
        let time = split.get(1).unwrap().parse::<f64>().unwrap();
        let grade = split.get(2).unwrap();

        if grade.trim().eq("P") {
            continue;
        }

        let score = grade_to_score(grade);
        time_sum += time;
        score_sum += score * time;
    }

    println!("{}", score_sum / time_sum);
}
