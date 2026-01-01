import time


def get_current_timestamp():
    """返回当前时间戳（秒，带小数）"""
    return time.time()


def timestamp_to_readable(ts):
    """将时间戳转换为可读的日期时间字符串"""
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))


def main():
    print("=== 时间戳计算工具 ===\n")

    # 获取当前时间戳
    current_ts = get_current_timestamp()
    print(f"当前时间戳：{current_ts:.6f} 秒")
    print(f"当前可读时间：{timestamp_to_readable(current_ts)}\n")

    # 用户输入数据
    try:
        input_data = float(input("请输入一个数字（将乘以50计算偏移）："))

        # 计算偏移量并得到新时间戳
        offset = input_data * 50
        future_ts = current_ts + offset

        print(f"\n计算过程：")
        print(f"输入值 × 50 = {input_data} × 50 = {offset} 秒（偏移量）")
        print(f"未来时间戳：{future_ts:.6f} 秒")
        print(f"对应可读时间：{timestamp_to_readable(future_ts)}")

        # 如果偏移是负数，也会显示过去的时间
        if offset > 0:
            print(f"（这是当前时间 + {offset:.2f} 秒后的时间点）")
        elif offset < 0:
            print(f"（这是当前时间 - {abs(offset):.2f} 秒前的时间点）")
        else:
            print(f"（偏移为0，与当前时间相同）")

    except ValueError:
        print("输入无效！请输入一个数字。")


if __name__ == "__main__":
    main()
