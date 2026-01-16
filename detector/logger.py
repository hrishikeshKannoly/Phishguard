import json
from datetime import datetime

LOG_FILE = "logs/detections.log"

def log_detection(input_data, url_result, text_result, final_result):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "input": input_data,
        "url_analysis": url_result,
        "text_analysis": text_result,
        "final_result": final_result
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")
