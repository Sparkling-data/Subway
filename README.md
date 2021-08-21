# Subway
지하철 이용 정보

<h2> : 주제선정</p>
&nbsp; : 오프라인교육했을때 대부분이 지하철을 이용했는데, 여기서 지하철 관련 데이터를 이용하고자 하는 아이디어가 나옴:</p>
</p>	


<br><br><br>!

<!-- 날짜별 진행과정-->
<h2> :calendar: Progress by date
&nbsp;&nbsp;&nbsp;<h3><details><summary> 첫번째 회의 [210708] </summary></p>
&nbsp;&nbsp;&nbsp;1. 아이디어 활용방안 논의 및 결정 : </p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 코로나로 인한 평일과 주말의 유동인구차이 분석</p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 지하철 칸의 혼잡도 분석</p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 1호선의 어르신들이 많은거같은데 기분탓일까? 분석</p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 월별로 특히 사람이 많이 몰리는 곳(12월의 명동 같은...)을 피할 수 있도록 유동인구 분석</p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 시간대별 이용자수 분석</p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 늦은시간에 승차인이 많은 곳 = 서울내 핫플인증인것같은데 이를 분석</p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 여기서 '1호선의 어르신들이 많은거같은데 기분탓일까? 분석' 아이디어와 '월별로 특히 사람이 많이 몰리는 곳(12월의 명동 같은...)을 피할 수 있도록 유동인구 분석' 아이디어 채택</p>
&nbsp;&nbsp;&nbsp;2. 데이터 수집 </p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 티머니 사이트 지하철 데이터 - https://www.t-money.co.kr/ncs/pct/ugd/ReadTrcrStstList.dev;jsessionid=H5SkfKE0ckd3Faql1OL6Kg2ddeCpmp6JvU5HdmdScaPWLdhNJo3s0jc0rSpfTiN1.czzw01ip_servlet_tmyweb</p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 202101~202105 지하철 호선별 역별 이용자수 - http://data.seoul.go.kr/dataList/OA-12914/S/1/datasetView.do</p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 전철 지하철 2019 요일별 승하차 총합 데이터 - https://gits.gg.go.kr/gtdb/web/trafficDb/railRoad/TransitSWPass.do</p>


&nbsp;&nbsp;&nbsp;<h3><details><summary> 두번째 회의 [210710] </summary></p>
&nbsp;&nbsp;&nbsp;1. 페이지 구상 아이디어 회의 </p>
&nbsp;&nbsp;&nbsp;2. 사용할 기술셋 결정</p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 판다스</p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- html</p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- chart</p>
&nbsp;&nbsp;&nbsp;3. 각자 역할 분담</p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 태영 : 티머니 데이터(무임승차 표) 정제(1명) > 일단 1달만 테스트 > 호선별로 분류하고 차트를 그려서 무임승차 수가 많은 역을 따로 빼서 분석</p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 재선, 유경, 선영 : 티머니 월별 총 승차수 데이터 정제 -> 전체호선(X), 호선 후보 : 1~5호선 -> 티머니 사이트에서 2020(코로나)1월 ~ 12월(3명) > 4개월분
	> 재선(1~4), 유경(5~8), 선영(9~12) > 공통 데이터 프레임 정하기 > 월요일에 회의전까지 차트 1개씩은 그려보고 공통 데이터프레임 생각해오기</p>

&nbsp;&nbsp;&nbsp;<h3><details><summary> 세번째 회의 [210713] </summary></p>
&nbsp;&nbsp;&nbsp;1. 중간점검 </p>
&nbsp;&nbsp;&nbsp;2. 추가 역할 분담</p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 태영 :  무임승차 표 스스로 작품완성</p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 재선 : 월별 데이터(데이터 정제(1~12) > 45호선)</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 유경 : 월별 데이터(데이터 정제(1~12) > 123호선)</p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 선영 : 시간별 이용현황 다중 선택지로 user가 선택할 수 있도록</p>

</details> 


&nbsp;&nbsp;&nbsp;<h3><details><summary> 네번째 및 마지막 회의 [210716, 210717] </summary></p>
&nbsp;&nbsp;&nbsp;1. 각자 만든것 합치기</p>
&nbsp;&nbsp;&nbsp;2. html연결 문제 해결</p>

</details>

<br><br><br>
