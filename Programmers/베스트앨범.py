def solution(genres, plays):
    answer = [] # 정답을 담을 리스트
    genre_dict = {} # 장르별로 노래의 인덱스와 재생횟수를 담을 딕셔너리
    genre_play_dict = {} # 장르별로 노래의 총 재생횟수를 담을 딕셔너리
    for i in range(len(genres)): # 장르별로 노래의 인덱스와 재생횟수를 딕셔너리에 저장
        genre_list = genre_dict.get(genres[i], []) # 해당 장르의 노래가 없으면 빈 리스트를 생성
        genre_list.append((i, plays[i])) # 해당 장르의 노래 리스트에 노래의 인덱스와 재생횟수를 추가
        genre_dict[genres[i]] = genre_list # 딕셔너리에 저장
        genre_play_dict[genres[i]] = genre_play_dict.get(genres[i], 0) + plays[i] # 해당 장르의 총 재생횟수를 저장
    sorted_genre = sorted(genre_play_dict.items(), key=lambda x: x[1], reverse=True) # 장르별 총 재생횟수를 기준으로 내림차순 정렬
    for genre, _ in sorted_genre: # 장르별로 노래의 인덱스와 재생횟수를 정렬
        sorted_genre_dict = sorted(genre_dict[genre], key=lambda x: (-x[1], x[0])) # 재생횟수를 기준으로 내림차순 정렬하고, 재생횟수가 같으면 인덱스를 기준으로 오름차순 정렬
        print(sorted_genre_dict) # 정렬된 리스트 출력
        answer.append(sorted_genre_dict[0][0]) # 장르별로 가장 많이 재생된 노래의 인덱스를 정답 리스트에 추가
        if len(sorted_genre_dict) > 1: # 장르별로 노래가 2개 이상이면
            answer.append(sorted_genre_dict[1][0]) # 두 번째로 많이 재생된 노래의 인덱스를 정답 리스트에 추가
    return answer # 정답 반환