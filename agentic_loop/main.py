from dataclasses import dataclass

@dataclass
class Claim:
    claim_id: str
    customer: str
    claim_type: str
    amount: float
    description: str

CLAIMS = [
    Claim("CLM-1001", "Mario Novak", "vehicle_damage", 1250.0, "Rear bumper damaged"),
    Claim("CLM-1002", "John Smith", "theft", 12500.0, "Vehicle reported stolen"),
    Claim("CLM-1003", "Anna Brown", "glass_damage", 320.0, "Cracked windshield"),
]

def classify_claim(c):
    if c.claim_type == "theft" or c.amount >= 10000: return "ESCALATE"
    if c.amount >= 1000: return "MANUAL_REVIEW"
    return "AUTO_PROCESS"

def simulated_agent_loop(c):
    steps=[("tool_use", "classify_claim"), ("end_turn", classify_claim(c))]
    for i,(reason,value) in enumerate(steps,1):
        print(f"iteration={i} stop_reason={reason} result={value}")
        if reason == "end_turn": return value

if __name__ == "__main__":
    for claim in CLAIMS:
        print(f"\n{claim.claim_id}: {claim.customer}")
        simulated_agent_loop(claim)
