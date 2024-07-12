from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_sql_query_chain
from langchain.prompts import PromptTemplate
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from app.db.database import db
from app.core.logging_config import logger
from app.core.prompts import final_answer_prompt, sql_query_prompt
from app.core.logging_config import logger
import re

google_llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.0)

conversation_history = []

def add_to_conversation_history(user_question, sql_query, executed_query_result, final_answer, matplotlib_code):
    """
    This function is used for creating the conversation history of the LLM. We are keeping a maximum history of the most recent 3 messages.
    """
    conversation_history.append({
        "user_question": user_question,
        "sql_query": sql_query,
        "executed_query_result": executed_query_result,
        "final_answer": final_answer,
        "matplotlib_code": matplotlib_code
    })
    if len(conversation_history) > 3:
        conversation_history.pop(0)

def get_conversation_context():
    """
    This function is used for appending the context in the conversation history.
    """
    context = ""
    try:
        for interaction in conversation_history:
            context += f"User Question: {interaction['user_question']}\n"
            context += f"SQL Query: {interaction['sql_query']}\n"
            context += f"Executed Query Result: {interaction['executed_query_result']}\n"
            context += f"Final Answer: {interaction['final_answer']}\n\n"
    except:
        context = ""
    return context

def generate_sql_query(user_question, context):
    """
    This function is used for generating the corresponding SQL query from provided natural language based user question.
    """
    try:
        generate_query = create_sql_query_chain(google_llm, db)
        prompt_with_history = f"{context}User Question: {user_question}\n{sql_query_prompt}"
        sql_query = generate_query.invoke({"question": prompt_with_history})
        query_split = sql_query.split('SQLQuery: ')
        refined_sql_query = query_split[1].strip() if len(query_split) > 1 else sql_query.strip()
    except:
        refined_sql_query = ""
    return refined_sql_query

def execute_sql_query(query):
    """
    This function is used for executing the generated SQL query and fetch the corresponding result.
    """
    try:
        execute_query = QuerySQLDataBaseTool(db=db)
        executed_query_result = execute_query.invoke(query)
    except Exception as e:
        logger.error(f"Error executing SQL query: {e}")
        executed_query_result = "No result either due to a wrongly generated SQL Query or no SQL query generated at all"
    return executed_query_result

def generate_final_answer(user_question, refined_sql_query, executed_query_result, csv_content):
    """
    This function is used for finally converting the result obtained from the SQL query back to natural language which would then be understandable to the user.
    """
    try:
        answer_prompt_template = PromptTemplate.from_template(final_answer_prompt)
        answer_prompt = answer_prompt_template.format(
            question=user_question, query=refined_sql_query, result=executed_query_result, table_info=csv_content
        )
        final_answer_resp = google_llm.invoke(answer_prompt)
        final_answer = final_answer_resp if isinstance(final_answer_resp, str) else final_answer_resp.content
        match = re.search(r"```python\n(.*?)\n```", final_answer, re.DOTALL)
        if match:
            matplotlib_code = match.group(1)
            parts = re.split(r"```python\n.*?\n```", final_answer, flags=re.DOTALL)
            final_answer = parts[0]
        else:
            matplotlib_code = ""    
    except:
        final_answer = ""
        matplotlib_code = ""
    logger.info(f"matplotlib code > {matplotlib_code}")
    return final_answer, matplotlib_code
