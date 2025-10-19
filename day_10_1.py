# 求 1 到 n 的和
def sum_to_n(n):
    return sum(range(1, n + 1))

if __name__ == "__main__":
    n = int(input("请输入一个正整数: "))
    print(f"1 到 {n} 的和是: {sum_to_n(n)}")