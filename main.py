# main.py

from config import LOG_FOLDER_PATH, EMAIL_MAP
from log_reader import read_all_logs
from classifier import classify_log, is_error_log
from summarizer import llm_classify_and_summarize
from notifier import send_email
from api_reader import fetch_logs_from_api

def main():
    print("📂 Reading all log files...")
    logs = read_all_logs(LOG_FOLDER_PATH)
    print("🌐 Fetching logs from API...")
    #logs = fetch_logs_from_api()

    for log_obj in logs:
        file_name = log_obj["file_name"]
        lines = log_obj["lines"]

        print(f"\n🔍 Processing file: {file_name}")

        error_lines = [line for line in lines if is_error_log(line)]
        unmatched_errors = []

        has_etl = any('tdcsmkt01_salesforce_ch_feedback' in line for line in lines)

        for error_line in error_lines:
            category = classify_log(error_line, has_etl)

            if category:
                email = EMAIL_MAP.get(category)
                summary = llm_classify_and_summarize(error_line)

                print(f"📧 Sending {category} alert for {file_name}")
                print(f"Summary: {summary}")
                send_email(
                    email,
                    f"[ALERT] {category} | File: {file_name}",
                    summary
                )
            else:
                unmatched_errors.append(error_line)

        if unmatched_errors:
            all_unmatched = "\n".join(unmatched_errors)
            result = llm_classify_and_summarize(all_unmatched)

            print(f"📧 Sending GENERAL alert for {file_name}")
            print(f"Summary: {result}")
            send_email(
                EMAIL_MAP["OTHER"],
                f"[ALERT] UNKNOWN ISSUE | File: {file_name}",
                result
            )

    print("\n✅ All files processed")

if __name__ == "__main__":
    main()