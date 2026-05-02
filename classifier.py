import re

ERROR_PATTERN = re.compile(r"(error|failed|exception|tempdb|camep_contact_history|camep_inbound_feedback|camep_outbound_feedback)", re.IGNORECASE)

ETL_JOB_PATTERN = re.compile(r"etl_job_id\s*=\s*tdcsmkt01_salesforce_ch_feedback", re.IGNORECASE)

PATTERNS = [
    # TEMPDB ERROR
    ("TEMPDB", re.compile(r"tempdb", re.IGNORECASE)),

    # CAMP CONTACT HISTORY (only if etl_job_id matches)
    ("CAMP_CONTACT_HISTORY", re.compile(r"Table data camep_contact_history is not ready.*Retry source check.*", re.IGNORECASE)),

    # CAMP INBOUND FEEDBACK (only if etl_job_id matches)
    ("CAMP_INBOUND_FEEDBACK", re.compile(r"Table data camep_inbound_feedback is not ready", re.IGNORECASE)),

    # CAMP OUTBOUND FEEDBACK (only if etl_job_id matches)
    ("CAMP_OUTBOUND_FEEDBACK", re.compile(r"Table data camep_outbound_feedback is not ready", re.IGNORECASE)),
]

def is_error_log(log_line):
    return bool(ERROR_PATTERN.search(log_line))

def classify_log(log_line, has_etl=False):
    # Check for TEMPDB first
    if PATTERNS[0][1].search(log_line):
        print(f"✅ Regex Matched → {PATTERNS[0][0]}")
        return PATTERNS[0][0]

    # For CAMP patterns, check if etl_job_id matches
    if has_etl:
        for category, pattern in PATTERNS[1:]:
            if pattern.search(log_line):
                print(f"✅ Regex Matched → {category}")
                return category

    print("🤖 No regex match → LLM required")
    return None