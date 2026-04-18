# Engineered feature extractor — computes the 15 features in blueprint §9.
# extract(user_id, date) → dict with keys in exact order:
#   logon_count, logoff_count, offhours_logon_ratio, weekend_logon_ratio,
#   unique_hosts_count, usb_connect_count, bytes_copied_to_usb,
#   unique_files_accessed, file_write_count, file_read_count,
#   unique_http_hosts, external_http_ratio, email_send_count,
#   email_bytes_total, email_attachment_count_mean.
# Writes result to user_day_features table with feature_version="v1".
