extern "C" {
    fn FindPrimes(start: i32, end: i32);
}

fn main() {
    unsafe {
        FindPrimes(3, 99);
    }
}
