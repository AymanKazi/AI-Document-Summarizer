from .ollama_client import generate_summary

def summarize_text(text: str, reduction_ratio: float = 0.2):
    original_words = len(text.split())
    max_words = max(30, int(original_words * reduction_ratio))

    prompt = (
        f"Summarize the following document clearly and concisely.\n"
        f"The summary MUST NOT exceed {max_words} words.\n"
        f"Do NOT add introductory phrases.\n\n"
        f"{text}"
    )

    summary = generate_summary(prompt)
    summary_words = len(summary.split())

    return {
        "summary": summary,
        "original_words": original_words,
        "summary_words": summary_words
    }
