from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

import streamlit as st

st.title("専門家に聞いてみよう")

st.write("専門家の種類を選択し、質問内容を入力してください。AI専門家が答えてくれます。")

selected_item = st.radio(
    "専門家を選択してください。",
    ["マーケティング", "営業"]
)

input_message = st.text_input(label="専門家への質問を入力してください。")
text_count = len(input_message)

#質問回答する関数
def answer_question(selected_item, input_message):
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    messages = [
        SystemMessage(content=f"あなたは{selected_item}の専門家です。入力された質問に専門家として回答します。回答の冒頭に「{selected_item}の専門家として回答します。」と書いてください。"),
        HumanMessage(content=f"{input_message}"),
    ]
    result = llm(messages)
    return result.content


if st.button("実行"):
    st.divider()

    if selected_item and input_message:
        answer = answer_question(selected_item, input_message)
        st.write(answer)

    else:
        st.error("専門家を選択し、質問内容を入力してください。")