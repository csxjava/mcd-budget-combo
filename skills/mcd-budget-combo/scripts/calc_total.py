import json
import sys

def main():
    """输入 JSON 数组:[{"name":"...","price":数字,"kcal":数字,"qty":整数}, ...]"""
    items = json.loads(sys.stdin.read())
    total_price = sum(i["price"] * i.get("qty", 1) for i in items)
    total_kcal = sum(i.get("kcal", 0) * i.get("qty", 1) for i in items)
    print(json.dumps(
        {"total_price": round(total_price, 2), "total_kcal": round(total_kcal)},
        ensure_ascii=False,
    ))

if __name__ == "__main__":
    main()