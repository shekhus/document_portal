# Prepare prompt template
from langchain_core.prompts import ChatPromptTemplate

# Prompt for document analysis
document_analysis_prompt = ChatPromptTemplate.from_template("""
You are a highly capable assistant trained to analyze and summarize documents.
Return ONLY valid JSON matching the exact schema below.

{format_instructions}

Analyze this document:
{document_text}
""")

# Prompt for document comparison
document_comparison_prompt = ChatPromptTemplate.from_template("""
You will be provided with content from two PDFs. Your tasks are as follows:

1. Compare the content in two PDFs
2. Identify the difference in PDF and note down the page number 
3. The output you provide must be page wise comparison content 
4. If any page do not have any change, mention as 'NO CHANGE' 

Input documents:

{combined_docs}

Your response should follow this format:

{format_instruction}
""")


# Central dictionary to register prompts
PROMPT_REGISTRY = {
    "document_analysis": document_analysis_prompt,
    "document_comparison": document_comparison_prompt,
    # "contextualize_question": contextualize_question_prompt,
    # "context_qa": context_qa_prompt,
}