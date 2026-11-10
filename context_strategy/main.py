import json
from pathlib import Path
KEYWORDS=("claim","damage","bumper","repair","estimate","approved")

def compress(messages):
    if len(messages) <= 2: return messages
    first=messages[:1]; recent=messages[-2:]
    middle=[m for m in messages[1:-2] if any(k in m["text"].lower() for k in KEYWORDS)]
    return first+middle+recent

def token_estimate(messages):
    return sum(len(m["text"].split()) for m in messages)

if __name__ == "__main__":
    data=json.loads(Path(__file__).with_name("conversation.json").read_text())
    out=compress(data)
    before,after=token_estimate(data),token_estimate(out)
    print(f"Original estimated tokens: {before}")
    print(f"Compressed estimated tokens: {after}")
    print(f"Reduction: {(1-after/before)*100:.1f}%")
    for m in out: print(m)
