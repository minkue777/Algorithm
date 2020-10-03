from typing import Dict, List


def get_args():
    word = input()
    return word


def convert_to_upper_case(word: str) -> str:
    transfer: int = ord('A') - ord('a')
    reverted_word: List[str] = [chr(ord(c) + transfer) if 'a' <= c <= 'z' else c for c in word]
    return ''.join(reverted_word)


def count_characters(word: str) -> Dict:
    count: Dict = {}
    for c in word:
        count[c] = count.get(c, 0) + 1
    return count


def solution(word: str):
    word: str = convert_to_upper_case(word)
    count: Dict = count_characters(word)
    max_count: int = 0
    duplicate: bool = False
    max_character: str = ''

    for k, v in count.items():
        if max_count < v:
            max_character = k
            max_count = v
            duplicate = False
        elif max_count == v:
            duplicate = True

    print(max_character if not duplicate else '?')


def main():
    word = get_args()
    solution(word)


if __name__ == '__main__':
    main()