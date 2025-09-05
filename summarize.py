from litellm import completion
from config import PROVIDER_MODEL as MODEL

def summarize(text, length="brief"):
    lengths = {"brief":"in 1–2 sentences","medium":"in 3–4 sentences","detailed":"in 5–6 sentences with key points"}
    r = completion(
        model=MODEL,
        messages=[
            {"role":"system","content":f"You are an expert summarizer. Summarize {lengths.get(length,'in 2–3 sentences')}"},
            {"role":"user","content":text}
        ],
        temperature=0.0, max_tokens=100,
    )
    return r.choices[0].message["content"].strip()

if __name__ == "__main__":
    sample = """Recent advances in AI… (Lemons are a citrus fruit. Like other citrus fruits, they contain vitamin C and other antioxidants.

Antioxidants are essential for human health. These compounds mop up free radicals in the body that can damage the body’s cells and lead to diseases, such as cancers.

Researchers believeTrusted Source that the flavonoids in lemon and other citrus fruits have antibacterial, anticancer, and antidiabetic properties.)"""
    print(summarize(sample, "brief"))
