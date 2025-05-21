pip install streamlit

# ファイル名：personality_test.py

import streamlit as st

st.title("あなたの性格を診断します")
st.write("以下の5つの質問に答えてください")

# 質問パート（ラジオボタンで選択）
Q1 = st.radio("Q1. 新しいことに挑戦するのが好きですか？", ("はい", "いいえ"))
Q2 = st.radio("Q2. 困っている人がいると、つい助けたくなりますか？", ("はい", "いいえ"))
Q3 = st.radio("Q3. 一人で過ごす時間が好きですか？", ("はい", "いいえ"))
Q4 = st.radio("Q4. 物事を決めるときは感情よりも論理を重視しますか？", ("はい", "いいえ"))
Q5 = st.radio("Q5. 周囲にどう思われているかを気にする方ですか？", ("はい", "いいえ"))

# 診断ボタン
if st.button("診断する"):
    score = [Q1, Q2, Q3, Q4, Q5].count("はい")


    if score <= 1:
        result = "慎重な観察者タイプ"
        desc = "一人での時間を大切にし、深く考える力があります。信頼されるタイプです。"
    elif score <= 3:
        result = "バランス型"
        desc = "柔軟に対応できるタイプ。個人でもチームでも力を発揮できます。"
    else:
        result = "行動派リーダータイプ"
        desc = "挑戦を恐れず、エネルギッシュに行動するリーダー気質です。"

    st.subheader(f"診断結果: {result}")
    st.write(desc)

    # メール入力欄
    email = st.text_input("もっと詳しく知りたい場合はメールアドレスを入力してください")
    if email:
        st.success(f"{email} 宛に詳細情報をお送りします（※送信処理は未実装）")
