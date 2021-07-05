# Sentiment_Analysis

## 주의사항

- Pororo 최신 버전에서는 Sentiment Analysis 관련 버그가 있습니다. (model args 누락) 
- 해당 분석 기능을 사용하시려면 다음 사항을 수정하셔야 합니다.

---

- models > brainbert > BrainRoBERTa.py
- predict_output()

<pre><code>assert self.args.task == "sentence_prediction" ## 주석처리</code></pre>
<pre><code>self.args.regression_target ## 원하는 결과 type에 맞게 boolean으로 치환</code></pre>

---

## 사용법

1. input 폴더에 지정된 형식의 json 파일 추가
2. input_list.py 에 추가된 json 파일명 기입
3. main.py 실행

---

## 사용 라이브러리

- PORORO (https://github.com/kakaobrain/pororo)