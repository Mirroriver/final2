import ipaddress
import csv
import json

input_file = "dbip-country-lite-2025-06.csv"
output_file = "ip_country_ranges.json"

result = []

with open(input_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        try:
            start = int(ipaddress.IPv4Address(row[0].strip('"')))
            end = int(ipaddress.IPv4Address(row[1].strip('"')))
        except ipaddress.AddressValueError:
            continue  # 跳过不是IPv4的行
        country = row[2].strip('"')
        result.append([start, end, country])

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(result, f)

print(f"转换完成，已保存为 {output_file}")
