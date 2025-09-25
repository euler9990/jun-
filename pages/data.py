import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

st.title('간단한 데이터 시각화 앱')

# 한글 폰트 설정 (NanumGothic)
font_path = 'fonts/NanumGothic-Regular.ttf'
fontprop = fm.FontProperties(fname=font_path)

# 샘플 데이터 생성
np.random.seed(42)
data = pd.DataFrame({
	'x': np.arange(1, 101),
	'y': np.random.randn(100).cumsum()
})

st.subheader('데이터 테이블')
st.dataframe(data)

st.subheader('라인 차트')
st.line_chart(data, x='x', y='y')

st.subheader('히스토그램')
fig, ax = plt.subplots()
ax.hist(data['y'], bins=20, color='skyblue', edgecolor='black')
ax.set_title('히스토그램', fontproperties=fontprop)
ax.set_xlabel('값', fontproperties=fontprop)
ax.set_ylabel('빈도', fontproperties=fontprop)
st.pyplot(fig)
