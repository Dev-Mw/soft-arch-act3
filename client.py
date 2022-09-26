# -*- Coding: utf-8 -*-
import sys
import time
from typing import Any

import http3
import asyncio
from prettytable import PrettyTable



API_URL = 'http://localhost:3000/api'


def show_results(results: Any) -> None:
    data = results['data']
    total_records = data['total']
    records = data['matches']

    print(f'\033[1;31mTotal records: {total_records}\033[0m\n')

    x = PrettyTable()
    x.field_names = ['ID', 'IP', 'ISP', 'PORT', 'TRANSPORT', 'COUNTRY', 'CITY']

    row_id = 1
    for record in records:
        x.add_row([
            row_id,
            record['ip_str'],
            record['isp'],
            record['port'],
            record['transport'],
            record['location']['country_name'],
            record['location']['city']
        ])
        row_id += 1

    print(x)


async def request(keyword: str, count: int) -> Any:
    client = http3.AsyncClient()
    _ = await client.get(f'{API_URL}/{keyword}/{count if count else 10}', timeout=120)
    return _


async def run():
    keyword = input('\n\033[1;32mSearch for keyword: \033[0m')
    rows = input('\033[1;32mRows count [10]: \033[0m')

    if not keyword:
        print('You must specify a keyword to search for any host.\n')

    rows = rows if rows else 10

    try:
        _ = int(rows)
    except:
        print(f'{rows} is not a integer\n')
        sys.exit(1)

    results = await request(keyword, int(rows))

    show_results(results.json())


if __name__ == "__main__":
    asyncio.run(run())
