import json, sqlite3
from pathlib import Path
DB=Path(__file__).with_name("orchestrator.db")
STATE=Path(__file__).with_name("state.json")

def setup():
    con=sqlite3.connect(DB); cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS incidents(id INTEGER PRIMARY KEY,title TEXT,severity TEXT,status TEXT)")
    cur.executemany("INSERT OR REPLACE INTO incidents VALUES(?,?,?,?)",[(1,"Payment service unavailable","critical","open"),(2,"Customer portal slow","medium","open"),(3,"Authentication service failure","critical","open"),(4,"Old reporting issue","low","closed")])
    con.commit(); con.close()

def critical_open():
    con=sqlite3.connect(DB); rows=con.execute("SELECT id,title,severity FROM incidents WHERE status='open' AND severity='critical'").fetchall(); con.close(); return rows

def load_state():
    return json.loads(STATE.read_text()) if STATE.exists() else {"shift":1,"processed_incidents":[]}

def save_state(s): STATE.write_text(json.dumps(s,indent=2))

def fork_state(s, investigation):
    child={**s, "investigation": investigation, "processed_incidents": list(s["processed_incidents"])}
    return child

if __name__ == "__main__":
    setup(); state=load_state(); print("Recovered state:", state)
    rows=critical_open(); print("SQL pre-filtered incidents:", rows)
    for row in rows:
        if row[0] not in state["processed_incidents"]: state["processed_incidents"].append(row[0])
    child=fork_state(state,"authentication root cause")
    save_state(state); print("Saved tiny state:", state); print("Forked investigation:", child)
