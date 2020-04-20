from collections import Counter


def sockMerchant(pairs, socket_list):
    sock_groups = Counter(socket_list)
    pairs_found = 0

    for pair_number, values in sock_groups.items():
        if values % 2 == 0:
            pairs_found += values // 2
        else:
            while values > 2:
                _result = values // 2
                pairs_found += 1
                values -= 2
        print(f"After doing {pair_number}: {values} we found {pairs_found}")

    return pairs_found
