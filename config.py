# mail
MAIL_SENDER_ADDRESS = "shawninjuly@gmail.com"
MAIL_SENDER_NAME = "南川"
MAIL_APP_PASSWORD = "zjwigxgruzvgmfaw"  # google 应用专用密码！, ref: https://myaccount.google.com/apppasswords?pli=1&rapt=AEjHL4OCKSPTpmzjxIQv7oe8s6mbw7OdIUuDZJzV1Cl7cnfoXMLPp_8vb8eFOFu_fCH0qRntGfaH7Sl351UoHMEIchb5GpteLg
MAIL_SMTP_SERVER = 'smtp.gmail.com'
MAIL_SMTP_PORT = 465

# auth
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"  # openssl rand -hex 32
SECURITY_ALGO = "HS256"
SECURITY_ACCESS_TOKEN_EXPIRE_MINUTES = 1
NOTION_VISIT_URL = "https://gkleifeng.notion.site/da7ad92cb3414e6891c80e52541a6678"
NOTION_COOKIE = 'notion_browser_id=ee0024cf-69ba-452f-8b2e-aee3ac87fc25; intercom-id-gpfdrxfd=d072f01b-ec07-4e0a-8790-8c5735d46497; intercom-device-id-gpfdrxfd=54b4c53d-f4de-4ec2-a9f9-aca5640eabc4; intercom-session-gpfdrxfd=; notion_check_cookie_consent=false; __cf_bm=mXmsTZyOCNbeA5vtjpbTt6AzwXRCutaWn4l2POVinmA-1676470443-0-Ac4TUhTOuPhmaSFYtoevUDjRbBbxI0HccHqmCAKpnrYffK2TY/OBLY6uqLa+A6s3KAFGrGkVAt37WQPgoZXkQfY=; amp_af43d4=ee0024cf69ba452f8b2eaee3ac87fc25...1gpabddt6.1gpamrb1l.ji.8.jq''notion_browser_id=ee0024cf-69ba-452f-8b2e-aee3ac87fc25; intercom-id-gpfdrxfd=d072f01b-ec07-4e0a-8790-8c5735d46497; intercom-device-id-gpfdrxfd=54b4c53d-f4de-4ec2-a9f9-aca5640eabc4; intercom-session-gpfdrxfd=; notion_check_cookie_consent=false; __cf_bm=mXmsTZyOCNbeA5vtjpbTt6AzwXRCutaWn4l2POVinmA-1676470443-0-Ac4TUhTOuPhmaSFYtoevUDjRbBbxI0HccHqmCAKpnrYffK2TY/OBLY6uqLa+A6s3KAFGrGkVAt37WQPgoZXkQfY=; amp_af43d4=ee0024cf69ba452f8b2eaee3ac87fc25...1gpabddt6.1gpamrb1l.ji.8.jq'
NOTION_COL_MAP = {
    "name": "嘉宾姓名",
    "title": "title（25字内）",
    "avatar": "照片",
    "cities": "坐标",
}