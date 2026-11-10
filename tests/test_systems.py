from agentic_loop.main import Claim,classify_claim,simulated_agent_loop
from context_strategy.main import compress,token_estimate
from orchestrator.main import fork_state

def test_auto(): assert classify_claim(Claim("x","u","glass_damage",200,"x")) == "AUTO_PROCESS"
def test_manual(): assert classify_claim(Claim("x","u","vehicle_damage",2500,"x")) == "MANUAL_REVIEW"
def test_escalate_type(): assert classify_claim(Claim("x","u","theft",500,"x")) == "ESCALATE"
def test_escalate_amount(): assert classify_claim(Claim("x","u","other",10000,"x")) == "ESCALATE"
def test_loop_ends(): assert simulated_agent_loop(Claim("x","u","glass_damage",100,"x")) == "AUTO_PROCESS"
def test_context_keeps_edges():
    x=[{"text":"claim important"},{"text":"noise"},{"text":"repair approved"},{"text":"latest one"},{"text":"latest two"}]
    y=compress(x); assert y[0]==x[0] and y[-2:]==x[-2:]
def test_context_not_larger():
    x=[{"text":"claim"},{"text":"noise"},{"text":"noise"},{"text":"recent"},{"text":"recent"}]; assert token_estimate(compress(x)) <= token_estimate(x)
def test_fork_isolated():
    p={"shift":1,"processed_incidents":[1]}; c=fork_state(p,"A"); c["processed_incidents"].append(2); assert p["processed_incidents"]==[1]
