from typing import List
def generate_combinations(options: List[str], size: int) -> List[List[str]]:

    if size == 0:
        return [[]]
    else:
        res = []
        for i in range(len(options)):
            sub_options = options[:i] + options[i+1:]
            sub_res = generate_combinations(sub_options, size-1)

            for sub in sub_res:
                sub.append(options[i])
                res.append(sub)
            
        return res


def main():
    options = list(range(1, 7))
    print(options)
    res = generate_combinations(options, 3)
    print(res)
    print(len(res))

main()