airports = ['Alxa 레프트배너 Bayanhot 공항(중국)', 'Holingol Huolinhe 공항(중국)', '고치 공항(일본)', '광주 공항(대한민국)', '군산 공항(대한민국)', '김포 국제공항(대한민국)', '김해 국제공항(대한민국)', '노토 공항(일본)', '다네가시마 공항(일본)', '대구 국제공항(대한민국)', '델린가 공항(중국)', '레분 공항(일본)', '무안 국제공항(대한민국)', '미야자키 공항(일본)', '미호 공항(일본)', '바이윤 공항(중국)', '불산 샤디 공항(중국)', '사천 공항(대한민국)', '센다이 공항(일본)', '아구니 공항(일본)', '아마미 공항(일본)', '아오모리 공항(일본)', '양양 국제공항(대한민국)', '여수 공항(대한민국)', '오비히로 공항(일본)', '오쿠시리 공항(일본)', '요룬 공항(일본)', '울산 공항(대한민국)', '원주 공항(대한민국)', '위린 푸미안 공항(중국)', '인천 국제공항(대한민국)', '제주 국제공항(대한민국)', '조양 공항(중국)', '창덕 타오화원 공항(중국)', '청주 국제공항(대한민국)', '충칭 우산 공항(중국)', '토하마 /토이아마 공항(일본)', '포항 공항(대한민국)', '한단 공항(중국)', '항저우 지오샨 국제공항(중국)', '호홋 바이타 국제공항(중국)']

korea_airport = []

for i in airports:
    if i[-6:] == "(대한민국)":
        korea_airport.append(i)

print(korea_airport)