from fastapi import APIRouter
from app.schemas.message import Message
from app.services.chat_service import (
    conversation_history, add_to_conversation_history, get_conversation_context, generate_sql_query,
    execute_sql_query, generate_final_answer
)
import os
from app.core.logging_config import logger

router = APIRouter()

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, '..', '..', '..', 'data', 'Finance_data.csv')
print('\n\nfile_path >', file_path)

try:
    with open(file_path, 'r') as f:
        csv_content = f.read()
    logger.info(f"CSV file loaded successfully from {file_path}")
except Exception as e:
    csv_content = None
    logger.error(f"File not found: {file_path} due to this error - {e}")

@router.get("/")
async def health_check():
    try:
        logger.info("Health check is successful")
        return {"success":1, "response":"Health check is successful"}
    except Exception as e:
        logger.error(f"Health check is unsuccessful due to some internal development issue - {e}")
        return {"success":0, "response":f"Health check is unsuccessful due to some internal development issue - {e}"}

@router.post("/chat")
async def chat(message: Message):
    try:
        logger.info(f"Chat endpoint called. User message - {message.user_message}")
        user_question = message.user_message
        conversation_context = get_conversation_context()
        refined_sql_query = generate_sql_query(user_question, conversation_context)
        executed_query_result = execute_sql_query(refined_sql_query)
        final_answer, matplotlib_code = generate_final_answer(user_question, refined_sql_query, executed_query_result, csv_content)
        add_to_conversation_history(user_question, refined_sql_query, executed_query_result, final_answer, matplotlib_code)
        return {
            "success": 1,
            "response": final_answer,
            "chat_history": conversation_history
        }
    except Exception as e:
        logger.error(f"Chat endpoint failed. Exception: {e}")
        return {"success": 0,"response": "The bot is not able to temporarily answer your queries due to an internal issue."}