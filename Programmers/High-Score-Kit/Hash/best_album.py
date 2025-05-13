"""코딩테스트 고득점 Kit / Level 3. 베스트 앨범"""


from collections import defaultdict


# Solution of the problem.
def solution(genres, plays):
    # Create dictionary that stores album's id and plays.
    albums = defaultdict(list)
    for _id, (genre, play) in enumerate(zip(genres, plays)):
        albums[genre].append((_id, play))

    # Sort the genres in descending order of total plays.
    sorted_albums = dict(
        sorted(
            albums.items(),
            key=lambda item: sum(p for _, p in item[1]),
            reverse=True
        )
    )

    # Sort albums within each genre in descending order of plays.
    for genre, play in sorted_albums.items():
        sorted_albums[genre] = sorted(play, key=lambda p: p[1], reverse=True)

    # Select up to two top songs from each genre.
    best_albums = []
    for album in sorted_albums.values():
        count = 0
        for album_id, _ in album:
            if count < 2:
                best_albums.append(album_id)
                count += 1

    return best_albums


# Test cases for solutions.
def testcases():
    testcase = [
        {
            'genres': ['classic', 'pop', 'classic', 'classic', 'pop'],
            'plays': [500, 600, 150, 800, 2500],
        },
        {
            'genres': ['classic', 'pop', 'classic', 'classic'],
            'plays': [500, 600, 150, 800],
        },
    ]
    return testcase


def main():
    for testcase in testcases():
        answer = solution(testcase.get('genres'), testcase.get('plays'))
        print(answer)


if __name__ == '__main__':
    main()
