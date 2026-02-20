import time

def retry_execution(function, max_retries=5):
    retry_count = 0
    delay = 2

    while retry_count < max_retries:
        try:
            return function()
        except Exception as exc:
            retry_count += 1
            print(f"ERROR: {exc}")
            print(f"Retry {retry_count} in {delay}s")
            time.sleep(delay)
            delay *= 2

    raise Exception("Max retries exceeded")
    